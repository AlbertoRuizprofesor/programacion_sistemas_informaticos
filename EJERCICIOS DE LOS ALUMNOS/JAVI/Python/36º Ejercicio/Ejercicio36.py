"""
Definir una lista que almacene por asignación los nombres de 5 personas.
Contar cuantos de esos nombres tienen 5 o más caracteres.
"""

lista = ["Antonio", "Ana", "Pedrito", "Jose", "Roberto"]

cantidad = 0
x = 0

while x < len(lista):
    if len(lista[x]) >= 5:
        cantidad = cantidad + 1
    x = x + 1



print("Esos nombres son: ")
print(cantidad)



