#Programa que solicita el nombre de un producto, las unidades y el precio por unidad.
#Calcula el total sin IVA, aplica el IVA del 21% y muestra el importe final a pagar.

# Pedimos al usuario el nombre del producto
producto = input("Introduce el nombre del producto: ")

# Pedimos cuántas unidades quiere comprar y lo convertimos a entero
unidades = int(input("Introduce las unidades: "))

# Pedimos el precio por unidad y lo convertimos a número decimal
importe = float(input("Introduce el importe por unidad: "))

# Calculamos el total sin IVA (precio por unidad * unidades)
total_sin_iva = unidades * importe

# Calculamos el IVA (21%) sobre el total sin IVA
iva = total_sin_iva * 0.21

# Sumamos el IVA al total para obtener el precio final
total_con_iva = total_sin_iva + iva

# Mostramos todos los resultados al usuario
print("\nResultado\n")
print("Producto: ",producto)
print("Unidades:", unidades)
print("El importe por unidad es:", importe)
print("Total:", total_sin_iva)
print("El IVA es:", iva)
print("El total a pagar es:", total_con_iva)