numeroCamisas = float(input("Introduce el número de camisas: "))
print("La unidad sale a 100€")
iva = float(input("El IVA es: "))
total = numeroCamisas * 100
totalImporte = total + ((total) * iva / 100)
print(f"El Total a pagar es: {totalImporte}")
