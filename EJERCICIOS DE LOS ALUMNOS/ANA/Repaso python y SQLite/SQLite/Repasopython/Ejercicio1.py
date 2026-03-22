#Pide por teclado el nombre de un producto, su precio unitario y la cantidad comprada. 
#Calcula el subtotal, el IVA (21 %) y el total final. Muestra un resumen bien formateado.

producto = input ("producto: ")
precio = float (input ("precio unitario: "))
cantidad = int (input ("cantidad: "))

subtotal = precio * cantidad
IVA = subtotal * 0.21
total = subtotal + IVA

print (f"producto: {producto}")
print (f"subtotal: {subtotal:2f} €")
print(f"IVA: {IVA:2f} €")
print(f"total: {total:2f} €")