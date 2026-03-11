#Programa que solicita los datos de un producto (nombre, unidades y precio por unidad),
#calcula el total sin IVA, aplica un descuento del 30%, añade el IVA correspondiente
#y obtiene el total final. Además, pide el dinero entregado por el cliente y calcula
#el cambio a devolver.


#Pedimos al usuario el nombre del producto
producto = input("Introduce el nombre del producto: ")

#Pedimos cuántas unidades quiere comprar y lo convertimos a entero
unidades = int(input("Introduce las unidades: "))

#Pedimos el precio por unidad y lo convertimos a número decimal
importe = float(input("Introduce el importe por unidad: "))

#Calculamos el total sin aplicar IVA ni descuento
total_sin_iva = unidades * importe

#Calculamos el descuento del 30% sobre el total
descuento = total_sin_iva * 0.30

#Restamos el descuento para obtener el total con descuento aplicado
total_con_descuento = total_sin_iva - descuento

#Calculamos el IVA (21%) sobre el total con descuento
iva = total_con_descuento * 0.21

#Sumamos el IVA al total con descuento para obtener el precio final
total_con_iva = total_con_descuento + iva

#Pedimos cuánto dinero entrega el cliente para calcular el cambio
entregado = float(input("Introduce el dinero entregado por el cliente: "))
devolver = entregado - total_con_iva



#Mostramos todos los resultados al usuario
print("\nResultado\n")
print("Producto: ",producto)
print("Unidades:", unidades)
print("El importe por unidad es:", importe, "€")
print("Total:", total_sin_iva, "€")
print("Descuento (30%):", descuento, "€")
print("Total con descuento:", total_con_descuento, "€")
print("El IVA es:", iva, "€")
print("El total a pagar es:", total_con_iva, "€")
print("Dinero entregado:", entregado, "€")
print("Dinero a devolver:", devolver, "€")