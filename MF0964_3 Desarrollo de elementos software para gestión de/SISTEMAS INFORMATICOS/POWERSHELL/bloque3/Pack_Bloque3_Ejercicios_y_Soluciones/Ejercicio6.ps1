# 1. Creamos la acción
$action = New-ScheduledTaskAction -Execute 'notepad.exe'

# 2. Creamos el disparador
$trigger = New-ScheduledTaskTrigger -At 08:43 -Once

# 3. Registramos la tarea
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName 'AbrirNotepad5' -Description 'Abrir Notepad al mediodía'