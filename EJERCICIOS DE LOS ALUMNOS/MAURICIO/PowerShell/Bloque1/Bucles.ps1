$tabla = Read-host("Dime un numero: ")
$numeros = 1..10

foreach ($n in $numeros) {
    $resultado = $n * $tabla
    
    "$tabla * $n = $resultado" 

}