#Con un input me pide una nota, con condicionales, si es mayor de 4.5, que muestre un mensaje que diga que aprobado y si es menor suspendo

nota = float(input("Introduce tu nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida. Por favor ingresa una nota entre 0 y 10.")
    
else:
    if nota >= 4.5 and nota <= 5.4:
        print("Aprobado por los pelos")
    if nota >= 5.5 and nota <= 6.4:
        print("Bien")
    if nota >= 6.5 and nota <= 8.4:
        print("Pedazo de notable")
    if nota >= 8.5 and nota <10:
        print("Sobresaliente")
    if nota == 10:
        print("Ole tus cataplines")
    elif nota < 4.5:
        print("Suspenso")