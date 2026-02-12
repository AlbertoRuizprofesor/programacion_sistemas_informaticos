print("Ejercicio 147")
print("")
print("")

def cargar_fecha():
    dd=int(input("Ingrese el número de día: "))
    mm=int(input("Ingrese el número del mes: "))
    aa=int(input("Ingrese el número del año: "))
    return (dd,mm,aa)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2], sep="/")


fecha=cargar_fecha()
imprimir_fecha(fecha)

print("Fin del programa")

