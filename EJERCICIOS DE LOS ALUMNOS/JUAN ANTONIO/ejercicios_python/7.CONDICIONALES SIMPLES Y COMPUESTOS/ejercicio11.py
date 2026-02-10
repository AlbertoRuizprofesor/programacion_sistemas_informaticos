#Realizar un programa que solicite la carga por teclado de dos números, 
# si el primero es mayor al segundo informar su suma y diferencia, 
# en caso contrario informar el producto y la división del primero respecto al segundo.


#Solicitud de entrada de datos
num1 = int(input("Introduzca el primer número:"))
num2 = int(input("Introduzca el segundo número:"))

#Compara los números. 
# Si num1 es mayor que num2 da la suma y la resta
# En caso contrario da el producto y la división

if num1 > num2:
    suma = num1 + num2
    resta = num1 - num2
    print(f"La suma de {num1} + {num2} es igual a: {suma}")
    print(f"La resta de {num1} - {num2} es igual a: {resta}")
else:
    producto = num1 * num2
    division = num1 / num2
    print(f"El producto de {num1} x {num2} es igual a: {producto}")
    print(f"La división de {num1} : {num2} es igual a: {division}")