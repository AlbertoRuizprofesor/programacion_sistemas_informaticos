# SOLUCIÓN 24
$desde=(Get-Date).AddDays(-7)
Get-EventLog -LogName System -EntryType Error |
  Where-Object TimeGenerated -ge $desde |
  Group-Object Source | Sort-Object Count -Descending | Select-Object -First 5 Name,Count
