# Ejercicio 1. Calculadora de compra
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario (€): "))
cantidad = int(input("Cantidad comprada: "))

subtotal = precio * cantidad
iva = precio * 0.21
total = subtotal + iva

print("----- RESUMEN DE COMPRA -----")
print(f"Producto:        {producto}")
print(f"Precio unitario: {precio:.2f} €")
print(f"Cantidad:        {cantidad}")
print(f"Subtotal:        {subtotal:.2f} €")
print(f"IVA (21%):       {iva:.2f} €")
print(f"TOTAL A PAGAR:   {total:.2f} €")