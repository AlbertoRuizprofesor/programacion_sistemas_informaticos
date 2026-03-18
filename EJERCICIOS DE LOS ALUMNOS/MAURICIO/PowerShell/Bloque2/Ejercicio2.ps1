New-Item -path C:\Backup -ItemType Directory || Write-Host ("Directory / Carpeta Ya existe")
Copy-Item -Path "C:\Reportes\*" -Destination "C:\Backup" -Recurse -Verbose