#Por otro lado el programa principal que importa solo la función mayor es:


from Emayormenor import mayor #Importar el diccionario  y sus funciones con el mismo nombre que fueron creados.

valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese segundo valor: "))
print("El mayor de los dos valores es",mayor(valor1,valor2))
