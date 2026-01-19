print("Ejercicio 144")
print("")
print("")

# Confeccionar una función que reciba una serie de edades 
# y me retorne la cantidad que son mayores o iguales a 18
# (como mínimo se envía un entero a la función)

def listaedades(edad1,*edades):
    cant=0
    if edad1 >=18:
        cant+=1
    for x in range(len(edades)):
        if edades[x]>= 18:
            cant+=1
    return cant

mayoresedad=listaedades(18,15,45,65,12,16,1)
print("El número de personas mayores de 18 es: ",mayoresedad)

print("Fin de programa")



