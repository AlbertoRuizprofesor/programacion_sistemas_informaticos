$asignatura = Read-Host "¿Que asignatura?"
[double]$nota   = Read-Host "¿Tu nota?"
if ($nota -le 4.5) {
    "$asignatura está suspenso"
} else {
    "$asignatura está aprobado"
}



