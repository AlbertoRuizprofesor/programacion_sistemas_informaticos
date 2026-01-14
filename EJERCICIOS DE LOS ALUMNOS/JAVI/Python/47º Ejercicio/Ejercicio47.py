"""
Confeccionar una función que reciba tres enteros 
y nos muestre el mayor de ellos. 
La carga de los valores hacerlo por teclado.
"""

def num_mayor(num1, num2, num3):
    print("El valor mayor de los tres numeros es")
    if num1>num2 and num1>num3:
        print(num1)
    else:
        if num2>num3:
            print(num2)
        else:
            print(num3)

def cargar():
    num1=int(input("Ingrese el primer valor:"))
    num2=int(input("Ingrese el segundo valor:"))
    num3=int(input("Ingrese el tercer valor:"))
    num_mayor(num1,num2,num3)

cargar()


