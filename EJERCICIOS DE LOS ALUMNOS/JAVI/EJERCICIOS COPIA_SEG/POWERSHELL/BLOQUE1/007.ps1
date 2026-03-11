
function Saludar{
    param($nombre)
    "Hola, $nombre"
}
$nombre = Read-Host "¿Cómo te llamas?"
Saludar -nombre $nombre
