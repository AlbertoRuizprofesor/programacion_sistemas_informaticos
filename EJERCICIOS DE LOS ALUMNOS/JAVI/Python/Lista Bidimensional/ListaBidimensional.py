"""
capitales=[["España", "Madrid"], ["Italia", "Roma"]]
print("posicion 0,0 ", capitales[0][0])  # Imprime "España"
print("posicion 0,1 ", capitales[0][1])  # Imprime "Madrid"
print("posicion 1,0 ", capitales[1][0])  # Imprime "Italia"
print("posicion 1,1 ", capitales[1][1])  # imprime "Roma"

#posicion Fila, columna

print("*******************")


for pais, capital in capitales:
    print(f"La capital de {pais} es {capital}.")
    print("-----")

"""



"""
Ejercicio: hacer el mismo pero con notas, ejemplo "Matematicas", 10, "Historia",9, "Lengua",5
cuando me muestre print posicion, al tener esta lista mas elementos quiero que salgan todos los elementos
de manera que se tiene que quedar en el print("posicion.. ", notaw[x][x][x])  # 
"""

""" # Lista bidimensional con asignaturas y notas
notas = [
    ["Matematicas", 10],
    ["Historia", 9],
    ["Lengua", 5]
]

# Acceso a posiciones concretas (fila, columna)
print("posicion 0,0 ", notas[0][0])  # Matematicas
print("posicion 0,1 ", notas[0][1])  # 10

print("posicion 1,0 ", notas[1][0])  # Historia
print("posicion 1,1 ", notas[1][1])  # 9

print("posicion 2,0 ", notas[2][0])  # Lengua
print("posicion 2,1 ", notas[2][1])  # 5

print("*******************")

# Recorrido de toda la lista (mostrar todos los elementos)
for asignatura, nota in notas:
    print(f"La nota de {asignatura} es {nota}")
    sumanotas=sum([nota for asignatura, nota in notas])
    print("-----")
media= sumanotas//len(notas)
print(f"La nota media es {media}")
"""




"""
Ejercicio: hacer el mismo pero con puestos y salarios, "profesor", 2000, 
"administrativo",1500, "auxiliar", 1200, "Becario",100
igual que en el ejercicio anterior con respecto a print(posicion......)
"""

# Lista bidimensional con asignaturas y notas
sueldos = [
    ["Profesor", 2000],
    ["Administrativo", 1500],
    ["Becario", 100]
]

# Acceso a posiciones concretas (fila, columna)
print("posicion 0,0 ", sueldos[0][0])  # Profesor
print("posicion 0,1 ", sueldos[0][1])  # 2000

print("posicion 1,0 ", sueldos[1][0])  # Administrativo
print("posicion 1,1 ", sueldos[1][1])  # 1500

print("posicion 2,0 ", sueldos[2][0])  # Becario
print("posicion 2,1 ", sueldos[2][1])  # 1

print("*******************")

# Recorrido de toda la lista (mostrar todos los elementos)
for profesiones, sueldo in sueldos:
    print(f"El sueldo de {profesiones} es {sueldo}")
    sumasueldo=sum([sueldo for profesiones, sueldo in sueldos])
    print("-----")
media= sumasueldo//len(sueldos)
print(f"El sueldo medio es {media}")


    
 
 