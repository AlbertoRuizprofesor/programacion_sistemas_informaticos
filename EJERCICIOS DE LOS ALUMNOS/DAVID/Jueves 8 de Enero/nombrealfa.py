# Pedimos los dos nombres
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

print("-" * 30)
print("Nombres ordenados alfabéticamente:")

# Comparamos para decidir el orden de impresión
if nombre1.lower() < nombre2.lower():
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)

print("-" * 30)