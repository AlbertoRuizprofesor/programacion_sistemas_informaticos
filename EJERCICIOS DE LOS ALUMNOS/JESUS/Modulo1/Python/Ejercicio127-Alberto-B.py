#Crear un programa que me pida en una lista 5 edades, me haga la media de edad en una función 
# y me diga el número de personas mayores de edad y menores de edad en otra función.

# Resultado

# Edades: 18,13,24,45,67
# media: 
# El numero de personas mayores de edad: 4
# El numero de personas menores de edad: 1

def pedir_edad():               #creamos la funcio con varias listas que devuelva los tres valores con return
    años=[]
    mayores=[]
    menores=[]
    for i in range(5):
        año= int(input(f"Pon tu edad {i+1}: "))
        años.append(año)
        if años[i]>=18:
            mayores +=1
        else:
            menores +=1
        
    return años, mayores, menores  #return de las tres listas


def calc_media(años):
    return sum(años) / len(años)










