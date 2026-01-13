notas = [["Matemáticas", 10],["Historia", 9], ["Lengua", 5]]

print("posicion 0,0", notas[0][0]) # Matemáticas
print("posicion 0,1", notas[0][1]) # 10
print("posicion 1,0", notas[1][0]) # Historia
print("posicion 1,1", notas[1][1]) # 9
print("posicion 2,0", notas[2][0]) # Lengua
print("posicion 2,1", notas[2][1]) # 5

# posicion [Fila][Columna]
print("**********")

for asignatura, nota in notas:
    print(f"La nota de {asignatura} es {nota}.")