multiplo3=0
multiplo4=0

for i in range(10):
    valor=int(input("Ingrese el valor: "))
    if valor%3==0:
        multiplo3=multiplo3+1
    if valor%5==0:
        multiplo4=multiplo4+1
print("Cantidad de valores multiplos de 3:", multiplo3)
print("Cantidad de valores multiplos de 4:", multiplo4)