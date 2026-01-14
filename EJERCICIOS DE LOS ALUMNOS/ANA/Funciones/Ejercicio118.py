#Desarrollar un programa que permita ingresar el lado de un cuadrado. 
#Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def muestra_perimetro(lado):
    per=lado*4
    print("El perimetro es" ,per)

def muestra_superficie(lado):
    sup=lado*lado 
    print("la superficie es" ,sup)

def cargar_datos():
    l=int(input("ingrese el valor del lado de un cuadrado:"))
    respuesta= input("quiero que se muestre el perimetro o la superficie [ingresar texto: perimetro/superficie]?")

    if respuesta=="perimetro":
        muestra_perimetro(l)
    if respuesta=="superficie":
        muestra_superficie(l)

#programa principal

cargar_datos()