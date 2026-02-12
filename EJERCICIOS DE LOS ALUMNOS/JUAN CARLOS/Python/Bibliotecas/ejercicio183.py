"""
Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.
Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la biblioteca estándar de Python.
"""
#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")
def entradaDatos(numeroValores):
    for cntValores in range (numeroValores):
        #Objeto de salida
        listaValores = []
        listaValores.append(float(input(f"Introduce el valor {cntValores + 1}: ")))
        return listaValores
#Biblioteca
from math import sqrt, pow
#Main
#Variables
listaValores = entradaDatos(1)
cuadradoValor = sqrt(listaValores[0])
potenciaValor = pow(listaValores[0], 3)
#Logica
#Impresión
print(f"Para el número {listaValores[0]}, su raiz cuadrada es: {cuadradoValor:.2f} y su potencia es: {potenciaValor}")
