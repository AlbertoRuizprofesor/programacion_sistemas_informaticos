Get-Eventlog -Logname System -Newest 50 |
Export-Csv c:\reporte\eventos_sistema.csv -NoTypeInformation