New-Item -Path C:\Reportes -ItemType Directory ||
Write-Host "El directorio ya existe"
New-Item -Path c:\Reportes\Resumen.txt -ItemType File ||
Write-Host "El archivo ya existe"  
