#Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, 
#imprimir en pantalla la leyenda "Alguno de los números es menor a diez".


# Pedimos al usuario que introduzca los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))


# Comprobamos si alguno de los tres números es menor que 10 
# # Con 'or', basta con que UNA sola condición sea verdadera
if numero1 < 10 or numero2 < 10 or numero3 < 10:
    print(f"Alguno o todos los números introducidos son menores de 10. Los números son {numero1}, {numero2}, {numero3}")
else:       # Si ninguna condición anterior se cumple, entonces todos son mayores o iguales a 10
    print(f"Los números introducidos son mayores de 10. Los números son {numero1}, {numero2}, {numero3}")