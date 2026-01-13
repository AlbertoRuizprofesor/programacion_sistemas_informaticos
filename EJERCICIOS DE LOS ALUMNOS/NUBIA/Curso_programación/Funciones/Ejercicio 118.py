# Desarrollar un programa que permita ingresar el lado de un cuadrado. 
# Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Calcular perímetro o superficie?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)
        
def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es " ,per)

def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)

# programa principal
cargar_dato()