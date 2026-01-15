"""
En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y valor.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def mostrarDiccionario(paises):
    for clave in paises:
        print(f"{clave}, {paises[clave]}")


#Main
dicPaises = {
    "China": 1444216107,
    "India": 1428627668,
    "USA": 345123456,
    "Indonesia": 279118651,
    "Pakistan": 247153970
}
mensaje("Diccionario países")
mostrarDiccionario(dicPaises)
mensaje("Fin del programa")
