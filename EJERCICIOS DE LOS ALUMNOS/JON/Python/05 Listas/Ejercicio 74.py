print("Problemas propuestos 3")
print("")
print("")

lista=["Ana", "Juan", "Pedro", "Lucia", "Maria"]
cantidad=0
x=0
print("Introduzca el nombre de 5 personas: ")
for x in range(len(lista)):
    if len(lista[x])>=5:
        cantidad=cantidad+1
    x=x+1

print("todos los nombres son: ",lista)
print("La cantidad de nombres con 5 o más letras es: ", cantidad)

print("Fin de programa!!!")
