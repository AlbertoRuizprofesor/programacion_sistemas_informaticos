"""
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro.
Definir un segundo parámetro llamado termino que por defecto almacene el valor 10.
Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def tablaMultiplicar(valor, termino=10):
    for cnt in range(1, termino + 1):
        print(f"{valor} x {cnt} = {valor * cnt}")


#Main
mensaje("Tabla del 5 (default 10)")
tablaMultiplicar(valor=5)
mensaje("Tabla del 3 hasta 7")
tablaMultiplicar(valor=3, termino=7)
mensaje("Fin del programa")
