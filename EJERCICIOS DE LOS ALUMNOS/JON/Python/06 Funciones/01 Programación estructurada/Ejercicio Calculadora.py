print("Ejercicio Calculadora")
print("")
print("")

n1=float(input("Ingrese el primer numero: "))
n2=float(input("Ingrese el segundo numero: "))  

def sumar(n1,n2):
    resultado=n1+n2
    print("La suma es: ", resultado)

def restar(n1,n2):
    resultado=n1-n2
    print("La resta es: ", resultado)

def multiplicar(n1,n2):
    resultado=n1*n2
    print("La multiplicacion es: ", resultado)

def dividir(n1,n2):
    if n2!=0:
        resultado=n1/n2
        print("La division es: ", resultado)
    else:
        print("Error: No se puede dividir por cero")

sumar(n1,n2)
restar(n1,n2)   
multiplicar(n1,n2)
dividir(n1,n2)

print("Fin del programa")
