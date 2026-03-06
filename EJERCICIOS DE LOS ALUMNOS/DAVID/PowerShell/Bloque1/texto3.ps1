$asignatura = Read-Host "¿Que asignatura?"
[double]$nota = Read - Host "¿tu nota?"

if ($nota -le 4.5) {

    "$asignatura esta suspenso"
}else {
    "$asignatura está aprobado"
}
