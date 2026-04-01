# SOLUCIÓN 22
Get-EventLog -LogName System | Where-Object Source -like '*Service Control Manager*'
