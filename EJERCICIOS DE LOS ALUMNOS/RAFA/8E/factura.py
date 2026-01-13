importe=(float(input(" dime un importe: ")))

baseImponible=importe
print("baseImponible: ", baseImponible)

iva=(baseImponible*21)/100
print("iva 21%: ", iva)

total=baseImponible + iva
print("total factura es: ", total)