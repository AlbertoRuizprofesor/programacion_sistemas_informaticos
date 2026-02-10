salarioMensual = int(input("Salario Mensual Bruto: "))
salarioAnual = salarioMensual * 14
if salarioAnual >= 56000:
    print(f"Tu impuesto es del 21% y tu cobras: {salarioAnual - salarioAnual*0.21} al año o {salarioMensual - salarioMensual*0.21} al mes netos.")
    print(f"Hacienda se lleva: {salarioAnual*0.21} todos los años o {salarioMensual*0.21} todos los meses.")
else:
    print(f"Tu impuesto es del 15% y tu cobras: {salarioAnual - salarioAnual*0.15} al año o {salarioMensual - salarioMensual*0.15} al mes netos.")
    print(f"Hacienda se lleva: {salarioAnual*0.15} todos los años o {salarioMensual*0.15} todos los meses.")