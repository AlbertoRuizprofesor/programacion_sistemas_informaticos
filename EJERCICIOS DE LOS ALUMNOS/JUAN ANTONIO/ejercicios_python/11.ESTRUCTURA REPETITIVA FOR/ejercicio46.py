#Codificar un programa que lea n números enteros y calcule 
#la cantidad de valores mayores o iguales a 1000 (n se carga por teclado)

# Inicializamos el contador para valores mayores o iguales a 1000
contador=0

# Pedimos cuántos valores se van a ingresar
n=int(input("Cuantos valores ingresará:"))

# Repetimos el ingreso de valores 'n' veces
for f in range(n):
    valor=int(input("Ingrese el valor:"))   # Pedimos un valor y lo convertimos a entero
    if valor>=1000:     # Si el valor es mayor o igual a 1000, aumentamos el contador
        contador=contador+1

# Mostramos cuántos valores cumplen la condición
print("La cantidad de valores ingresados mayores o iguales a 1000 son", contador)
