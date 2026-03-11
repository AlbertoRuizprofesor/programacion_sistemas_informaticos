#- Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.


#Función para saber la cantidad de vocales que tiene el texto
def numero_vocales(cadena):
    cant = 0
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u" or cadena[x]:
            cant = cant + 1
    print(f"Cantidad de vocales de la palabra, {cadena} es {cant}")


#Invocación de las funciones
numero_vocales("hola")
numero_vocales("administracion")
numero_vocales("correr")
