# Ejercicio 1.1 Valida que el precio y la cantidad no sean negativos
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario (€): "))
cantidad = int(input("Cantidad comprada: "))

if precio < 0:
    print("Error: el precio no puede ser negativo.")
else:
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
    else:
        subtotal = precio * cantidad
        iva = subtotal * 0.21
        total = subtotal + iva

        print("\n----- RESUMEN DE COMPRA -----")
        print(f"Producto:        {producto}")
        print(f"Precio unitario: {precio:.2f} €")
        print(f"Cantidad:        {cantidad}")
        print(f"Subtotal:        {subtotal:.2f} €")
        print(f"IVA (21%):       {iva:.2f} €")
        print(f"TOTAL A PAGAR:   {total:.2f} €")
