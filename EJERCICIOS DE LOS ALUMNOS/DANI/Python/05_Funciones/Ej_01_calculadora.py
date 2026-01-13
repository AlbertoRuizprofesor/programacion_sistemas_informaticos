# Calculadora

#-------------FUNCIONES--------------
def suma(num1, num2):
    print(f"La suma es: {num1+num2}")

def resta(num1, num2):
    print(f"La resta es: {num1-num2}")

def multi(num1, num2):
    print(f"La multiplicación es: {num1*num2}")

def div(num1, num2):
    print(f"La división es: {num1/num2}")

def presentacion():
    print("\n***********************")
    print("Vamos al lio.")
    print("***********************")    

#--------------PROGRAMA PRINCIPAL--------------

# Usar función.
presentacion()

# Pedir al usuario que introduzca el valor de las variables
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Hacer un listado de opciones para decidir que hacer
print("\n-----OPCIONES-----\n1.Suma\n2.Resta\n3.Multiplicar\n4.Dividir")
opcion = int(input("Que quieres hacer? "))

# Ver si la opción es válida
if opcion >=1  and opcion <=4 :
    match opcion:
        case 1:
            # Llamar a la función
            suma(num1,num2)
        case 2:
            resta(num1,num2)
        case 3:
            multi(num1,num2)
        case 4:
            div(num1,num2)
else:
    print("Eres tonto? No hay esa opción.")

print("\n***********************")
print("Gracias por usarme.\n")