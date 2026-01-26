#Ejercicio 121 notion Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def retor_mayor(val1,val2): #funcion con parametros y condicion 
    if val1>val2:
        mayor=val1
    else:
        mayor=val2
    return mayor


#bloque del programa 
num1=int(input("Ingrese el primer numero: ")) #peticion por consola 
num2=int(input("Ingrese el segundo numero: "))
print(f"El numero mayor es {retor_mayor(num1,num2)}") #comparacion entre ambos numeros con invocacion a la funcion 
