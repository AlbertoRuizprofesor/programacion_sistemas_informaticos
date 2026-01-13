# Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

# ---------FUNCION---------
def mayor(n1,n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return n1

# ---------Programa---------
num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame otro número: "))
print(f"El número mayor es: {mayor(num1,num2)}")
