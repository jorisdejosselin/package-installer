# Package Install Script

$packages = @(
{0}
)

function Check-PackageManager {{
    try {{
        winget --version
        return $true
    }}
    catch {{
        Write-Host "Package manager is not installed. Please install winget first."
        return $false
    }}
}}

function Install-Package {{
    param($packageId)
    Write-Host "Installing $packageId..."
    winget install --id $packageId --silent
    if ($LASTEXITCODE -eq 0) {{
        Write-Host "$packageId installed successfully." -ForegroundColor Green
    }} else {{
        Write-Host "Failed to install $packageId." -ForegroundColor Red
    }}
}}

if (Check-PackageManager) {{
    foreach ($package in $packages) {{
        Install-Package $package
    }}
    Write-Host "All installations completed."
}} else {{
    Write-Host "Script execution stopped due to missing package manager."
}}