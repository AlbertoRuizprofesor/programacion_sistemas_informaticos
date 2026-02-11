print("Datos de la primer persona")
nombre1=input("Ingrese nombre: ")
altura1=float(input("Ingrese la altura: "))

print("\nDatos de la segunda persona")
nombre2=input("Ingrese nombre:")
altura2=float(input("Ingrese la altura:"))

print("\nLa persona mas alta es:")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)
