print("Ejercicio calcular precio/descuento")
print("")
print("")

importe=int(input("Introduzca el importe del artículo: "))
cantidad=int(input("Introduzca la cantidad a comprar: "))
totalres=importe*cantidad
descuento=0
if totalres<=100:
	print("No tienes descuento.")
else:
	if 101<=totalres<=1000:
    	descuento=0.05
    if 1001>totalres<=2000:
    	descuento=0.10
    if totalres>2000:
        descuento=0.20

print("El importe total es: ",totalres)
print("Tu descuento es: ",totalres*descuento)
print("El total a pagar es:", totalres-(totalres*descuento))
