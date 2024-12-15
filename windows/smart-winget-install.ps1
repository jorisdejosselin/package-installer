# Smart Winget Install Script

# Define an array of application IDs
$apps = @(
    "7zip.7zip",
    "AutoHotkey.AutoHotkey",
    "EpicGames.EpicGamesLauncher",
    "Mozilla.Firefox",
    "GIMP.GIMP",
    "Git.Git",
    "Google.Chrome",
    "Greenshot.Greenshot",
    "Notepad++.Notepad++",
    "NSSM.NSSM",
    "Playnite.Playnite",
    "QBittorrent.QBittorrent",
    "SABnzbd.SABnzbd",
    "Spotify.Spotify",
    "Valve.Steam",
    "Sunshine.Sunshine",
    "Ubisoft.UbisoftConnect",
    "Ubisoft.Uplay",
    "Vortex.Vortex",
    "WinDirStat.WinDirStat",
    "WinRAR.WinRAR",
    "WireGuard.WireGuard",
    "LizardByte.Sunshine",
    "Microsoft.VisualStudioCode",
    "Discord.Discord",
    "AgileBits.1Password",
    "Spotify.Spotify"
)

# Function to check if Winget is installed
function Check-Winget {
    try {
        winget --version
        return $true
    }
    catch {
        Write-Host "Winget is not installed. Please install Winget first."
        return $false
    }
}

# Function to install an app
function Install-App {
    param($appId)
    Write-Host "Installing $appId..."
    winget install --id $appId --silent
    if ($LASTEXITCODE -eq 0) {
        Write-Host "$appId installed successfully." -ForegroundColor Green
    } else {
        Write-Host "Failed to install $appId." -ForegroundColor Red
    }
}

# Main script
if (Check-Winget) {
    foreach ($app in $apps) {
        Install-App $app
    }
    Write-Host "All installations completed."
} else {
    Write-Host "Script execution stopped due to missing Winget."
}
