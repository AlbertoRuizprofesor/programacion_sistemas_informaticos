profesiones = [["profesor", 2000],["administrativo", 1500], ["auxiliar", 1200], ["Becario", 100]]

print("posicion 0,0", profesiones[0][0]) # profesor
print("posicion 0,1", profesiones[0][1]) # 2000
print("posicion 1,0", profesiones[1][0]) # administrativo
print("posicion 1,1", profesiones[1][1]) # 1500
print("posicion 2,0", profesiones[2][0]) # auxiliar
print("posicion 2,1", profesiones[2][1]) # 1200
print("posicion 3,0", profesiones[3][0]) # Becario
print("posicion 3,1", profesiones[3][1]) # 100

# posicion [Fila][Columna]
print("**********")

for profesion, sueldo in profesiones:
    print(f"Un {profesion} cobra {sueldo}€.")