#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a" ", en cambio una cadena vacía es ""


#Pide al ususario que introduzca una oración
oracion = input("Escriba una oración: ")

#Inicialización de las variables para almacenar los espacios y el contador del bucle while
cantidad_espacios = 0
x = 0

#Recorre la oración, busca los espacios en blanco y los suma y almacena
while x < len(oracion):
    if oracion[x] == " ":
        cantidad_espacios = cantidad_espacios +1
    x = x + 1

#Imprime la cantidad de espacios que hay en la frase
print(f"La cantidad de espacios de la oración es igual a : {cantidad_espacios}")
