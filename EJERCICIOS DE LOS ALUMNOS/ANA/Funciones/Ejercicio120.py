#Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado
# y nos retorne su superficie.

def retornar_superficie(lado):
    super=lado*lado
    return super

#pilar principal del programa

val=int(input("ingresa el valor del lado del cuadrado:"))
super= retornar_superficie(val)
print("la superficie del cuadrado es",super)