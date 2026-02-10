#Ejercicio 118: Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.


def mostrar_perimetro(lado):
    per=lado*4
    print("EL perimetro es", per)
    
def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es", sup)
    
def cargar_valor():
    valor=int(input("Ingrese el valor del lado del cuadrado: "))
    respuesta=input("Quiere calcular el perimetro o la superficie [perimetro/superficie/ambos] ?")
    if respuesta=="perimetro":
        mostrar_perimetro(valor)
    if respuesta=="superficie":
        mostrar_superficie(valor)
    if respuesta=="ambos":
        mostrar_perimetro(valor)
        mostrar_superficie(valor)        
        
        
cargar_valor()