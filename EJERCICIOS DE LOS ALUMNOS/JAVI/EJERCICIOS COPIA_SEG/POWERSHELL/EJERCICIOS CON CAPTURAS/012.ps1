# Elimina la tarea si ya existe
if (Get-ScheduledTask -TaskName "Guardar_Log_Diario" -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName "Guardar_Log_Diario" -Confirm:$false
}

# Crear carpeta si no existe
if (!(Test-Path "C:\Logs")) {
    New-Item -Path "C:\Logs" -ItemType Directory | Out-Null
}

# Acción
$script = "Add-Content -Path 'C:\Logs\DailyLog.txt' -Value ('Log entry at ' + (Get-Date))"
$accion = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -Command `"$script`""

# Disparador
$disparador = New-ScheduledTaskTrigger -Daily -At 9am

# Registrar tarea
Register-ScheduledTask -TaskName "Guardar_Log_Diario" -Action $accion -Trigger $disparador

