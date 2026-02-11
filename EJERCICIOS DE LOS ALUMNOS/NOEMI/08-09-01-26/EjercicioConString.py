#Ejercicio trabajar con string.

nombre1="Noemi"
posicion=nombre1[0] #Posición de la letra.
print("caracter nº1", posicion)

if posicion>="N" and posicion<="I":
    print("Es mayúscula")
else:
    print("es minúscula")
    
print("el numero de caracteres", len(nombre1)) #Instrucción que cuenta las palabras que tiene una letra.