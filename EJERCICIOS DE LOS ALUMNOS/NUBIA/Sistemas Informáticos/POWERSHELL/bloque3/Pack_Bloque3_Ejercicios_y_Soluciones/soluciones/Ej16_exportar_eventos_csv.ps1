# SOLUCIÓN 16
Get-EventLog -LogName Security -Newest 50 -ErrorAction SilentlyContinue | 
  Export-Csv .\eventos_seguridad.csv -NoTypeInformation
