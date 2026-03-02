$nombre = Read-Host "¿Cómo te llamas?"
$edad = Read-Host "¿Cuántos años tienes?"
Write-Host "Bienvenido $nombre"
Write-Host "Tienes $edad años"


if($edad -ge 18){
    "$nombre es mayor de edad"
}else{
    "$nombre es menor de edad"
}

