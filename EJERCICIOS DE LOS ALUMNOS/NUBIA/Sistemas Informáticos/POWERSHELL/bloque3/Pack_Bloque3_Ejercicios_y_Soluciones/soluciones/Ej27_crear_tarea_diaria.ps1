# SOLUCIÓN 27
$action = New-ScheduledTaskAction -Execute 'PowerShell.exe' -Argument '-File C:\Scripts\informe.ps1'
$trigger = New-ScheduledTaskTrigger -Daily -At 09:00
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'InformeDiario09' -Description 'Ejecuta informe diario' -ErrorAction SilentlyContinue
