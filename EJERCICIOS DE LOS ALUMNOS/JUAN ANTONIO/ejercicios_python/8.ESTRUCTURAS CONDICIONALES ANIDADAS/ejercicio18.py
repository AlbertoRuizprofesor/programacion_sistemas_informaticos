#- Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. 
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según 
# el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:

#Nivel máximo:	Porcentaje>=90%.
#Nivel medio:	Porcentaje>=75% y <90%.
#Nivel regular:	Porcentaje>=50% y <75%.
#Fuera de nivel:	Porcentaje<50%.
    

# Pedimos al usuario el número total de preguntas del examen
total = int(input("Indique el número total de preguntas del examen: "))

# Pedimos cuántas preguntas ha contestado correctamente
correctas = int(input("Indique el número de preguntas correctas: "))

# Calculamos el porcentaje de aciertos
porcentaje = (correctas / total) * 100

# Primera condición: si el porcentaje es 90% o más: Nivel Máximo
if porcentaje >= 90:
    print(f"Has acertado {correctas} de {total}, lo que equivale a un porcentaje {porcentaje:.2f}%. Tienes Nivel Máximo")

else:
    # Si no llega al 90%, comprobamos si es 75% o más: Nivel Medio
    if porcentaje >= 75:
        print(f"Has acertado {correctas} de {total}, lo que equivale a un porcentaje {porcentaje:.2f}%. Tienes Nivel Medio")

    else:
        # Si tampoco llega al 75%, comprobamos si es 50% o más: Nivel Regular
        if porcentaje >= 50:
            print(f"Has acertado {correctas} de {total}, lo que equivale a un porcentaje {porcentaje:.2f}%. Tienes Nivel Regular")

        else:
            # Si no cumple ninguna condición anterior: Fuera de nivel
            print(f"Has acertado {correctas} de {total}, lo que equivale a un porcentaje {porcentaje:.2f}%. Estás fuera de nivel")


