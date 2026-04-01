# SOLUCIÓN 32
Start-ScheduledTask -TaskName 'BackupSemanal' -ErrorAction SilentlyContinue
Get-ScheduledTaskInfo -TaskName 'BackupSemanal' -ErrorAction SilentlyContinue | Select-Object LastRunTime, LastTaskResult
