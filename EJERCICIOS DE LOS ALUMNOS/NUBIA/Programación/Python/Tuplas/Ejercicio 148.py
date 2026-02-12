# Definir una tupla con tres valores enteros. 
# Convertir el contenido de la tupla a tipo lista. 
# Modificar la lista y luego convertir la lista en tupla.

tupla = (1, 2, 3) # Defino lista con 3 valores
lista = list(tupla) # Convierto tupla a lista

lista.append(4) # Agrego valor a la lista (la modifico)

tupla = tuple(lista) # La vuelvo a convertir en tupla

print(tupla) # Muestro en pantalla la tupla