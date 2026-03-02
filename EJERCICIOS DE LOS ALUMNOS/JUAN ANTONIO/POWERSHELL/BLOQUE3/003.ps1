# Muestra la dirección IPv4 principal del equipo
Get-NetIPAddress -InterfaceAlias "Wi-Fi" -AddressFamily IPv4 |
    Where-Object {$_.IPAddress -notlike "169.*"} |
    Select-Object InterfaceAlias, IPAddress
