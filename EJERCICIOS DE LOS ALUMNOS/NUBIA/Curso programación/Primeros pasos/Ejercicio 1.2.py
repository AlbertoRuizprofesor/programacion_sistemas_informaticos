#Ahora vamos a hacer el siguiente cambio: añadimos las unidades y descrripción, ambos que me lo pids por consola.
descripción = input("Ingrese la descripción del producto: ")
importe = float(input("Ingrese el importe: "))
unidades = int(input("Ingrese la cantidad de unidades: "))
iva = importe * 0.21
total_importe = importe * unidades
total_con_iva = total_importe + iva

print(descripción)
print(f"unidades: {unidades}")
print(f"El importe es: {importe}")
print(f"El total con IVA incluido es: {total_con_iva}")
print(f"El IVA (21%) es: {iva}")