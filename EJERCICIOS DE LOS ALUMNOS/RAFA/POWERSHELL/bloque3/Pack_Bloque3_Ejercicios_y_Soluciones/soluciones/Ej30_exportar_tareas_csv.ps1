# SOLUCIÓN 30
Get-ScheduledTask | Select-Object TaskName, State | Export-Csv .\tareas.csv -NoTypeInformation
