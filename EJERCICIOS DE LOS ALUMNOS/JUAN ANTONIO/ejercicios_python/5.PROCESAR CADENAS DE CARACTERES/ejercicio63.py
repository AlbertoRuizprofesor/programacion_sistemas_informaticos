#Solicitar la carga del nombre de una persona en minúsculas. 
# Mostrar un mensaje si comienza con vocal dicho nombre.


#Se introduce un nombre por consola
nombre = input("Introduzca un nombre en minúsculas: ")

#Se comprueba que la primera letra del nombre introducido sea vocal o no y se imprime el resultado
if nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "u":
    print(f"El nombre introducido comienza por vocal, míralo tu mismo: {nombre}")
else:
    print(f"El nombre introducido comienza por consonante, míralo tu mismo: {nombre}")