import PyInstaller.__main__
import shutil
from pathlib import Path

def build_executable():
    PyInstaller.__main__.run([
        'package_installer.py',
        '--onefile',
        '--name=package_installer.exe',
        '--add-data=windows/templates/install_script_template.ps1:windows/templates'
    ])

    # Copy the executable to the project root
    dist_path = Path('dist/package_installer.exe')
    if dist_path.exists():
        shutil.copy(dist_path, 'package_installer.exe')
        print("Executable created: package_installer.exe")
    else:
        print("Failed to create executable")

if __name__ == "__main__":
    build_executable()