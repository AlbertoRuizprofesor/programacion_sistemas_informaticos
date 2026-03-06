# SOLUCIÓN 6: Función con valor de retorno (factorial)
function Calcular-Factorial {
    param([int]$N)
    if ($N -lt 0) { throw "N debe ser >= 0" }
    $r = 1
    for ($i=1; $i -le $N; $i++) { $r *= $i }
    return $r
}
$n = [int](Read-Host "Introduce n (>=0)")
Write-Host "$n! = $(Calcular-Factorial -N $n)"
