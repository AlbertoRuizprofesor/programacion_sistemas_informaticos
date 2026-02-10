
#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
#Mostrar el nombre de persona menor en orden alfabético.




listaNombres = []                         #Creamos una lista vacía donde guardaremos los nombres

for x in range(5):                   #Repetimos 5 veces (índices 0 a 4)
    nombre = input("Ingrese nombre de persona: ")  # Pedimos un nombre al usuario
    listaNombres.append(nombre)              #Añadimos el nombre a la lista

nombreMenor = listaNombres[0]             #Suponemos que el primer nombre es el "menor" alfabéticamente

for x in range(1, 5):                #Recorremos la lista desde el segundo nombre hasta el último
    if listaNombres[x] < nombreMenor:     #Comparamos alfabéticamente: 'Ana' < 'Carlos', por ejemplo
        nombreMenor = listaNombres[x]     #Si encontramos uno "menor", lo actualizamos

print("La lista completa de nombres ingresados es:")
print(listaNombres)                       #Mostramos la lista completa

print("El nombre menor en orden alfabético es:")
print(nombreMenor)                   #Mostramos el nombre que quedó como el menor
