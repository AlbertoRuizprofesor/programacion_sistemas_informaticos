#Declaración de la lista capitales
capitales = [["España", "Madrid"], ["Italia", "Roma"]]

#Imprime las posiciones
print("posicion 0,0", capitales[0][0])
print("posicion 0,1", capitales[0][1])
print("posicion 1,0", capitales[1][0])
print("posicion 1,1", capitales[1][1])

#Posición Fila, columna
print("=================")

#Recorre posiciones e imprime el resultado
for pais, capital in capitales:
    print(f"La capital de {pais} es {capital}")
    print("------")

#Inserta un espacio
espacio = """

"""
print (espacio)




"""
 Ejercicio: hacer el mismo pero con notas, ejemplo "Matematicas", 10, "Historia",9, "Lengua",5
 cuando me muestre print posicion, al tener esta lista mas elementos quiero que salgan todos 
 los elementos de manera que se tiene que quedar en el print("posicion.. ", notaw[x][x][x])  # 
"""
#Declaración de la lista notas
notas = [["Matemáticas", 10], ["Historia", 9], ["Lengua", 5]]

#Imprime las posiciones 
print("posicion 0,0", notas[0][0])
print("posicion 0,1", notas[0][1])
print("posicion 1,0", notas[1][0])
print("posicion 1,1", notas[1][1])
print("posicion 2,0", notas[2][0])
print("posicion 2,1", notas[2][1])

print("=============================")

#Recorre posiciones e imprime el resultado
for asignatura, nota in notas:
    print(f"La nota de {asignatura}, es {nota}")
    print("--------------------------------")
    

print(espacio)


"""
 Ejercicio: hacer el mismo pero con puestos y salarios, "profesor", 2000, 
 "administrativo",1500, "auxiliar", 1200, "Becario",100
 igual que en el ejercicio anterior con respecto a print(posicion......)
"""
#Declaración de la lista puestos
puestos = [["Profesor", 2000], ["Administrativo", 1500], ["Auxiliar", 1200], ["Becario", 100]]

#Imprime las posiciones de la lista
print("posicion 0,0", puestos[0][0])
print("posicion 0,1", puestos[0][1])
print("posicion 1,0", puestos[1][0])
print("posicion 1,1", puestos[1][1])
print("posicion 2,0", puestos[2][0])
print("posicion 2,1", puestos[2][1])

print("===============================")

#Recorre las posiciones e imprime el resultado
for nivel, sueldo in puestos:
    print(f"El {nivel} cobra {sueldo}")
    print("--------------------------------")
    