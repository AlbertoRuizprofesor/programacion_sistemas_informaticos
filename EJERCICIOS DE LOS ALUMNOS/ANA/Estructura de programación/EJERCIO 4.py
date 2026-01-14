#Realizar la carga del precio de un producto y la cantidad a llevar. 
#Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)

precio= int(input("ingrese el precio del producto"))
cantidad= int(input("la cantidad a llevar"))

importe = precio * cantidad 

print("el importe a pagar es ", importe)