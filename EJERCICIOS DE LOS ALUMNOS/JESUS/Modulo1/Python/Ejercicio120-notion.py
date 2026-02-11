#Ejercicio 120 notion 
# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def retor_super(lado): #funcion con retorno del producto
    superf=lado*lado
    return superf 

valor=int(input("Ingresa el valor de un lado del cuadrado: "))
superficie=retor_super(valor) #variable que invoca a la funcion 
print("la superficie del cuadrado es ", superficie)

