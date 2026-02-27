# Asegúrate de que la carpeta existe
if (!(Test-Path "C:\Logs")) {
    New-Item -Path "C:\Logs" -ItemType Directory | Out-Null
}

# Define la acción (guardar timestamp en el log)
$script = "Add-Content -Path 'C:\Logs\DailyLog.txt' -Value ('Log entry at ' + (Get-Date))"
$accion = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -Command `"$script`""

# Define el disparador (diario a las 9:00)
$disparador = New-ScheduledTaskTrigger -Daily -At 9am

# Registra la tarea
Register-ScheduledTask -TaskName "Guardar_Log_Diario" -Action $accion -Trigger $disparador


