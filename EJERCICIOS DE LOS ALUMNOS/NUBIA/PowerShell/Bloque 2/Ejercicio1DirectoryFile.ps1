New-Item -Path C:\reporte -ItemType Directory ||
Write-Host "El directorio ya existe"

New-Item -Path C:\reporte\prueba.txt -ItemType File ||
Write-Host "El archivo ya existe"