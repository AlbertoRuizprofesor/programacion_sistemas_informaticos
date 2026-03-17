function Saludar {
    param ($n,$e)
 "Hola, $n, tienes $e años"
}

$nombre = Read-Host("Dime tu Nombre: ")
$edad = Read-Host ("edad: ")
Saludar -n $nombre -e $edad