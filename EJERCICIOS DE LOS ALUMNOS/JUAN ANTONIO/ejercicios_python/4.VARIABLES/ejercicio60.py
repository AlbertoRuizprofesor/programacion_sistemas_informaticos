#Realizar la carga de enteros por teclado. 
# Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
#Mostrar la suma de los valores ingresados.

#Iniciación de variables
respuesta = "si"
suma = 0

#Mientras respuesta sea si, se sigue introduciendo números
#Cuando se introduce no, se deja de introducir números
#Se realiza la suma de todos los números
while respuesta == "si":
    numero = int(input("Introduzca un número: "))
    suma = suma + numero
    respuesta = input("¿Quiere cargar otro número? (si/no)")

#Se imprime el resultado de la suma de los números
print(f"La suma de los números que ha introducido es igual a {suma}")
