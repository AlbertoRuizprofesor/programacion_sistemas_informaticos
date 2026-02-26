# SOLUCIÓN 3: Función con condicional
function Es-MayorEdad {
    param([int]$Edad)
    if ($Edad -ge 18) { return "Mayor de edad" } else { return "Menor de edad" }
}
$edad = [int](Read-Host "Introduce tu edad")
Write-Host (Es-MayorEdad -Edad $edad)
