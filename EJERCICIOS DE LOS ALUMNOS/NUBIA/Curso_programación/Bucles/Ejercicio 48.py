# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

cantidad_numeros = int(input("Ingrese la cantidad de números a cargar (debe ser al menos 10): "))

while cantidad_numeros < 10:
    print("Debe ingresar al menos 10 números.")
    cantidad_numeros = int(input("Ingrese la cantidad de números a cargar (debe ser al menos 10): "))
    
suma_ultimos_cinco = 0

for x in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {x + 1}: "))
    if x >= cantidad_numeros - 5:
        suma_ultimos_cinco += numero

print(f"La suma de los últimos 5 números ingresados es: {suma_ultimos_cinco}")