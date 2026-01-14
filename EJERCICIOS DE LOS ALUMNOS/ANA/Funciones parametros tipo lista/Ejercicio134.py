#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
#Imprimir la edad promedio de las personas.

def carga_de_datos():
    nombres=[]
    edades=[]

    for x in range (5):
        nombre =  input("ingresa el nombre de la persona")
        edad = int(input("ingrese la edad"))

        nombres.append(nombre)
        edades.append(edad)
    return [nombres, edades]

def mayores_de_edad(nombres, edades):
    print("personas mayores de edad")
    for i in range(len(edades)):
        if edades[i] >=18:
            print(f"{nombres[i]} es mayor de edad")

def promedio_de_edades(edad):
    suma_de_edades = 0
    suma_edades = 0
    for e in edad:
        suma_edades += e
        promedio = suma_edades / len(edad)
    
    print("el promedio de edad es, " , promedio)

#final del programa
nombres, edades = carga_de_datos()
mayores_de_edad(nombres, edades)
promedio_de_edades(edades)
