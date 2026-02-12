# Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar. 
# La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.

def fecha():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    return dia, mes, año

def mostrar_fecha():
    print(f"La fecha es: {tupla[0]}/{tupla[1]}/{tupla[2]}")
    

tupla = (fecha())
mostrar_fecha()