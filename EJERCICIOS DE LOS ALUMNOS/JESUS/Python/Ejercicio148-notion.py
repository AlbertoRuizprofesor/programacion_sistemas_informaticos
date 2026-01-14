#Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. 
# Modificar la lista y luego convertir la lista en tupla.

fechatupla1=(14,1,2026)
print("Imprime la primera tupla")
print(fechatupla1)
fechalista=list(fechatupla1)
print("Imprimimos la lista que se copia de la tupla ")
print(fechalista)
fechalista[0]=15
print("Imprimimos la lista modificada")
print(fechalista)
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla copiada de lista")
print(fechatupla2)

