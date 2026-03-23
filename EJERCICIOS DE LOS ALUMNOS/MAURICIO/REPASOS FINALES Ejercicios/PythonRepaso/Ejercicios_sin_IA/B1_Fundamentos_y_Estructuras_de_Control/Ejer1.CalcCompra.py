# Ejercicio 1. Calculadora de compra
# Pide por teclado el nombre de un producto,
# su precio unitario y la cantidad comprada.
# Calcula el subtotal, el IVA (21 %) y el total final.
# Muestra un resumen bien formateado.
# Idea clave: Haz una segunda versión que valide
# que el precio y la cantidad no sean negativos.


producto = input("Producto comprado: ")

# El while True junto con el break es el estándar en Python
# para mantener en el bucle al usuario hasta que dé una respuesta lógica.

while True:
    precio = float(input("Precio porunidad: "))
    if precio >= 0:
        break
    else:
        print("Error: el precio debe ser mayor o igual que cero")

while True:
    cantidad = int(input("Cuantos has comprado: "))
    if cantidad > 0:
        break
    else:
        print("Error: La cantidad debe ser mayor de 0")

# Operaciones
totalSinIva = precio * cantidad
iva = totalSinIva * 0.21
total = totalSinIva + iva

# Sacamos por Pantalla
print(f"Producto: {producto}")
print(f"Precio de todo sin IVA: {totalSinIva:.2f} €")
print(f"El IVA: {iva:.2f} €")
print(f"Total a pagar: {total:.2f} €")
