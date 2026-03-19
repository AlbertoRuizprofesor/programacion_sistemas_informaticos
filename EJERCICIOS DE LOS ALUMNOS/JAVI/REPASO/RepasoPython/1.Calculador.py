producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
iva = subtotal * 0.21
total = subtotal + iva

print(f"Producto: {producto}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Total: {total:.2f} €")
