print("Ejercicio 132")
print("")
print("")


# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
# Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10.
# Desde el bloque principal del programa llamar a ambas funciones.

def cargar_lista():
    lista=[]
    for n in range(5):
        valor=int(input(f"Ingrese el valor entero {n+1}: "))
        lista.append(valor)
    return lista

def mostrar_mayores_10(lista):
    print("Valores mayores a 10:")
    for valor in lista:
        if valor > 10:
            print(valor)

lista = cargar_lista()
mostrar_mayores_10(lista)

print("Fin del programa")