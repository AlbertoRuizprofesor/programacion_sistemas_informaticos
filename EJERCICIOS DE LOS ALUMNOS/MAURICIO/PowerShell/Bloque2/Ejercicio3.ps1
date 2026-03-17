New-Item -path C:\Informe_Procesos -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")
New-Item -path C:\Informe_Servicios -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")
New-Item -path C:\Backup1 -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")

New-Item -path C:\Informe_Procesos\informeprocesos.txt -ItemType File || Write-Host ("File / Archivo Creado")
New-Item -path C:\Informe_Servicios\informeservicios.txt -ItemType File || Write-Host ("File / Archivo Creado")
New-Item -path C:\Informe_Procesos\anual.txt -ItemType File || Write-Host ("File / Archivo Creado")

Copy-Item -Path "C:\Informe_Procesos\informeprocesos.txt" -Destination "C:\Backup1" -Recurse -Verbose
Copy-Item -Path "C:\Informe_Servicios\informeservicios.txt" -Destination "C:\Backup1" -Recurse -Verbose

Move-Item -Path "C:\Informe_Procesos\anual.txt" -Destination "C:\Backup1" -Verbose

#Remove-Item -path C:\Backup1\anual.txt -Recurse -Force

