
# Daily GitHub Automation

# Find the project folder
$RepoPath = Split-Path -Parent $PSScriptRoot
Set-Location $RepoPath

# Get today's date
$Today = Get-Date -Format "yyyy-MM-dd"

# Create daily log folder
$LogFolder = Join-Path $RepoPath "Daily-Logs"
New-Item -ItemType Directory -Force -Path $LogFolder | Out-Null

# Create today's learning log
$LogFile = Join-Path $LogFolder "Day-$Today.md"

if (!(Test-Path $LogFile)) {
    $Content = @"
# Daily Learning Log - $Today

## Topics Studied
-

## Coding Practice
-

## Practical Work
-

## What I Learned
-

## Tomorrow's Goal
-

## Status
Not updated yet
"@

    Set-Content -Path $LogFile -Value $Content
    Write-Host "Daily learning log created."
}
else {
    Write-Host "Today's learning log already exists."
}

# Upload changes to GitHub
git add -A

git diff --cached --quiet

if ($LASTEXITCODE -ne 0) {
    git commit -m "Daily update: $Today"
}

git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "GitHub upload successful!"
}
else {
    Write-Host "Upload failed. Check your internet and GitHub authentication."
}
