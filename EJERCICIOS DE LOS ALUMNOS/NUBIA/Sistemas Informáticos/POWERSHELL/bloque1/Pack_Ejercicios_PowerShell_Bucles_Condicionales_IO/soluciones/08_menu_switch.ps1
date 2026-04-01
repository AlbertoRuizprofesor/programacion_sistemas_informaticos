# SOLUCIÓN 8: Menú con switch
Write-Host "1) Saludar"; Write-Host "2) Mostrar fecha"; Write-Host "3) Salir"
$op = Read-Host "Elige una opción"
switch ($op) {
  "1" { $n = Read-Host "Tu nombre"; Write-Host "¡Hola, $n!" }
  "2" { Write-Host "Fecha/Hora: $(Get-Date)" }
  "3" { Write-Host "Adiós" }
  Default { Write-Host "Opción no válida" }
}
