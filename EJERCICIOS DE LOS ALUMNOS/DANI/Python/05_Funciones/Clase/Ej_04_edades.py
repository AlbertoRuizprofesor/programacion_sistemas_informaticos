# Crear un programa que me pida en una lista 5 edades, me haga la media de edad en una función y me diga el número de personas mayores de edad y menores de edad en otra función.

# ---------FUNCIONES---------
def media(lista):
    med = 0
    suma = 0
    for list in lista:
        suma += list
    med = suma / 5
    return med

def mayor_edad(lista):
    mayor = 0
    menor = 0
    for list in lista:
        if list >= 18:
            mayor += 1
        else:
            menor += 1
    print (f"Hay {mayor} que son mayores de edad y {menor} menores.")

# ---------PROGRAMA PRINCIPAL---------
edades = []
for x in range (5):
    edad = int(input(f"Dame la edad de la persona número {x+1}: "))
    edades.append(edad)

print(f"\nEdades: {edades}")
print(f"Media: {media(edades)}")
mayor_edad(edades)
