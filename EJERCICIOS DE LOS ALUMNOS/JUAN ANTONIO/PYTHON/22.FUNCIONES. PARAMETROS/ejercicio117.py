#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
# La carga de los valores hacerlo por teclado.


#Función para calcular el número que es mayor
def calcular_mayor(v1, v2, v3):
    print("El mayor de los números ingresado es: ")
    if v1 > v2 and v1>v3:
        print(v1)
    else:
        if v2 > v3:
            print(v2)
        else:
            print(v3)

#Función para ingresar los valores e instanciar la función calcular_mayor
def ingresar_valores():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    calcular_mayor(valor1, valor2, valor3)

ingresar_valores()
