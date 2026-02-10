#Programa que calcula el precio total de una compra aplicando un descuento del 30%,
#añade el IVA correspondiente y muestra el importe final. Además, gestiona el tipo
#de pago (tarjeta o efectivo) y, en caso de pago en metálico, calcula el cambio a devolver.

#Pedimos al usuario el importe unitario del producto y lo convertimos a número decimal
importe = float(input("Ingrese el importe: "))

#Pedimos cuántas unidades quiere comprar y lo convertimos a número entero
unidades = int(input("Ingrese la cantidad de unidades: "))

#Pedimos el tipo de pago para decidir si habrá cambio o no
tipo_de_pago = input("Ingrese el tipo de pago (tarjeta/efectivo): ")

#Calculamos el total sin aplicar descuentos ni impuestos
totalUnidades = importe * unidades

#Calculamos el descuento del 30% sobre el total
descuento = totalUnidades * 0.30

#Restamos el descuento para obtener la base imponible
base_imponible = totalUnidades - descuento

#Calculamos el IVA (21%) sobre la base imponible
iva = base_imponible * 0.21

#Sumamos base imponible + IVA para obtener el total final
total = base_imponible + iva

#Mostramos los resultados al usuario
print("\n---Resultado---\n")
print("El importe es: ", importe, "€")
print("Las unidades son: ", unidades)
print("El total sin IVA es: ", totalUnidades, "€")
print("El descuento es (30%): ", descuento, "€")
print("Base imponible tras descuento: ", base_imponible, "€")
print("El IVA es: ", iva, "€")
print("El total con IVA es: ", total, "€")


# Comprobamos el tipo de pago
if tipo_de_pago == "tarjeta": 
    #Si paga con tarjeta, simplemente mostramos el total
    print("El tipo de pago es tarjeta.") 
    print("Total a pagar:", total) 
else: 
    #Si paga en efectivo, pedimos cuánto dinero entrega
    entrega = float(input("Ingrese entrega en metálico: ")) 

    #Calculamos el cambio a devolver
    total_devolver = entrega - total 

    #Imprime el tipo de pago y el cambio
    print("\nEl tipo de pago es efectivo.") 
    print("Cambio a devolver:", total_devolver)