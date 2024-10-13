import typer
import json
import os
import subprocess
import git

app = typer.Typer()

DEFAULT_PACKAGES_FILE = "windows/packages.json"
LOCAL_CONFIG_FILE = ".localpackages"
SCRIPT_TEMPLATE_FILE = "windows/templates/install_script_template.ps1"

def load_packages(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_packages(packages, file_path):
    with open(file_path, 'w') as f:
        json.dump(packages, f, indent=2)

def load_local_config():
    if os.path.exists(LOCAL_CONFIG_FILE):
        with open(LOCAL_CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_local_config(config):
    with open(LOCAL_CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def generate_powershell_script(packages):
    with open(SCRIPT_TEMPLATE_FILE, 'r') as f:
        template = f.read()

    apps_list = '\n'.join(f'    "{pkg}"' for pkg in packages)
    return template.format(apps_list)

@app.command()
def install(
    packages_file: str = typer.Option(DEFAULT_PACKAGES_FILE, help="Path to the packages JSON file"),
    save_to_git: bool = typer.Option(False, help="Save changes to git repository")
):
    """
    Install packages using winget based on the specified JSON file.
    """
    packages = load_packages(packages_file)
    script = generate_powershell_script(packages)

    # Save the script to a temporary file
    temp_script_path = "temp_winget_install.ps1"
    with open(temp_script_path, 'w') as f:
        f.write(script)

    # Run the PowerShell script
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", temp_script_path], check=True)
    finally:
        os.remove(temp_script_path)

    if save_to_git:
        local_config = load_local_config()
        repo_path = local_config.get('repo_path')
        if not repo_path:
            repo_path = typer.prompt("Enter the path to your git repository")
            local_config['repo_path'] = repo_path
            save_local_config(local_config)

        repo = git.Repo(repo_path)
        file_path = os.path.join(repo_path, packages_file)
        save_packages(packages, file_path)
        repo.git.add(file_path)
        repo.git.commit('-m', 'Update package list')
        repo.git.push()
        typer.echo(f"Changes saved to git repository: {repo_path}")

@app.command()
def add_package(
    package: str = typer.Argument(..., help="Package ID to add"),
    packages_file: str = typer.Option(DEFAULT_PACKAGES_FILE, help="Path to the packages JSON file")
):
    """
    Add a package to the JSON file.
    """
    packages = load_packages(packages_file)
    if package not in packages:
        packages.append(package)
        save_packages(packages, packages_file)
        typer.echo(f"Added {package} to {packages_file}")
    else:
        typer.echo(f"{package} is already in {packages_file}")

@app.command()
def remove_package(
    package: str = typer.Argument(..., help="Package ID to remove"),
    packages_file: str = typer.Option(DEFAULT_PACKAGES_FILE, help="Path to the packages JSON file")
):
    """
    Remove a package from the JSON file.
    """
    packages = load_packages(packages_file)
    if package in packages:
        packages.remove(package)
        save_packages(packages, packages_file)
        typer.echo(f"Removed {package} from {packages_file}")
    else:
        typer.echo(f"{package} is not in {packages_file}")

if __name__ == "__main__":
    app()