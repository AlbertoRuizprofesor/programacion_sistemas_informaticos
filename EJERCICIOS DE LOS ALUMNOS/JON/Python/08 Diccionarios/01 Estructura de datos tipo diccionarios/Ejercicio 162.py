print("Ejercicio 162")
print("")
print("")

def cargar():
    censo={}
    for i in range (4):
        nombre=input(f"Introduce el nombre completo de la persona {i+1}: ")
        dni=input(f"Introduce el número de DNI de la persona {i+1}: ")
        censo[dni]=nombre
    return censo

def imprimir(censo):
    for dni in censo:
        print(dni, censo[dni])

def consulta(censo):
    ni=input("Introduce el DNI a consultar: ")
    if ni in censo:
        print(f"El nombre completo es: {censo[ni]}")


listado=cargar()
imprimir(listado)
consulta(listado)
