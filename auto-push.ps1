# PowerShell script to automatically commit and push changes to GitHub

param(
    [string]$Message = "Auto-commit: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
)

# Colors for output
$InfoColor = "Cyan"
$SuccessColor = "Green"
$ErrorColor = "Red"
$WarningColor = "Yellow"

Write-Host "========================================" -ForegroundColor $InfoColor
Write-Host "  Face Recognition - Auto Push Script  " -ForegroundColor $InfoColor
Write-Host "========================================" -ForegroundColor $InfoColor
Write-Host ""

# Check if we're in a git repository
$gitDir = git rev-parse --git-dir 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Not in a git repository!" -ForegroundColor $ErrorColor
    exit 1
}

Write-Host "[1/4] Checking git status..." -ForegroundColor $InfoColor
$status = git status --porcelain
if ([string]::IsNullOrEmpty($status)) {
    Write-Host "No changes to commit." -ForegroundColor $WarningColor
    exit 0
}

Write-Host "Changes detected:" -ForegroundColor $SuccessColor
Write-Host $status
Write-Host ""

Write-Host "[2/4] Staging all changes..." -ForegroundColor $InfoColor
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to stage changes!" -ForegroundColor $ErrorColor
    exit 1
}
Write-Host "✓ Changes staged" -ForegroundColor $SuccessColor

Write-Host ""
Write-Host "[3/4] Creating commit: '$Message'" -ForegroundColor $InfoColor
git commit -m $Message
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to create commit!" -ForegroundColor $ErrorColor
    exit 1
}
Write-Host "✓ Commit created" -ForegroundColor $SuccessColor

Write-Host ""
Write-Host "[4/4] Pushing to GitHub..." -ForegroundColor $InfoColor
git push
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully pushed to GitHub!" -ForegroundColor $SuccessColor
    Write-Host ""
    Write-Host "========================================" -ForegroundColor $SuccessColor
    Write-Host "  Push completed successfully!        " -ForegroundColor $SuccessColor
    Write-Host "========================================" -ForegroundColor $SuccessColor
} else {
    Write-Host "WARNING: Push encountered an issue" -ForegroundColor $WarningColor
    Write-Host "Please check your GitHub authentication and network connection."
    exit 1
}
