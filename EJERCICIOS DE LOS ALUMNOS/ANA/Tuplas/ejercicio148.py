# Definir una tupla con tres valores enteros. 
# Convertir el contenido de la tupla a tipo lista. 
# Modificar la lista y luego convertir la lista en tupla.

#Definimos la tupla

fechatupla1 = (31,5,1989)
print("Imprimimos la primera tupla")
print(fechatupla1)

fechalista = list(fechatupla1) 
print("Imprimimos la lista que acabamos de crear con el contenido de la tupla anterior")
print(fechalista)

fechalista[0] = 1 
print("Imprimimos la lista ya modificada")
print(fechalista)

fechatupla2 = tuple(fechalista) 
print("Imprimimos la segunda tupla que acabamos de crear a partir del contenido de la lista anterior")
print(fechatupla2)