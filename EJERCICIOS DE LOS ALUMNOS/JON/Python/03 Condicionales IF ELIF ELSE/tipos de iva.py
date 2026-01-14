print("Ejercicio tipos de iva")
print("")
print("")

producto=input("Introduzca el producto: ")
importe=float(input("Introduzca el precio del producto: "))
print("")

if producto=="bebida" or producto=="alimentación":
    iva=0.07
if producto=="electrodoméstico" or producto=="informática":
    iva=0.21
if producto=="Curso de informática" or producto=="Curso de cocina":
    iva=0.0

print("Su producto es: ", producto)
print("El importe es: ", importe)
print("El IVA es", iva*100,"%: ", importe*iva)
print("El total es: ", importe+(importe*iva))