Get-EventLog -LogName System -Newest 50 |
Export-Csv eventos_sistema_rafa.csv –NoTypeInformation
