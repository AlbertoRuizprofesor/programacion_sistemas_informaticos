# Inicializamos la variable $i con el valor 1
$i = 1

#Iniciamos un bucle do...while, que siempre se ejecuta al menos una vez
do{

    # Mostramos por pantalla el número de ejecución actual
    Write-Host "Ejecución número $i"

    # Incrementamos el valor de $i en 1
    $i++

# El bucle continuará mientras $i sea menor o igual que 5
}while ($i -le 5)