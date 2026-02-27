# 1. Creamos la acción
$action = New-ScheduledTaskAction -Execute 'notepad.exe'

# 2. Creamos el disparador
$trigger = New-ScheduledTaskTrigger -At 11:25 -Once

# 3. Registramos la tarea
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AbrirNotepad9' -Description 'Abrir Notepad al mediodía'
