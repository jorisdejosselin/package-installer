# Winget Install Scripts

This repository contains scripts for bulk installation of applications using Windows Package Manager (winget).

## Main Script: Smart Winget Install

The primary script in this repository is `smart-winget-install.ps1`, a PowerShell script that automates the installation of multiple applications using winget.

### Features

- Checks if winget is installed before attempting to use it
- Installs a predefined list of applications silently
- Provides colored output for successful and failed installations
- Easy to modify the list of applications to install

### Prerequisites

- Windows 10 (1809 or later) or Windows 11
- [Windows Package Manager (winget)](https://docs.microsoft.com/en-us/windows/package-manager/winget/) installed

### Usage

1. Clone this repository or download the `smart-winget-install.ps1` file.
2. Open PowerShell as Administrator.
3. Navigate to the directory containing the script.
4. Run the script:

```powershell
.\windows\smart-winget-install.ps1
```

Alternatively, you can run the script directly from GitHub:

```powershell
Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jorisdejosselin/package-scripts/refs/heads/main/windows/smart-winget-install.ps1" -UseBasicParsing).Content
```

Replace `yourusername` with your actual GitHub username.

### Customizing the Application List

To modify the list of applications to install, edit the `$apps` array in the `smart-winget-install.ps1` file. Add or remove application IDs as needed.

## Contributing

Contributions to improve the scripts or add new functionality are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Please review the script and understand its actions before running it. Always exercise caution when running scripts, especially those that install software on your system.

## Acknowledgments

- Microsoft for creating and maintaining [winget](https://github.com/microsoft/winget-cli)
- All the application developers whose software can be installed using this script