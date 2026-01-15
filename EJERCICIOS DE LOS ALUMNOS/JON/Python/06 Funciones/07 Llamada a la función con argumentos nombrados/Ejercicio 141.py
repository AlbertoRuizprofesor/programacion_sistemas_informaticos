print("Ejercicio 141")
print("")
print("")

# Cargar una lista de 10 enteros,
# luego mostrarlos por pantalla a cada elemento separados por una coma.

def ingresar_numeros(cantidad=10):
    lista = []
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        lista.append(numero)
    return lista

def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i], end=", ")

lista=ingresar_numeros()
imprimir(lista)


print("Fin del programa")
