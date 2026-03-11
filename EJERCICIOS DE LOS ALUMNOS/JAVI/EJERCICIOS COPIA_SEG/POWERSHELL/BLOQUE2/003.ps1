
# Crea las carpetas
New-Item -Path C:\INFORMESPROCESOS -ItemType Directory || Write-Host "El directorio ya existe"
New-Item -Path C:\INFORMESSERVICIOS -ItemType Directory || Write-Host "El directorio ya existe"
New-Item -Path C:\BACKUP -ItemType Directory || Write-Host "El directorio ya está creado"

#Crea los ficheros
New-Item -Path C:\INFORMESPROCESOS\INFORMESPROCESOS.txt -ItemType File || Write-Host "El archivo ya existe"
New-Item -Path C:\INFORMESSERVICIOS\INFORMESSERVICIOS.txt -ItemType File || Write-Host "El archivo ya existe"
New-Item -Path C:\INFORMESSERVICIOS\BACKUP.txt -ItemType File || Write-Host "El archivo ya existe"

#Copia los dos primeros a BACKUP
Copy-Item C:\INFORMESPROCESOS\INFORMESPROCESOS.txt C:\BACKUP || Write-Host 
Copy-Item C:\INFORMESSERVICIOS\INFORMESSERVICIOS.txt C:\BACKUP || Write-Host

#Mover BACKUP.TXT a BACKUP
Move-Item C:\INFORMESSERVICIOS\BACKUP.txt C:\BACKUP

#Borra Carpetas
Remove-Item C:\INFORMESPROCESOS Recurse -Force
Remove-Item C:\INFORMESSERVICIOS Recurse -Force
Remove-Item C:\BACKUP Recurse -Force
Remove-Item C:\Final Recurse -Force


