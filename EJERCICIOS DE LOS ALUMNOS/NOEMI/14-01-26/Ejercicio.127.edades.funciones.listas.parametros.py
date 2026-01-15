#Ejercicio 127 funciones y parametros: Crear un programa que me pida en una lista 5 edades, me haga la media de edad en una función y me diga el número de personas mayores de edad y menores de edad en otra función.

def cargar_valores():
    lista=[]
    for i in range(5):
        valor=int(input(f"Introduce {i+1} su edad: "))
        lista.append(valor)
    return lista

def media_edades(lista):
    return sum(lista)/len(lista)

def contar_mayores_menores(lista):
    mayores=0
    menores=0
    for edad in lista:
        if edad>=18:
            mayores +=1
        else:
            menores +=1
    return mayores, menores

edades=cargar_valores()

print("La lista de edades es: ", edades)

media=media_edades(edades)
mayores,menores=contar_mayores_menores(edades)


print("La media de edad es", media) 
print("Número de personas mayores de edad: ", mayores)
print("Número de personas menores de edad: ", menores)
        
  
                