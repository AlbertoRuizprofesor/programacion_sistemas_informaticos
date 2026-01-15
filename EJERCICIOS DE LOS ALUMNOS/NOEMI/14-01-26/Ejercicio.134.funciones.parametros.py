#Ejercicio 134: Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años) Imprimir la edad promedio de las personas.

def cargar_datos():
    nombres=[]
    edades=[]
    for i in range(5):
        listanombres=input(f"Introduce un {i+1} nombre: ")
        nombres.append(listanombres)
        listaedades=int(input(f"Introduce una {i+1} edad: "))
        edades.append(listaedades)
    return [nombres, edades]

def mayor_edad(nombres, edades):
    print("Nombres de personas mayores de edad")
    for i in range(len(nombres)):
        if edades[i]>=18:
            print(nombres[i])
  
def promedio(edades):
    suma=0
    for i in range(len(edades)):
        suma=suma+edades[i]
    promedio=suma//5
    print("El promedio de la edad de las personas:", promedio)
    
    
#Bloque principal:

nombres, edades=cargar_datos()

promedio(edades)
mayor_edad(nombres, edades)
promedio(edades)