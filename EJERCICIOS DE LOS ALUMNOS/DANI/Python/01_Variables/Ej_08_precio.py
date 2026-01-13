importe = float(input("Dame el importe: "))
descuento = float(input("Dame el descuento (%): ")) / 100

# Aplicar descuento
total_importe = importe * (1 - descuento)

# IVA
iva = 0.21
pago_total = total_importe * (1 + iva)

print(f"Total con descuento: {total_importe}")
print(f"Total a pagar con IVA: {pago_total}")