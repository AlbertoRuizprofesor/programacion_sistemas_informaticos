# 1. Definir la ACCIÓN
# Aquí indicas qué aplicación quieres lanzar. 
# "notepad.exe" es el ejecutable del Bloc de notas.
$action = New-ScheduledTaskAction -Execute "calc.exe" 

# 2. Definir el DISPARADOR (Trigger)
# Al usar -Daily, la tarea se repetirá cada día.
# El formato "09:15" usa el reloj de 24 horas.
$trigger = New-ScheduledTaskTrigger -At 09:31 -Once


# 3. REGISTRAR la tarea
# TaskName: Es el nombre que verás en el "Programador de tareas".
# Action y Trigger: Llaman a las variables que creaste arriba.
Register-ScheduledTask -TaskName "AbrirTareaProgramada4" -Action $action -Trigger $trigger -Description "Ejecuta un programa a una hora fija"