#Crear una lista de enteros por asignación
#Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
#Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

lista = [1,2,3,4,5,6,7,8,9,10]

def multiplicador_lista(lista_enteros, multiplicador):
    for numero in lista_enteros:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
entero = int(input("ingrese un numero entero para multiplicar la lista: "))

