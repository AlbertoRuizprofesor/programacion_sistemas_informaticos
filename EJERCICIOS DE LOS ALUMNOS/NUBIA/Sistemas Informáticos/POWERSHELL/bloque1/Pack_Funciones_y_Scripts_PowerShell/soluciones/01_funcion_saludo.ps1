# SOLUCIÓN 1: Función de saludo
function Saludar {
    param([string]$Nombre)
    Write-Host "Hola, $Nombre"
}
$nombre = Read-Host "¿Cómo te llamas?"
Saludar -Nombre $nombre
