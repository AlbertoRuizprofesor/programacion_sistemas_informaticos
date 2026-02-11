# Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar. 
def cargar_fecha():
    dd=int(input("Ingrese numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa) # --> Poner '()' para introducir en tupla

# La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.
def imprimir_fecha(tupla):
    print(tupla[0],tupla[1],tupla[2],sep="/")
                                    # sep= --> sirve para separar lo que hay en el interior del print

# ---------PROGRAMA PRINCIPAL---------
fecha=cargar_fecha()
imprimir_fecha(fecha)
