print("Ejercicio 129")
print("")
print("")

# Crear una lista de enteros por asignación. 
# Definir una función que reciba una lista de enteros y un segundo parámetro 
# de tipo entero. Dentro de la función mostrar cada elemento de la lista 
# multiplicado por el valor entero enviado.

def multiplicar(lista, valor):
    for n in range(len(lista)):
        print(f"El elemento {lista[n]} multiplicado por {valor} es: {lista[n]*valor}")
    return

lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)

print("Fin del programa")



