#Funciones con def Ejercicio 112:

def presentación(): 
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("*******************************")

    
def carga_suma():
    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es: ", suma)
    
def finalizacion():
    print("**********************")
    print("Gracias por utilizar este programa.")
    
    
presentación()
carga_suma()
finalizacion()
