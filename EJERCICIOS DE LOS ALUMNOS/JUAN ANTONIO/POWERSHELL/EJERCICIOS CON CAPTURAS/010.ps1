# Define la acción (abrir el Bloc de notas)
$accion = New-ScheduledTaskAction -Execute 'notepad.exe'

# Define el disparador (cada día a las 10:00)
$disparador = New-ScheduledTaskTrigger -Daily -At 10am

# Registra la tarea con un nombre
Register-ScheduledTask -TaskName "Abrir_Notepad" -Action $accion -Trigger $disparador

