$nombre = Read-Host "¿Cómo te llamas?"
$edad = Read-Host "¿Qué edad tienes?"

if ($edad -ge 18) {
    Write-Host "$nombre, eres mayor de edad"
}

else {
    "$nombre, eres menor de edad"
}


