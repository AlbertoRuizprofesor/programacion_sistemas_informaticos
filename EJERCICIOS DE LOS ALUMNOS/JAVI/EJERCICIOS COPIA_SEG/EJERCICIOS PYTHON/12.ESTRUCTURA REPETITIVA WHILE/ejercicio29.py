
"""
Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.

"""

numero = int(input("Ingrese un número: "))  #Pedimos al usuario un número y lo convierte a entero

x = 1   #Inicializamos el contador en 1, será el primer número que imprimamos

while x <= numero:  #Mientras x sea menro o igual que "numero", el bucle se seguirá ejecutando
    print(x, end= " ")  #Imprimimos el valor actual de x en la misma línea, separado por un espacio
    x = x + 1           #Incrementamos x en 1 para avanzar y evitar un bucle infinito


