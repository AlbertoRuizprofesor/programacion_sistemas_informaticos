# 1. Creamos la acción
$action = New-ScheduledTaskAction -Execute 'calc.exe'

# 2. Crear un disipador, con una hora y una sola vez
$trigger = New-ScheduledTaskTrigger -At 09:30 -Once

# 3. Registramos la nueva tarea
Register-Scheduledtask -Action $action -Trigger $trigger -Taskname 'Abrir calculadora' -Description 'Abrir calculadora'