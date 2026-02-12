# Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
# En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def carga_enteros():
    entero1 = int(input("Ingrese el primer entero: "))
    entero2 = int(input("Ingrese el segundo entero: "))
    entero3 = int(input("Ingrese el tercer entero: "))
    return entero1, entero2, entero3

def ordenar_enteros(entero1, entero2, entero3):
    enteros_ordenados = sorted([entero1, entero2, entero3])
    print(f"Los enteros ordenados de menor a mayor son: {enteros_ordenados}")
    
entero1, entero2, entero3 = carga_enteros()
ordenar_enteros(entero1, entero2, entero3)