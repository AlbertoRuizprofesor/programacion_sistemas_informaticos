
Get-WinEvent -FilterHashtable @{LogName='information';ID=19} 
| Where-Object { $_.Properties[5].Value -eq 'alber' }