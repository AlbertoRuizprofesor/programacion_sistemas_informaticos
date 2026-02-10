# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n_puntos = int(input("¿Cuántos puntos quieres ingresar de cada?: "))
contador_cuadrante_1 = 0 # cuadrante 1 = +, +
contador_cuadrante_2 = 0 # cuadrante 2 = -, +
contador_cuadrante_3 = 0 # cuadrante 3 = -, -
contador_cuadrante_4 = 0 # cuadrante 4 = +, -

for n in range (n_puntos):
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))

    if x > 0 and y > 0:
        contador_cuadrante_1 += 1
    elif x < 0 and y > 0:
        contador_cuadrante_2 += 1
    elif x < 0 and y < 0:
        contador_cuadrante_3 += 1
    elif x > 0 and y < 0:
        contador_cuadrante_4 += 1

print(f"Puntos en el primer cuadrante: {contador_cuadrante_1}")
print(f"Puntos en el segundo cuadrante: {contador_cuadrante_2}")
print(f"Puntos en el tercer cuadrante: {contador_cuadrante_3}")
print(f"Puntos en el cuarto cuadrante: {contador_cuadrante_4}")