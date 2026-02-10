
#Tiene que pedirme por consola un importe y me tiene que salir el importe, el iva 21% y el total con iva incluido.

importe = float(input("Ingrese el importe: "))
iva = importe * 0.21
total_con_iva = importe + iva

print(f"El importe es: {importe}")
print(f"El IVA (21%) es: {iva}")
print(f"El total con IVA incluido es: {total_con_iva}")

