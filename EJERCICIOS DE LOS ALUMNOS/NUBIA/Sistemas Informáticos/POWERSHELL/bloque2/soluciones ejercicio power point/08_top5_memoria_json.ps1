# Exportar a JSON los 5 procesos con mayor WorkingSet (sin transformar a MB)
Get-Process |
  Sort-Object WorkingSet -Descending |
  Select-Object -First 5 Name, Id, WorkingSet |
  ConvertTo-Json |
  Out-File .\top5_memoria.json -Encoding utf8
