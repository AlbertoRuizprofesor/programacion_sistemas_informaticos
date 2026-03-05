# Define la acción (un script que guarda un timestamp en un archivo de log) 
# Asegúrate de que la carpeta C:\Logs ya existe.
$script = "Add-Content -Path C:\Logs\DailyLog.txt -Value ('Log entry at ' + (Get-Date))" $accion = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -Command `"$script`"“
# Define el disparador (diario a las 9:00, por ejemplo) 
$disparador = New-ScheduledTaskTrigger -Daily -At 9am # Registra la tarea Register-ScheduledTask -TaskName "Guardar_Log_Diario" -Action $accion -Trigger $
