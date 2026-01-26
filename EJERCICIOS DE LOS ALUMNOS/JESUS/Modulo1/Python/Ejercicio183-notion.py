#Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.


from math import sqrt, pow #Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la biblioteca estándar de Python. Podemos consultar el módulo math [aquí](https://docs.python.org/3/library/math.html)


valor=int(input("Ingrese un valor entero: "))
r1=sqrt(valor)
r3=pow(valor,2)
r2=pow(valor,3)
print("La raiz cuadrada es",r1)
print("El cuadrado es",r3)
print("El cubo es",r2)
