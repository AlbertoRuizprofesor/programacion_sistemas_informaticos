num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))


def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


print(f"La suma de {num1} + {num2} = {suma(num1,num2)}")
print(f"La resta de {num1} - {num2} = {resta(num1,num2)}")
print(f"La multilication de {num1} * {num2} = {mult(num1,num2)}")
print(f"La división de {num1} + {num2} = {div(num1,num2)}")
