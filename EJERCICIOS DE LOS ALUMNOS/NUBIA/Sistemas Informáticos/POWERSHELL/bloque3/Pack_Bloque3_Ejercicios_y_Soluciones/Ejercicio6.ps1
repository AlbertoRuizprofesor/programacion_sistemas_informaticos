$action = New-ScheduledTaskAction -Execute 'notepad.exe'
$trigger = New-ScheduledTaskTrigger -At 13:45 -Once
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AbrirNotepad' -Description 'Abrir Notepad al mediodía'
