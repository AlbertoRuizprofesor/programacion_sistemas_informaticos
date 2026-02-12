"""Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado."""
#Funciones
def mensaje(mensaje):
    print(f"\n=== === === {mensaje} === === ===")
def multiplicacion(lista, operador):
    mensaje("Resultado")
    for cnt in lista:
        resultado = cnt * operador
        print (f"{cnt} x {operador} = {resultado}")
def entradaDatos(numeroValores):
    for cntValores in range (numeroValores):
        listaValores.append(int(input(f"Introduce el valor {cntValores + 1}: ")))

#Main
listaValores = []
listaAsignacion = [3, 7, 8, 10, 2]
entradaDatos(1)
multiplicacion(listaAsignacion, listaValores[0])
mensaje("")
