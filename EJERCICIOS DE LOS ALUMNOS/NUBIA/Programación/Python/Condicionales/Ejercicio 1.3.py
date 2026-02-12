#3º vamos a añadir un descuento o rebajas, del 30%, este descuento. Se ha de realizar sobre el total, no sobre el total a pagar.

descripción = input("Ingrese la descripción del producto: ")
importe = float(input("Ingrese el importe: "))
unidades = int(input("Ingrese la cantidad de unidades: "))
iva = importe * 0.21
total_importe = importe * unidades
total_con_iva = total_importe + iva
descuento = total_con_iva * 0.30
total_a_pagar = total_con_iva - descuento
tipo_de_pago = input("Ingrese el tipo de pago (efectivo/tarjeta): ")

print(descripción)
print(f"unidades: {unidades}")
print(f"El importe es: {importe}")
print(f"El total con IVA incluido es: {total_con_iva}") 
print(f"El IVA (21%) es: {iva}")
#Descuento del 30%
print(f"El descuento del 30% es: {descuento}")
print(f"El total a pagar es: {float(total_a_pagar)}")

if tipo_de_pago == "tarjeta":
    print("Pago realizado con tarjeta, no hay devolución.")
else:
    entrega = float(input("Ingrese el dinero entregado: "))
    a_devolver = entrega - total_a_pagar
    print(f"Dinero entregado es: {entrega}")
    print(f"Dinero a devolver es: {float(a_devolver):.2f}")