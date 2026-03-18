Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} | 
Where-Object { $_.Properties[5].Value -eq '2-DAW' } | 
Select-Object TimeCreated, Message | 
Format-Table -AutoSize

