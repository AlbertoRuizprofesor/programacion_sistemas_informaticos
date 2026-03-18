# Define la acción (abrir el Bloc de notas) 
$accion = New-ScheduledTaskAction -Execute 'notepad.exe’ 
# Define el disparador (cada día a las 10:00) 
$disparador = New-ScheduledTaskTrigger -At 11:42am -Once
# Registra la tarea con un nombre 
Register-ScheduledTask -TaskName "Abrir_Notepad_2" -Action $accion -Trigger $disparador
