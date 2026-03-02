# SOLUCIÓN 1
Test-Connection google.com -Count 4 | Select-Object Address, IPV4Address, ResponseTime, Status
