Get-EventLog -LogName System -Newest 50 |
Export-csv c:\reportes\eventos_sistema.csv  -NoTypeInformation


