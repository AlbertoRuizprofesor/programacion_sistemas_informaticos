$nombre = Read-Host "¿Cómo te llamas?"
Write-Host "Bienvenido, $nombre"

$edad = Read-Host "¿Qué edad tienes?"
if ($edad -ge 18) {'Eres mayor de edad'} else {'Eres menor de edad'}

Write-Host "
INFORMACIÓN:
Nombre: $nombre
Edad: $edad"