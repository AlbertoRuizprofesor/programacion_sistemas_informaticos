
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def cargar_datos():

    personas = {} 

    print("Introduzca los datos de 4 personas: ")
    for i in range(4):
        nombre = input(f"Nombre persona {i}: ")
        dni = int(input(f"DNI persona {i} sin letra: "))
        personas[dni] = nombre
    
    return personas

def imprimir_diccionario(diccionario):

    print("Listado completo del diccionario: ")

    for clave in diccionario:
        print(clave, diccionario[clave])


def consulta_persona(diccionario):

    dni = int(input("Introduzca el DNI de la persona a consultar sin letra: "))

    if dni in diccionario:
        print("El nombre asociado a ese DNI es: ", diccionario[dni])
    else:
        print("Esa persona no se encuentra en el diccionario")

# Programa

personas = cargar_datos()
imprimir_diccionario(personas)
consulta_persona(personas)

