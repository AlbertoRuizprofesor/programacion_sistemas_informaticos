cls
Get-NetAdapter 'Ethernet 2'
Get-NetAdapter | Where-Object Status -eq "Disconnected"
