$n=Read-Host("dime el numero:")
$numeros = 1..10
foreach ($n in $numeros) {
    $resultado=$n*$tabla
    writre-host "Numero: $n x $tabla = $resultado"
}