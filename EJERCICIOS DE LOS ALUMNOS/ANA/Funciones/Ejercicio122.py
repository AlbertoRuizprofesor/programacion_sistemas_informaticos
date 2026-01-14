#Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. 
#En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
#Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def largo(cadena):
    return len(cadena)

#pilar principal
nombre1=input("ingresa el primer nombre:")
nombre2=input("ingrese el segundo nombre:")
lar1=largo(nombre1)
lar2=largo(nombre2)
if lar1==lar2:
    print("los nombres:" , nombre1,nombre2, "tienen un igual de caracteres")
else: 
    if lar1>lar2:
        print(nombre1, "es mas largo")
    else:
        print(nombre2, "es mas largo")