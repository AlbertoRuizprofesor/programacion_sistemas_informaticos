cantidad = 0
n = int(input("Cuantos coodenadas ingresará: "))
lat = 0
lon = 0
cuadrante0 = 0
cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0

for f in range(n):
    lat = int(input(f"Ingrese la Latitud de la coodenada {f}: "))
    lon = int(input(f"Ingrese la Longitud de la coordenada {f}: "))

    if lat == 0 or lon == 0:
        cuadrante0 += 1
        print("Estas coordenadas no estan en ningun cuadrante, my friend")
    elif lat > 0 and lon > 0:
        cuadrante1 += 1
        print("Coordenada en el cuadrante 1")
    elif lat > 0 and lon < 0:
        cuadrante2 += 1
        print("Coordenadas en cuadrante 2")
    elif lat < 0 and lon > 0:
        cuadrante3 += 1
        print("Coordenadas en cuadrante 3")
    else:
        cuadrante4 += 1
        print("Coordenadas en cuadrante 4")

print(f"En Cuadrante 1 hay : {cuadrante1} coordenadas")
print(f"En Cuadrante 2 hay : {cuadrante2} coordenadas")
print(f"En Cuadrante 3 hay : {cuadrante3} coordenadas")
print(f"En Cuadrante 4 hay : {cuadrante4} coordenadas")
print(f"No están en ningún cuadrante en concreto: {cuadrante0} coordenadas")
