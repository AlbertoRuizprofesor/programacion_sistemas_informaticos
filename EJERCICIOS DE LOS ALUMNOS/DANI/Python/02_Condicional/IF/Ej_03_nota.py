# Me pide por consola una nota, y la condición va a ser que si la nota es igual o mayor que cinco, me aparezca por consola "aprobado" y sino que me muestre por consola "Suspenso"
# Pedimos que el usuario introduzca la nota
nota = float(input("Dime tu nota: "))  # Ponemos 'float' porque la nota puede tener decimales.

# Creamos la condicion 'if'
if nota >= 9 and nota <= 10:
    print(f"Con un {nota} tienes un sobresaliente.")
elif nota >= 7 and nota < 9:
    print(f"Con un {nota} tienes un notable.")
elif nota >= 5 and nota < 7:
    print(f"Con un {nota} tienes un bien.")
elif nota >= 0 and nota < 5:
    print(f"Con un {nota} tienes un insuficiente.")
else:
    print(f"{nota} no es una nota real.")

# Esta condición compara el valor de que ha dado el usuario con los números que hemos puesto.
# Aquí si el 'if' no se cumple va pasando por los 'elif' para ver si se cumple uno, si ninguno se cuple va directo al 'else'. 