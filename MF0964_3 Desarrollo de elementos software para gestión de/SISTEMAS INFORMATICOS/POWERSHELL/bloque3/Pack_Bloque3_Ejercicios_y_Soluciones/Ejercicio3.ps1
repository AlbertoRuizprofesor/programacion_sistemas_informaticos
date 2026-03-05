Write-Output "aquí de los 100 ultimos logs, cuales han sido errores_________________________________________________"
Get-EventLog -LogName System -Newest 100 | Where-Object EntryType -eq 'error'
#Write-Output "otra forma, aquí los ultimos 20 errores_________________________________________________"
#Get-EventLog -LogName Application -EntryType Error -Newest 20
#Write-Output 'muesttra todos los logs'
#Get-WinEvent -ListLog *


