# Inicializamos la variable suma en cero
suma_total = 0
continuar = "si"

# El bucle se ejecutará mientras la variable continuar sea "si"
while continuar.lower() == "si":
    # Pedimos el número entero
    numero = int(input("Ingresa un valor entero: "))
    
    # Sumamos el número al total acumulado
    suma_total = suma_total + numero
    
    # Preguntamos si quiere seguir
    continuar = input("¿Desea cargar otro valor? (si/no): ")

# Una vez que sale del bucle, mostramos el resultado
print("-" * 30)
print(f"La suma de los valores ingresados es: {suma_total}")
print("-" * 30)