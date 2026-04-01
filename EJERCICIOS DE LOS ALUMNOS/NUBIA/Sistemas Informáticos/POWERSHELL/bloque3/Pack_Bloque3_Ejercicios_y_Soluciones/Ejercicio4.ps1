Get-EventLog -LogName System -Newest 50 | Export-Csv eventos_sistema.csv -NoTypeInformation
