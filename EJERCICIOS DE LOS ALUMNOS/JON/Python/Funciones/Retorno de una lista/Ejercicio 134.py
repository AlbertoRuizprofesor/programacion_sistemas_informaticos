print("Ejercicio 134")
print("")
print("")

# Desarrollar un programa que permita cargar 5 nombres de personas
# y sus edades respectivas. 
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres 
# de las personas mayores de edad (mayores o iguales a 18 años)

def cargar_datos():
    lista = [[], []]
    for n in range(5):
        nombres = input(f"Ingrese el nombre de la persona {n+1}: ")
        edad = int(input(f"Ingrese la edad de {nombres}: "))
        nombres.append(nombres)
        edad.append(edad)
    return lista

def mostrar_mayores_edad(lista):
    print("Personas mayores de edad:")
    for n in range(len(lista[0])):
        if lista[1][n] >= 18:
            print(lista[0][n])

datos = cargar_datos()
mostrar_mayores_edad(datos)

print("Fin del programa")


    
   