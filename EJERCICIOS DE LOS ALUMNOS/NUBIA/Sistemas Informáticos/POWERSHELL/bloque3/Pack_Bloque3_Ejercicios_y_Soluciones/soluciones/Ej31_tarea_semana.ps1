# SOLUCIÓN 31
$action = New-ScheduledTaskAction -Execute 'PowerShell.exe' -Argument '-File C:\Scripts\backup.ps1'
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 08:30
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'BackupSemanal' -Description 'Backup cada lunes 08:30' -ErrorAction SilentlyContinue
