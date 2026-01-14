#Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
# Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. 
# Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro. 
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tabla_mul(numero, termino=10):
    for x in range(termino):
        valr=x*numero
        print(valr, ",",sep="", end="")
    print()


#bloque programa 

print("tabla del 3")
tabla_mul(3)                                #al no ponerle termino coge por defecto el 10 asignado 
print("Tabla del 3 con 5 terminos")         #se le indica 5 parametro termino 
tabla_mul(3,5)
print("Tabla del 3 con 20 terminos")
tabla_mul(termino=20,numero=3)              #se puede alterar las asignaciones si antes le hacemos referencia a cual dato queremos cambiar