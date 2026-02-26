# SOLUCIÓN 34
Get-EventLog -LogName System -EntryType Error -Newest 100 | 
  Select-Object TimeGenerated, Source, EventID, EntryType, Message |
  Export-Csv .\errores_system.csv -NoTypeInformation
