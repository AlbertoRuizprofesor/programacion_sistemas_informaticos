# Inicializa la variable $i con el valor 1. 
# Esta variable actuará como contador del bucle.
$i = 1

# Inicia un bucle while que se ejecutará mientras la condición sea verdadera. 
# En este caso, seguirá repitiéndose mientras $i sea menor o igual que 5.
while ($i -le 5){

    # Muestra en pantalla el valor actual del contador.
    Write-Host "Contador: $i"

    # Incrementa el valor de $i en 1 para evitar un bucle infinito.
    $i++
}