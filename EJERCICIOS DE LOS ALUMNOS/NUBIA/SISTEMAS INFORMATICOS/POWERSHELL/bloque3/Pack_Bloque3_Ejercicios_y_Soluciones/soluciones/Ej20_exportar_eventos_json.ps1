# SOLUCIÓN 20
Get-EventLog -LogName Application -Newest 30 |
  ConvertTo-Json -Depth 3 | Out-File .\app_last30.json -Encoding utf8
