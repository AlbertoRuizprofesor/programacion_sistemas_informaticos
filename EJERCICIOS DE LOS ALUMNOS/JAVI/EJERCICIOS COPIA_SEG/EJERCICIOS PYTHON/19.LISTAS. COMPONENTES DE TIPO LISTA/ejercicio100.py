#Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee. 
#Luego imprimir el último elemento de la lista principal.

# Definimos una lista que contiene tres sublistas.
# Cada sublista contiene nombres de personas.
lista = [["juan","ana"], ["luis"], ["pedro","carlos","maria"]]

# Accedemos a la última sublista usando:
# len(lista) - 1  →  devuelve el índice del último elemento.
# En este caso: len(lista) = 3, así que len(lista)-1 = 2
# Por lo tanto, lista[2] es ["pedro","carlos","maria"]
print(lista[len(lista)-1])
