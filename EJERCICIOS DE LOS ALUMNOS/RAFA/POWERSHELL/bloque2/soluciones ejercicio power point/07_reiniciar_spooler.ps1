# Reiniciar servicio Spooler (puede requerir permisos de administrador)
Get-Service Spooler | Select-Object Name, Status
Restart-Service -Name Spooler
Get-Service Spooler | Select-Object Name, Status
