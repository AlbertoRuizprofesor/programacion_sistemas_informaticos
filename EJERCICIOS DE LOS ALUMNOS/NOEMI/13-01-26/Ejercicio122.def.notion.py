#Ejercicio 122: Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def  largo(cadena):  #La funcion es  "largo" y el parametro es "cadena".
    return len(cadena)


n1=input("Ingrese el primer nombre: ")
n2=input("Ingrese el segundo nombre: ")
l1=largo(n1)
l2=largo(n2)
if l1==l2:
    print("Los nombres:", n1, n2, "tienen la misma cantidad de caracteres") 
else:
    if l1>l2:
        print(n1,"Es mas largo") 
    else:
        print(n2,"Es mas largo")
        
