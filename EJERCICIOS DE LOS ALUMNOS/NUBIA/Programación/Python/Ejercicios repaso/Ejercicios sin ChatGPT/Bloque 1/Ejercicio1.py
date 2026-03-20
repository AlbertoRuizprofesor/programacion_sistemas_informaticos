'''
Pide por teclado el nombre de un producto, su precio unitario y la cantidad comprada.
Calcula el subtotal, el IVA (21 %) y el total final. Muestra un resumen bien formateado.
'''

# Variables con input
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

# Cálculos
subtotal = cantidad*precio
precioIva = (subtotal*0.21) + subtotal

# Main programa

print(f"\nCALCULADORA COMPRA \nProducto: {producto} \nCantidad: {cantidad} \n\
Precio con IVA (21%): {precioIva:.2f} euros")
