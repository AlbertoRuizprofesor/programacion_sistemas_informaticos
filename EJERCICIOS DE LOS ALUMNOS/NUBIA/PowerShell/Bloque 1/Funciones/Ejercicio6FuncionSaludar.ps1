function Saludar {
    param($nombre, $edad)
    "Hola, $nombre. Tienes $edad años" 
}

#Para pedir el valor de nombre y edad, hacemos:
$nombre=Read-Host "¿Cómo te llamas?"
$edad=Read-Host "¿Cuántos años tienes?"

Saludar -nombre $nombre -edad $edad 