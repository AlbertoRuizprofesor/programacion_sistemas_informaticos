#crear una lista bidimensional
capitales=[["España", "Madrid"], ["Italia", "Roma"]]

#realizamos varios print con las distintas posiciones dentro de la lista

print("posicion 0,0 ", capitales[0][0])  # Imprime "España"
print("posicion 0,1 ", capitales[0][1])  # Imprime "Madrid"
print("posicion 1,0 ", capitales[1][0])  # Imprime "Italia"
print("posicion 1,1 ", capitales[1][1])  # imprime "Roma"

print("*******************")


for pais, capital in capitales:
    print(f"La capital de {pais} es {capital}.")
    print("-----")

    