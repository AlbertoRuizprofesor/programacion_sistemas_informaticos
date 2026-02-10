#crear una calculadora con funciones

def suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor1+valor2
    print("la suma de los dos valores es: ",suma)

def resta():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    resta=valor1-valor2
    print("la resta de los dos valores es: ",resta)

def multi():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    multi=valor1*valor2
    print("la multiplicacion de los dos valores es: ",multi)

def divi():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    divi=valor1/valor2
    print("la division de los dos valores es: ",divi)

valor1=float(input("Ingrese el primer valor: "))
valor2=float(input("Ingrese el segundo valor: "))

def calcu(valor1,valor2):
    
    suma=valor1+valor2
    resta=valor1-valor2
    multi=valor1*valor2
    divi=valor1/valor2
    print(f"La suma es {suma}, la resta es {resta}, la multiplicacion es {multi}, y la division es {divi}")

#suma()
#resta()
#multi()
#divi()

calcu(valor1,valor2)
