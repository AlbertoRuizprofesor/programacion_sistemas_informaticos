#Desarrollar un programa que permita ingresar el lado de un cuadrado. 
# Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.


#Función para calcular el perímetro
def calcular_perimetro(lado):
    perimetro = lado * 4
    print (f"El Perímetro es {perimetro}")

#Función para calcular la superficie
def calcular_superficie(lado):
    superficie = lado * lado
    print(f"La superficie es {superficie}")

#Función para ingresar datos, comprobar la respuesta
#Invocar las funciones según la respuesta 
def datos():
    lado = int(input("Ingrese el valor de lado del cuadrado: "))
    respuesta = input("Calcule el perímetro o la superficie. Ingrese: perimetro/superficie: ")
    if respuesta == "perimetro":
        calcular_perimetro(lado)
    if respuesta == "superficie":
        calcular_superficie


datos()

