camisas=(int(input("dime cuantas camisas: ")))
unidades=(int(input("dime importe unidad: ")))

albaran=camisas * unidades

base=albaran
print("base: ", base)

descuento= base * 0.30
print("descuento 30%: ", descuento)
print("base Imponible: ", base-descuento)

baseImponible=base-descuento

iva=(baseImponible*21)/100
print("iva 21%: ", iva)

total=baseImponible + iva
print("total factura es: ", total)

tipoPago=input("tarjeta/efectivo")
if tipoPago=="tarjeta":
    total=total - (total*0.05)
    print("descuento tarjeta:", total*0.05)

entrega=(int(input("entrega: ")))
adevolver=entrega - total
print("devolvemos: ",adevolver)