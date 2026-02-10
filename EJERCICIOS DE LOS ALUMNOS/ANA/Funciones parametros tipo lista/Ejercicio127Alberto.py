
#Crear un programa que me pida en una lista 5 edades
#me haga la media de edad en una función
#me diga el número de personas mayores de edad y menores de edad
#en otra función.


def edades():
    edades = []
    for e in range (5):
       var=int(input("ingrese una edad: "))
       edades.append(var)
    return edades

def calcular_media(edades):
    return sum(edades)/len(edades)

def personas_menores_de_edad(edades):
    menores=0
    mayores=0
    for e in edades:
        if e>=18:
            mayores+=1
        else:
         menores +=1
    return menores, mayores 

 #final del programa

edades=edades()
print ("calcular_media: " ,calcular_media(edades))
print("personas_menores_de_edad" , personas_menores_de_edad(edades))



         

