#Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y 
# a este resultado se lo multiplica por el tercero.

#Pedimos al usuario que ingrese los valores
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))

# Si son iguales, calculamos la suma del primero y segundo
if num1==num2 and num1==num3:
    suma=num1+num2
    print("La suma del primero y segundo:")
    print(suma)

    # Calculamos el producto de esa suma por el tercer número
    producto=suma*num3
    print("La suma del primero y segundo multiplicado por el tercero:")
    print(producto)