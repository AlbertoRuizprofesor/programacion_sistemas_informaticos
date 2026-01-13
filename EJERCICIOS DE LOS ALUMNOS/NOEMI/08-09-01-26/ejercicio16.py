#Ejercicio 16:Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

cant1=0
cant2=0
cant3=0
cant4=0

puntos=int(input("Ingrese la cantidad de puntos a ingresar: "))

for i in range(puntos):
    print(f"Punto {i+1}")
    x=int(input("Ingrese coordenada x: "))
    y=int(input("Ingrese coordenada y: "))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1
                    
print("\nCantidad de puntos por cuadrante:")
print("La cantidad de puntos en el primer cuadrante: ", cant1 )
print("La cantidad de puntos en el segundo cuadrante es ", cant2)
print("La cantidad de puntos en el tercer cuadrante es ", cant3)
print("La cantidad de puntos en el cuarto cuadrante es ", cant4)
