New-Item -Path C:\Servicios -ItemType Directory || Write-Host "El directorio ya existe"
New-Item -Path C:\Procesos -ItemType Directory || Write-Host "El directorio ya existe"
New-Item -Path C:\Backup -ItemType Directory || Write-Host "El directorio ya existe"


New-Item -Path C:\Servicios\Servicios.txt -ItemType File || Write-Host "El archivo ya existe"
New-Item -Path C:\Procesos\Procesos.txt -ItemType File || Write-Host "El archivo ya está creado"

Get-Service C:\Servicios\servicios.txt
Get-Process C:\Procesos\procesos.txt

Remove-Item C:\Servicios Recurse -Force
Remove-Item C:\Procesos Recurse -Force




