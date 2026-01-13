print("Ejercicio Salario")
print("")
print("")

salmes=float(input("Introduce tu salario bruto mensual:"))
salanual=salmes*14

print("Tu salario mensual es:", salmes)
print("Tu salario anual es: ",salanual)

if salanual>40000:
    print("El tramo a aplicar es el 21%")
    print("Tienes que pagar a hacienda:", salanual*0.21)
else:
    print("El tramo a aplicar es el 15%")
    print("Tienes que pagar a hacienda:", salanual*0.15)