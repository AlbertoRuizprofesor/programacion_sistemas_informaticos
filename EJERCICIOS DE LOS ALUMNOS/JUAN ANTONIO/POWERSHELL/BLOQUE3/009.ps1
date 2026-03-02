# Muestra los 10 primeros procesos con más uso de memoria
Get-Process | Sort-Object WS -Descending | Select-Object -First 10 Name, ID, WS