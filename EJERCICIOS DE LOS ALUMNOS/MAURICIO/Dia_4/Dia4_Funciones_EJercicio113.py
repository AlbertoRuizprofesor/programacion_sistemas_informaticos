# Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.

# Repetir la carga e impresion de la suma 5 veces.

# Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

### **Programa: ejercicio113.py**


def cargaDatos():
    n1 = int(input("Ingrese un entero: "))
    n2 = int(input("ingrese otro entero: "))
    s = n1 + n2
    return s


def separador():
    print()
    print(":_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:")
    print()


for i in range(5):
    suma = cargaDatos()
    print(f"La suma de los enteros es: {suma}")
    separador()
