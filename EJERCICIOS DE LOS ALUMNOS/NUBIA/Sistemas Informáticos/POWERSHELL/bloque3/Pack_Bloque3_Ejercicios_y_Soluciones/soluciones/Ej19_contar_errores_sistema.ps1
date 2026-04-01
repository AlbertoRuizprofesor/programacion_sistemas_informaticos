# SOLUCIÓN 19
$desde=(Get-Date).AddHours(-8)
(Get-EventLog -LogName System -EntryType Error | Where-Object TimeGenerated -ge $desde).Count
