Get-EventLog -LogName System -Newest 50 | 
Export-Csv c:\reportes\eventos_sistema.csv -NoTypeInformation
