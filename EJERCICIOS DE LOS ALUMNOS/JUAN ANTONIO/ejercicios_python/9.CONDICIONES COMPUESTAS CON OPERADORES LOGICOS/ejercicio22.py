#Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, 
#imprimir en pantalla la leyenda "Todos los números son menores a diez".

#Ingreso de los números por el usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Comprobamos si los tres números son menores que 10 
# # Para que esta condición sea verdadera, TODAS deben cumplirse
if numero1 < 10 and numero2 < 10 and numero3 < 10:
    print(f"Todos los números introducidos son menores de 10. Los números son {numero1}, {numero2}, {numero3}")
