importe = float(input("IMPORTE: "))
unidades = int(input("CANTIDAD: "))
total = importe * unidades
total_pagar = total

if total > 100 and total <= 1000:
    descuento = 5
    total_pagar = total * (1 - descuento / 100)
elif total > 1000 and total <= 2000:
    descuento = 10
    total_pagar = total * (1 - descuento / 100)
elif total > 2000:
    descuento = 20
    total_pagar = total * (1 - descuento / 100)
else:
    descuento = "No aplica"
    
print(f"\nIMPORTE: {importe}\nUnidades: {unidades}\nTotal: {total}\nDescuento: {descuento}\nTotal a pagar: {total_pagar}")