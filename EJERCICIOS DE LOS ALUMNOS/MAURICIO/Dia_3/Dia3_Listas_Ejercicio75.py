lista = []
for i in range(4):

    nombre = input("Nombre del operario: ")
    sueldo = float(input("Sueldo del operario: "))
    individuo = [nombre, sueldo]
    lista.append(individuo)

print(lista)
print(f"La lista anterior tiene un tamaño de {len(lista)}")
