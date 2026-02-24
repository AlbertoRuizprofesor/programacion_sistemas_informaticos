"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad 
(mayores o iguales a 18 años)
"""



# Creamos dos listas vacías: una para nombres y otra para edades
nombres = []
edades = []

# Bucle que se repite 5 veces para pedir datos de 5 personas
for x in range(5):
    nom = input("Ingrese el nombre de la persona:")  # Pedimos el nombre
    nombres.append(nom)  # Guardamos el nombre en la lista 'nombres'

    ed = int(input("Ingrese la edad de dicha persona:"))  # Pedimos la edad
    edades.append(ed)  # Guardamos la edad en la lista 'edades'

# Mostramos un título para la salida
print("Nombre de las personas mayores de edad:")

# Recorremos nuevamente las 5 posiciones
for x in range(5):
    if edades[x] >= 18:  # Comprobamos si la edad es mayor o igual a 18
        print(nombres[x])  # Si lo es, mostramos el nombre correspondiente
