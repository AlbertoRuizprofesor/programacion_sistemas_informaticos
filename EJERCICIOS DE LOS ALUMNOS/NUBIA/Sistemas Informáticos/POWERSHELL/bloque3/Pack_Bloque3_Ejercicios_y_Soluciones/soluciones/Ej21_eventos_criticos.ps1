# SOLUCIÓN 21
Get-EventLog -LogName System -Newest 200 |
  Where-Object { $_.EntryType -in @('Error','FailureAudit') } | Select-Object -First 10
