# Ejercicio 3. Tabla de multiplicar interactiva
numero = int(input("Introduce un número entero: "))

print(f"\nTabla de multiplicar del {numero}\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
