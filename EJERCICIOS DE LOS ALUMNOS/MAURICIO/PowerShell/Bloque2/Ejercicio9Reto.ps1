New-Item -path C:\Informe_Procesos -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")
New-Item -path C:\Informe_Servicios -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")
New-Item -path C:\Backup1 -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")

New-Item -path C:\Informe_Procesos\informeprocesos.txt -ItemType File || Write-Host ("File / Archivo ya existe")
New-Item -path C:\Informe_Servicios\informeservicios.txt -ItemType File || Write-Host ("File / Archivo ya existe")



