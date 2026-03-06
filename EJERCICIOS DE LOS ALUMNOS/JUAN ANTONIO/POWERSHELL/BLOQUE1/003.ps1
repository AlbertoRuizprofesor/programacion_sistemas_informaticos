# Pide al usuario un número y lo guarda en la variable $tabla
# Read-Host siempre devuelve texto (string).
$tabla = Read-Host("dime el número: ")

# Crea un array con los números del 1 al 10 usando el operador de rango.
$numeros = 1..10

# Recorre cada número del array $numeros.
foreach ($n in $numeros){

    # Multiplica el número actual ($n) por el valor introducido ($tabla). 
    # PowerShell convierte automáticamente $tabla a número si es posible.
    $resultado = $n * $tabla

    # Muestra el resultado en pantalla con formato.
    Write-Host "Número: $n x $tabla = $resultado"
}