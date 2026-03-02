# SOLUCIÓN 15
$desde = (Get-Date).AddHours(-24)
Get-EventLog -LogName System | Where-Object TimeGenerated -ge $desde
