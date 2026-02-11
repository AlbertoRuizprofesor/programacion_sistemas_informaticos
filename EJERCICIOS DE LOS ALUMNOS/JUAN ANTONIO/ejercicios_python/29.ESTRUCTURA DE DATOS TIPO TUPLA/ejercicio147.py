"""
Desarrollar una función que solicite la carga del dia, mes y año y 
almacene dichos datos en una tupla que luego debe retornar. 
La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.
"""


# -----------------------------------------
# Función: ingresar_fecha
# Pide al usuario día, mes y año por separado.
# Devuelve una tupla con esos tres valores.
# -----------------------------------------

def ingresar_fecha():
    dia = int(input("Ingrese número de día: "))
    mes = int(input("Ingrese número de mes: "))
    anio = int(input("Ingrese número de año: "))
    return (dia, mes, anio)           # Se devuelve como tupla


# -----------------------------------------
# Función: mostrar_fecha
# Recibe una tupla con (día, mes, año)
# e imprime la fecha en formato dd/mm/aa.
# -----------------------------------------

def mostrar_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

fecha_ingresada = ingresar_fecha()    # Carga la fecha desde teclado
mostrar_fecha(fecha_ingresada)        # La muestra en formato dd/mm/aa
