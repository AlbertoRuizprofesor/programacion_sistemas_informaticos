#Ejercicio 122 notion Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
# En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
# Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def largo(cadena):#funcion con parametro que devuelve el numero de caracteres 
    return len(cadena)



#bloque del programa

nombre1=input("Pon tu nombre: ")
nombre2=input("Pon el nombre de tu compañero: ")
larg1=largo(nombre1)#invocacion de la funcion 
larg2=largo(nombre2)#invocacion de la funcion 

if larg1==larg2:
    print("los nombres tienen la misma cantidad de caracteres")
else:
    if larg1>larg2:
        print(nombre1,"es el mas caracteres tiene")
    else:
        print(nombre2, "es el que mas caracteres tiene")

