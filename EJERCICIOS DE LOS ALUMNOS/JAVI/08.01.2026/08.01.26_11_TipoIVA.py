# Pedir datos al usuario
producto = input("Introduce el producto sin acentos: ")
importe = float(input("Introduce el importe: "))

# Determinar el IVA según el producto
if producto.lower() == "bebida" or producto.lower() == "alimentacion":
    iva = 0.07
elif producto.lower() == "informatica" or producto.lower() == "electrodomestico":
    iva = 0.21
elif producto.lower() in ["curso de informatica", "curso de cocina", "curso"]:
    iva = 0.0
else:
    iva = 0.0
    print("Producto no reconocido, IVA 0% aplicado")

# Calcular IVA y total
importe_iva = importe * iva
total = importe + importe_iva

# Mostrar resultados
print()
print(f"Su producto es de {producto}")
print(f"Su importe es de {importe}€")
print(f"El IVA es {int(iva * 100)}%: {importe_iva}€")
print(f"El total es: {total}€")
