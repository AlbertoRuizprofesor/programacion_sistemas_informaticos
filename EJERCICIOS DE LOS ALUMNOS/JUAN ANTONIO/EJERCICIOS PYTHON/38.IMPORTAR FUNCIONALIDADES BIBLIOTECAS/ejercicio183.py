#Confeccionar un programa que solicite la carga de un valor entero por teclado
#  y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.


#Importamos funciones matemáticas: squrt para raíz cuadrada y pow par potencia
from math import sqrt, pow

#Pedimos al usuario un número entero y lo convertimos a int
valor = int(input("Ingrese un valor entero: "))

#Calculamos la raíz cuadrada del valor ingresado
r1 = sqrt(valor)

#Calculamos el cubo del valor (valor elevado a 3)
r2 = pow(valor,3)

#Mostramos los resultados
print("La raíz cuadrada es: ", r1)
print("El cubo es: ", r2)