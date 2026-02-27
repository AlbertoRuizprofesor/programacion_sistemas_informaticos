# Crear Reportes\resumen.txt, copiar a Backup, mover a Final y eliminar Backup
New-Item -Path .\Reportes -ItemType Directory -Force | Out-Null
New-Item -Path .\Reportes\resumen.txt -ItemType File -Force | Out-Null
New-Item -Path .\Backup -ItemType Directory -Force | Out-Null
Copy-Item .\Reportes\resumen.txt .\Backup\
New-Item -Path .\Final -ItemType Directory -Force | Out-Null
Move-Item .\Backup\resumen.txt .\Final\resumen.txt -Force
Remove-Item .\Backup -Recurse -Force
