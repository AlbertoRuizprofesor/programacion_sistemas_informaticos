# SOLUCIÓN 8: Script modular
function Leer-Numero { param([string]$Msg) return [double](Read-Host $Msg) }
function Es-Par { param([double]$N) return ($N % 2 -eq 0) }
function Mostrar-Resultado {
    param([double]$N, [bool]$EsPar)
    if ($EsPar) { Write-Host "$N es par" } else { Write-Host "$N es impar" }
}
$n = Leer-Numero -Msg "Introduce un número"
Mostrar-Resultado -N $n -EsPar (Es-Par -N $n)
