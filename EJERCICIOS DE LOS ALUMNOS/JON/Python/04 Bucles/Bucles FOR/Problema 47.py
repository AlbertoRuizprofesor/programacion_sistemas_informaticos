print("Ejercicio 47")
print("")
print("")

n=int(input("¿Cuántos triángulos quieres procesar?: "))
mayora12=0
for x in range(n):
    base=int(input("Introduce la base del triángulo: "))
    altura=int(input("Introduce la altura del triángulo: "))
    superficie=(base*altura)/2
    print("La medida de la base es: ", base)
    print("La medida de la altura es: ", altura)
    print("El superficie del triángulo es: ", superficie)
    if superficie>12:
        mayora12=mayora12+1
print("Cantidad de triángulos con superficie mayor a 12: ", mayora12)
