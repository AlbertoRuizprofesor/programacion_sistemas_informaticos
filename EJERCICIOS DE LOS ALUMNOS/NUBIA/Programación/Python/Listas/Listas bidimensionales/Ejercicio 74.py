# Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres=["Nubia", "Ana", "Noemi", "Darío", "Andrés"]
cantidad=0
x=0

while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1

print(f"Todos los nombres son: {nombres}")
print(f"Cantidad de nombres con 5 o más caracteres: {cantidad}")
