"""
Crear un diccionario que permita almacenar 5 artículos,
utilizar como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")
def entradaDatos(numeroValores):
    diccionarioProductos = {}
    nombre = ""
    precio = 0.0
    for cntValores in range (numeroValores):
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input(f"Introduce el precio del producto {nombre}: "))
        diccionarioProductos[nombre] = precio
    return diccionarioProductos
def imprimirDicc(diccionario):
    for cnt in diccionario:
        print(f"Producto: {cnt}, Precio: {diccionario[cnt]}")
def printValor100(diccionario):
    for cnt in diccionario:
        if diccionario[cnt] > 100:
            print(f"Producto: {cnt}, Precio: {diccionario[cnt]}")

#Main
listaValores = entradaDatos(5)
mensaje("Productos/Valores")
imprimirDicc(listaValores)
mensaje("Precio mayor 100")
printValor100(listaValores)
mensaje("Fin del programa")
