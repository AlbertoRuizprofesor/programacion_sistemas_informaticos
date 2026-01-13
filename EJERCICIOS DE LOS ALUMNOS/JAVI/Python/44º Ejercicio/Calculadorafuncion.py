num1=float(input("Introduce el número:"))
num2=float(input("Introduce el número:"))

def sumar (num1, num2):
    resultado = num1 + num2
    return resultado

def restar (num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar (num1, num2):
    resultado = num1 * num2
    return resultado

def dividir (num1, num2):
    resultado = num1 / num2
    return resultado

resultado_suma = sumar(num1, num2)
print("La suma es: " , resultado_suma)

resultado_resta = restar(num1, num2)
print("La resta es: " , resultado_resta)

resultado_multi = multiplicar(num1, num2)
print("La multiplicacion es: " , resultado_multi)

resultado_div = dividir(num1, num2)
print("La division es: " , resultado_div)





