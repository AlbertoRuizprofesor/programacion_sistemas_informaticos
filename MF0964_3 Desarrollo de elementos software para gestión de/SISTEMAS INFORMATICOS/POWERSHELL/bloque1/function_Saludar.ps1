function Saludar {
  param($nombre,$edad)
  "Hola, $nombre, tienes $edad años"
}
$nombre = Read-Host "¿Cómo te llamas?"
$edad = Read-Host "¿Cuántos años tienes?"

Saludar -nombre $nombre -edad $edad


