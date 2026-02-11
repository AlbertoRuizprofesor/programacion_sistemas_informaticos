salario=int(input("dime tu salario: "))
salarioBruto=salario*14

print("Su salario mensual es: ", salario)
print("el salario anual es de: ", salarioBruto)

if salarioBruto>40000:
    salarioNeto=salarioBruto * 0.21
    print("el tramo a aplicar es del 21%")
else:
    salarioNeto=salarioBruto * 0.15
    print("el tramo a aplicar es del 15")

print("tiene que pagar a hacienda: ", salarioNeto)