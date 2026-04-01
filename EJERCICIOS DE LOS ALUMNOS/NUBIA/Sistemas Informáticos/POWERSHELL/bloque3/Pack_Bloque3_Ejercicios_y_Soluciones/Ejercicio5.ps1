Get-ScheduledTask
Write-Output "mostrando solo algunos datos"
Get-ScheduledTask | Select TaskName, State
