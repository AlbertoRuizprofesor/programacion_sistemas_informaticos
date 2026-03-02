$nota = Read-Host "Introduce la nota"
$asignatura = Read-Host "Introduce la asignatura"

Write-Host "La nota introducida es $nota"
Write-Host "La asignatura es $asignatura"


if($nota -lt 5){
    "está suspenso"
}else{
    "está aprobado"
}