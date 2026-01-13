"""
Confeccionar una función que le enviemos como parámetro
el valor del lado de un cuadrado y nos retorne su superficie.
"""

def superficie(lado):
    sup=lado * lado
    return sup

num = int(input("Dame el lado: "))
resultado = superficie(num)
print("La superficie del cuadro es: " , resultado)

