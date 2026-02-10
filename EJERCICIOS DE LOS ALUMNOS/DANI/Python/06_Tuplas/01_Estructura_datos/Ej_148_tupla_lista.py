# Definir una tupla con tres valores enteros. 
tupla = (1,2,3)

# Convertir el contenido de la tupla a tipo lista.
lista = []
for valor in tupla:
    lista.append(valor)

# Modificar la lista y luego convertir la lista en tupla.
modificador = 4
lista.append(modificador)

tupla = (lista[0],lista[1],lista[2],lista[3])

print(tupla)