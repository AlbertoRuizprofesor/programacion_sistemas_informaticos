# SOLUCIÓN 2: Mayor de edad
$nombre = Read-Host "Introduce tu nombre"
$edadStr = Read-Host "Introduce tu edad"
[int]$edad = $edadStr
if ($edad -ge 18) { Write-Host "$nombre, eres mayor de edad" } else { Write-Host "$nombre, eres menor de edad" }
