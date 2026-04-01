$tabla = Read-Host("Dime el número")
$numeros = 1..10
foreach ($n in $numeros) {
    $resultado=$n*$tabla
    Write-Host "Número: $n x $tabla = $resultado"
}
