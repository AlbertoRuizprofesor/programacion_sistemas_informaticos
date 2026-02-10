print("Ejercicio 143")
print("")
print("")

def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


print(f"La suma de 1+2 es {sumar(1,2)}")
print(f"La suma de 1+2+3+4 es {sumar(1,2,3,4)}")
print(f"La suma de 1+2+3+4+5+6+7+8+9+10 es {sumar(1,2,3,4,5,6,7,8,9,10)}")

print("Fin de programa")
