#Ejercicio 119: Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces con string distintos.


def cadena_vocales(cadena):
    
    cant=0
    
    for i in range(len(cadena)):
        if cadena[i]=="a" or cadena[i]=="e" or cadena[i]=="i" or cadena[i]=="o" or cadena[i]=="u":
            cant=cant+1

    print("La cantidad de vocales de la palabra", cadena, "es", cant)

cadena_vocales("Hola") 
cadena_vocales ("bebe")
cadena_vocales("bombom")
        
        