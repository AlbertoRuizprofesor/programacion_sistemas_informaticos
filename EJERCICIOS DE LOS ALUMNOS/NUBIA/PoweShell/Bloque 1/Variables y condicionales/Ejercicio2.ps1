$nombre = Read-Host "¿Cómo te llamas?"
[double] $notas = Read-Host "¿Qué notas tienes?"

if ($notas -le 4.5) {
    Write-Host "$nombre, estás suspenso"
}

else {
    "$nombre, estás aprobado"
}


