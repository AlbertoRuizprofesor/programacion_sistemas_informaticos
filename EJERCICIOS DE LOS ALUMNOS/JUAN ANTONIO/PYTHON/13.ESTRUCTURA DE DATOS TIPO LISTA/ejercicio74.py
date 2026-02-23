#Definir una lista que almacene por asignación los nombres de 5 personas.
# Contar cuantos de esos nombres tienen 5 o más caracteres.

#Declaración de la lista nombres
nombres = ["Juan", "María", "Jesús", "Antonio", "Alberto"]

#Declaración e iniciación de variables
cantidad = 0
x = 0

#Calculo del número de nombres con más o mismo número de 5 carateres
while x < len(nombres):
    if len(nombres[x]) >= 5:
        cantidad = cantidad + 1
    x = x + 1

#Imprime el resultado en pantalla
print(f"Los nombres contenidos en la lista son {nombres}")
print(f"La cantidad de nombres con 5 caracteres o más son: {cantidad}")