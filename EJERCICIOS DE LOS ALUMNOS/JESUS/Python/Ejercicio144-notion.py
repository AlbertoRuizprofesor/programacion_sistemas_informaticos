#Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def cant_mayores18(edad1,* edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant


#bloque principal

print("el numero de personas mayores de 18 son: ", cant_mayores18(38,16,17,95,57))

