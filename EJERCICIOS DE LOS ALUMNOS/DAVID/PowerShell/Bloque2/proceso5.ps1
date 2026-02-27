Get-services  Write-Host "Deteniendo spooler"
Stop-Service Spooler
Get-Service Spooler
write-host "Iniciando spooler"