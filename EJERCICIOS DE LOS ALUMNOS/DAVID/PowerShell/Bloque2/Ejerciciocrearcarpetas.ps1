New-Item -Path c:\informesprocesos -ItemType directory ||
Write-Host "El archivo ya existe"

New-Item -Path c:\informesprocesos\informesprocesos.txt -ItemType File ||
Write-Host "El archivo ya existe"

New-Item -Path c:\informeservicio\ -ItemType directory ||
Write-Host "El archivo ya existe"

New-Item -Path c:\informeservicio\informeservicio.txt -ItemType File ||
Write-Host "El archivo ya existe"


New-Item -Path c:\informesrvicio\ -ItemType directory ||
Write-Host "El archivo ya existe"

New-Item -Path c:\informesrvicio\backup.txt -ItemType File ||
Write-Host "El archivo ya existe"


Remove-Item C:\Backup-informesrvicio-backup.txt 




