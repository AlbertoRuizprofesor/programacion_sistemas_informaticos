# SOLUCIÓN 36
$action = New-ScheduledTaskAction -Execute 'PowerShell.exe' -Argument '-File C:\Scripts\auditoria.ps1'
$trigger = New-ScheduledTaskTrigger -Daily -At 09:00
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AuditoriaDiaria' -Description 'Auditoría de red y sistema' -ErrorAction SilentlyContinue
