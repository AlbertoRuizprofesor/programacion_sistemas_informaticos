# Definir una lista que almacene por asignación los nombres de 5 personas. 
# Contar cuantos de esos nombres tienen 5 o más caracteres.

# Crear lista y variables
nombres=["juan", "ana", "marcos", "carlos", "luis"]
cantidad=0
x=0

# Bucle while para recorrer la lista
while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1

print(f"Todos los nombres son: {nombres}")
print(f"Cantidad de nombres con 5 o mas caracteres: {cantidad}")