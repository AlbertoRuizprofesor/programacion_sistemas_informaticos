#Programa que muestra edades
#Calcula la media
#Contar cuántos son mayores y cuántos son menores de edad

#Función que devuelve una lista de edades (se pueden cambiar los valores)
def cargar_edades():
    return[18,13, 24, 45, 67]

#Función que calcula la media de una lista de números
def calcular_media(lista):
    return sum(lista) / len(lista)

#Función que calcula la media de una lista de números
def contar_edades(lista):
    mayores = 0         #Contador de mayores de edad
    menores = 0         #Contador de menores de edad

    for edad in lista:      #Recorremos cadd edad de la lista
        if edad >= 18: 
            mayores +=1
        else:
            menores +=1
    return mayores, menores    #Devolvemos ambos valores 
#Función que muestra todos los resultados
def mostrar_resultados():
    edades = cargar_edades()    #Obtenemos la lista de edades
    media = calcular_media(edades)  #Calculamos la media
    mayores, menores = contar_edades(edades)    #Contamos mayores y menores

    print("Edades: ", edades)
    print(f"Media: {media:.2f}")
    print("El número de personas mayores de edad: ", mayores)
    print("El número de personas menores de edad: ", menores)

#Llamamos a la función principal
mostrar_resultados()


