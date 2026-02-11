"""
Función carga fecha (día,mes,año) → tupla. Segunda función recibe tupla e imprime formateada.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_fecha():
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return (dia, mes, año)  # Tupla inmutable


def mostrar_fecha(fecha):
    print(f"Fecha: {fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}")  # Formato DD/MM/YYYY


#Main
fecha1 = cargar_fecha()
mensaje("Fecha cargada")
mostrar_fecha(fecha1)

fecha2 = (25, 12, 2026)
mensaje("Fecha fija")
mostrar_fecha(fecha2)

mensaje("Fin del programa")
