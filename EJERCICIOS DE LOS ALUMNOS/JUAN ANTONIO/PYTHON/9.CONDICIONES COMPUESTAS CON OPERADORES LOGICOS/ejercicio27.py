#Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación 
#(debe mostrar el mayor y el menor de ellos)

#Ingreso de datos y almacenamiento en las variables
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))

#Imprime el texto Rango de valor
rango_valor = print("Rango de valor")

# --- PRIMERA PARTE: encontrar el número menor ---

# Si num1 es menor que num2 y menor que num3, entonces num1 es el menor
if num1<num2 and num1<num3:
    print(num1)
else:   # Si num1 no es el menor, comprobamos si num2 es menor que num3
    if num2<num3:
        print(num2)
    else:   # Si ninguna de las anteriores se cumple, num3 es el menor
        print(num3)

# --- SEGUNDA PARTE: encontrar el número mayor ---

# Si num1 es mayor que num2 y mayor que num3, entonces num1 es el mayor
if num1>num2 and num1>num3:
    print(num1)
else:   # Si num1 no es el mayor, comprobamos si num2 es mayor que num3
    if num2>num3:
        print(num2)
    else:   # Si ninguna de las anteriores se cumple, num3 es el mayor
        print(num3)