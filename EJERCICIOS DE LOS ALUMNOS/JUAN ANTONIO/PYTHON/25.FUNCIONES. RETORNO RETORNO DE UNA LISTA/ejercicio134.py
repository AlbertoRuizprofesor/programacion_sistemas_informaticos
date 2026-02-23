#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

#Imprimir la edad promedio de las personas.


# Función que carga los datos de 5 personas: sus nombres y edades
def cargar_datos():
    nom = []        # Lista donde guardaremos los nombres
    ed = []         # Lista donde guardaremos las edades

    for x in range(5):  # Repetimos 5 veces (una por cada persona)
        v1 = input("Ingrese el nombre de la persona: ") # Pedimos el nombre
        nom.append(v1)      # Lo añadimos a la lista de nombres
        v2 = int(input("Ingrese la edad: "))    # Pedimos la edad
        ed.append(v2)   # La añadimos a la lista de edades

    # Devolvemos ambas listas juntas dentro de otra lista
    return [nom, ed]

# Función que muestra los nombres de las personas mayores de edad
def mayores_edad(nom, ed):
    print("Nombres de personas mayores de edad")

    # Recorremos la lista usando los índices
    for x in range(len(nom)):
        if ed[x] >= 18:     # Si la edad correspondiente es mayor o igual a 18...
            print(nom[x])   # ...mostramos el nombre

# Función que calcula y muestra la edad promedio
def promedio_edades(ed):
    suma = 0        # Variable acumuladora para sumar todas las edades

    # Recorremos la lista de edades
    for x in range(len(ed)):
        suma = suma + ed[x]     # Vamos sumando cada edad
    promedio = suma // 5        # Dividimos entre 5 (número de personas)
                                # Se usa // para obtener un número entero

    print("Edad promedio de las personas: ", promedio)

#------bloque principal---------
# Llamamos a la función que carga los datos y recibimos dos listas: 
# 'nombres' contiene los nombres y 'edades' contiene las edades
nombres, edades = cargar_datos()

# Mostramos las personas mayores de edad
mayores_edad(nombres, edades)

# Calculamos y mostramos la edad promedio
promedio_edades(edades)
