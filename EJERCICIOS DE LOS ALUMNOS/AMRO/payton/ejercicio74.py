nombres=["Amro", "Jose", "Alfonso", "Rodrigo", "Paula"]
cantidad=0
x=0
while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1

print("Todos los nombres de la lista son:")
print(nombres)
print("La cantidad de nombres con 5 o más caracteres :")
print(cantidad)     
