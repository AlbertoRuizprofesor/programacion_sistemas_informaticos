# Hace ping a 8.8.8.8 y guarda el resultado en un archivo de texto
Test-Connection 8.8.8.8 -Count 4 | Out-File "$env:USERPROFILE\Desktop\ping.txt"