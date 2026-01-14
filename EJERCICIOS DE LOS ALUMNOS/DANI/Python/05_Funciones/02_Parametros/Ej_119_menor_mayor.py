# Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 

# ---------FUNCIONES---------
def orden(lista):
    lista.sort()
    print(lista)

# En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
def numeros():
    lista = []
    
    for x in range(3):
        numero = int(input(f"Dame el {x+1} número: "))
        lista.append(numero)
    
    orden(lista)

# ---------PROGRAMA PRINCIPAL---------
numeros()