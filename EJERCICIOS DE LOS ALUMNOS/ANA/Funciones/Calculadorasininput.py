#calculadora con funciones sin input

numero1=float(input("Introduce el primer número: "))
numero2=float(input("Introduce el segundo número: "))

def sumar(numero1,numero2):
    resultado=numero1+numero2
    print(f"El resultado de la suma es: {resultado}")
    
def sumar2(numero1,numero2):
   resultado=numero1+numero2
   return resultado

sumar(numero1,numero2)
resultado_suma=sumar2(numero1,numero2)
print(f"la suma es: {resultado_suma}")
    
numero1=float(input ("introduce el primer número: el numero es 5"))
numero2=float(input ("introduce el segundo número: el número es 7"))

def sumar(umero1,numero2):
    resultado=numero1+numero2
    return resultado

