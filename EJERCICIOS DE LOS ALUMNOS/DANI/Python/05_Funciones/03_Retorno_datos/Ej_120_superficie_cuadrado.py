# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.
# ---------FUNCIONES---------
def superficie(n):
    sup = n ** 2
    return sup

def menu():
    lado = int(input("¿Cuánto mide un lado? "))
    print(f"La superficie del cuadrado es {superficie(lado)}.")

# ---------PROGRAMA PRINCIPAL---------
menu()