importe=int(input("Ingrese su importe: "))
unidades=int(input("Ingrese la cantidad de unidades: "))
total=importe*unidades
descuento=0

if total<100:
    print("El total a pagar es: ",total)
else:
    if total>=100 and total<=1000:
        descuento=0.05
    if total>1000 and total<=2000:
        descuento=0.1
    if total>2000:
        descuento=0.20

print("El total a pagar es: ",total-(total*descuento))