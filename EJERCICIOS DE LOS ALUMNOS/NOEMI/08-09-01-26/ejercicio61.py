#Ejercicio 61: Realizaar la carga de dos nombres distintos. Mostrar por pantalla orden alfabetico.

nom1="Saras"
nom2="Sara"

if nom1<nom2:
    print(f"{nom2} es mayor alfabeticamente que {nom1}")
elif nom1>nom2:
    print(f"{nom1} es mayor alfabeticamente que {nom2}")
    
else:
    print("Son iguales alfabeticamente")