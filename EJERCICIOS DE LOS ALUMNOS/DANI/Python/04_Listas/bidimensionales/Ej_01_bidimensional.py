capitales = [["España", "Madrid"],["Italia", "Roma"]]

print("posicion 0,0", capitales[0][0]) # España
print("posicion 0,1", capitales[0][1]) # Madrrd
print("posicion 1,0", capitales[1][0]) # Italia
print("posicion 1,1", capitales[1][1]) # Roma

# posicion [Fila][Columna]
print("**********")

for pais, capital in capitales:
    print(f"La capitañ de {pais} es {capital}.")