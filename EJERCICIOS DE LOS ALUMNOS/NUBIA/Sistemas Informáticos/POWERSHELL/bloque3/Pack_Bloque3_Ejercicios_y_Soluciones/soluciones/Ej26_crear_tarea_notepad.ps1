# SOLUCIÓN 26
$action = New-ScheduledTaskAction -Execute 'notepad.exe'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date.AddHours(10)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AbrirNotepad10' -Description 'Abrir Notepad a las 10:00' -ErrorAction SilentlyContinue
