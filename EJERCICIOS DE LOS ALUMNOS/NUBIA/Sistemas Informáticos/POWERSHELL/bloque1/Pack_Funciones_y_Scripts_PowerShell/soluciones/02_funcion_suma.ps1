# SOLUCIÓN 2: Función de suma
function Sumar {
    param([double]$A, [double]$B)
    return ($A + $B)
}
$a = [double](Read-Host "Primer número")
$b = [double](Read-Host "Segundo número")
$result = Sumar -A $a -B $b
Write-Host "Suma: $result"
