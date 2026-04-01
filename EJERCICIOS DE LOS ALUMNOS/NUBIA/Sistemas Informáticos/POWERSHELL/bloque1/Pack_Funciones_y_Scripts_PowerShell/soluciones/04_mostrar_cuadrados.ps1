# SOLUCIÓN 4: Función con bucle
function Mostrar-Cuadrados {
    param([int]$N)
    for ($i=1; $i -le $N; $i++) {
        Write-Host "$i x $i = $($i*$i)"
    }
}
$n = [int](Read-Host "Límite N")
Mostrar-Cuadrados -N $n
