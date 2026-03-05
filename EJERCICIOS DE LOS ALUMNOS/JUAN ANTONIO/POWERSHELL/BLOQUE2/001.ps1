New-Item -Path C:\Backup -ItemType Directory || Write-Host "El directorio ya existe"
Copy-Item C:\Reportes\Resumen.txt C:\Backup
Move-Item C:\Backup\Resumen.txt C:\Final