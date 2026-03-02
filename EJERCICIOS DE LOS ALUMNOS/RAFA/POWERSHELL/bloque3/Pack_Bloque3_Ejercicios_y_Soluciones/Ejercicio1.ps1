Test-Connection chagpt.com -Count 4
Test-NetConnection -ComputerName google.com -Port 443
Get-NetIPAddress | Where-Object IPv4Address -eq '169.254.251.107'

