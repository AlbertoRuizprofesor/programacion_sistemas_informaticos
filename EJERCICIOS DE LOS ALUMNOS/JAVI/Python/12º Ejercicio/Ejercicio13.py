"""
Realizar la carga de enteros por teclado. 
Preguntar después que ingresa el valor si desea cargar otro valor debiendo el 
operador ingresar la cadena 'si' o 'no' por teclado.

Mostrar la suma de los valores ingresados.

"""

num1 = int (input("Introduce el número: "))

opcion = input("¿Desea introducir otro número? (Sí/No): ")

if opcion == "No":
    print("El valor es: " , num1)

else:
 
    num2 = int (input("Introduce otro número: "))

    print("La suma de los números es: " , (num1 + num2))


