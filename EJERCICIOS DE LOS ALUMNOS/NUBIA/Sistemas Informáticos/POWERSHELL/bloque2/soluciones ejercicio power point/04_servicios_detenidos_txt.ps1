# Listar servicios detenidos y exportar a TXT
Get-Service |
  Where-Object Status -eq 'Stopped' |
  Select-Object Name, DisplayName, Status |
  Out-File .\servicios_detenidos.txt -Encoding utf8
