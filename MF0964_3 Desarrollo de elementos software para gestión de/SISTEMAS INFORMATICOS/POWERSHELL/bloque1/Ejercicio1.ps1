$nombre = Read-Host "¿Cómo te llamas?"
[int] $edad   = Read-Host "¿Cuántos años tienes?"
if ($edad -ge 18) {
    "$nombre es mayor de edad"
} else {
    "$nombre es menor de edad"
}





