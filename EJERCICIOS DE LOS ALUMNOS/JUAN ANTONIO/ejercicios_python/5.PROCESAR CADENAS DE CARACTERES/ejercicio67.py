#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. 
# Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

#Pide al usuario que escriba una oración y la guarda en la variable "oración"
oracion = input("Escriba una oración: ")

#Convierte toda la oración a minúsculas para que "A" y "a" cuenten igual
oracion_minuscula = oracion.lower()

#Contador que irá sumando cuántas vocales aparecen
vocales = 0

#Índice pra recorrer la oración letra por letra
x = 0

#Bucle que recorre toda la oración desde la posición 0 hasta el final
while x < len(oracion_minuscula):
    #Si la letra actual es una vocal, suma 1 al contador
    if oracion_minuscula[x] in "aeiou":
        vocales = vocales + 1
    #Avanza a la siguiente letra
    x = x + 1

#Muestra el total de vocales encontradas
print(f"La cantidad de vocales de la oración son: {vocales}")
