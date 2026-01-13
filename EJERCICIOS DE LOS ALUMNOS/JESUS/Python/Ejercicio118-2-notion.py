#- Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

#Ejercicio118.py

def cantidad_vocales(cadena): #definimos la funcion con el parametro cadena
    cant=0 #variable para ir sumando el numero de vocales
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u": #condicion con if 
            cant=cant+1 #suma si se cumple 
    print("Cantidad de vocales de la palabra",cadena,"es",cant)


# bloque principal
cantidad_vocales("hola")
cantidad_vocales("administracion")
cantidad_vocales("correr")



