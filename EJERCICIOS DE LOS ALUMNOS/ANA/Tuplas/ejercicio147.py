# Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar. 
# La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.

def carga_fecha():
    
    dia = int(input("Introduzca el día: "))
    mes = int(input("Introduzca el mes: "))
    aa = int(input("Introduzca el año: "))
    
    return (dia,mes,aa) 

#Funcion que recibe una tupla con una fecha y la imprime por pantalla
def imprimir_tupla(fecha): 

    print(fecha[0],fecha[1],fecha[2], sep ="/") 
    
#Programa
fecha = carga_fecha()
imprimir_tupla(fecha)