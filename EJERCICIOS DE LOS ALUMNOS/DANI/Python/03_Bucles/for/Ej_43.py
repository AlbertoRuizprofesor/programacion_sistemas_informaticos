# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio. 
# Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.

suma = 0

for x in range(10):
    x = x + 1
    num = int(input(f"Ingrese el {x}º: "))
    suma = suma + num

print(f"La suma es: {suma}")

promedio = suma/10

print(f"El promedio es: {promedio}")

# Como vemos la variable x del for solo sirve para iterar(repetir) las diez veces el bloque contenido en el for.
# El resultado hubiese sido el mismo si llamamos a la funcion range con los valores: range(1,11)