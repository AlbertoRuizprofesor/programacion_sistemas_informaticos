#  me pide dos inputs, uno la nomina, otro el irpf, vamos a usar 2 funciones, uno que calcule el irpf, el otro que me diga el neto que voy a cobrar, además quiero saber el bruto anual, el irpf anual y el neto anual, teniendo en cuenta que son 14 pagas.
nomina = float(input("Introduce tu salario bruto mensual: "))
irpf = float(input("Introduce el IRPF: "))

def calcular_irpf(salario_bruto_mensual, irpf):
    return nomina*irpf/100

def calcular_neto(nomina, irpf):
    return nomina-calculo 

calculo = calcular_irpf(nomina, irpf)
neto = calcular_neto(nomina, irpf)

print("El IRPF es: ", calculo)
print("El neto es: ", neto)

print(f"El IRPF anual es: {calculo*14}")
print(f"El neto anual es: {neto*14}")
print(f"El bruto anual es: {nomina*14}")