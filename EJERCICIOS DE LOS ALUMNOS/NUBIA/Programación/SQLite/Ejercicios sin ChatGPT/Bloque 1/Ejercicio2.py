'''
Pide una nota numérica entre 0 y 10 y muestra su calificación textual:
suspenso, aprobado, bien, notable o sobresaliente. 
Idea clave: Si la nota está fuera de rango, informa del error.
'''

while True: 
    nota = float(input("Indica tu nota: ")) 

    if 0 <= nota < 5: 
        print("Suspenso") 
        break 
    elif 5 <= nota < 6: 
        print("Aprobado") 
        break 
    elif 6 <= nota < 7: 
        print("Bien") 
        break 
    elif 7 <= nota < 9: 
        print("Notable") 
        break 
    elif 9 <= nota <= 10: 
        print("Sobresaliente") 
        break 
    else: 
        print("Error: La nota debe estar entre 0 y 10. Inténtalo de nuevo.")