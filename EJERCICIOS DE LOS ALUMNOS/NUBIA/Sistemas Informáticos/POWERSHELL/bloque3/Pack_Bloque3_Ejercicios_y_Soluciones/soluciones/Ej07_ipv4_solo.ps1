# SOLUCIÓN 7
Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -and $_.IPAddress -ne '0.0.0.0'} | Select-Object IPAddress, InterfaceAlias
