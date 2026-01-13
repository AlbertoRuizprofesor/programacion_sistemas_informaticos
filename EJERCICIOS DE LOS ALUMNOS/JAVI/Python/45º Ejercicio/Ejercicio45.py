"""
Ejercicio
 
me pide dos inputs, uno la nomina, otro el irpf, vamos a usar 2 funciones, 
uno que calcule el irpf,
el otro que me diga el neto que voy a cobrar, además
quiero saber el bruto anual, el irpf anual y el neto anual, 
teniendo en cuenta que son 14 pagas.
 
"""

nomina = float(input("Introduce la nómina: "))
irpf = float(input("Introduce el IRPF: "))


def calcular_irpf(nomina, irpf):
    resultado = nomina * irpf / 100
    return resultado

def calcular_neto(nomina, irpf):
    resultado = nomina - (nomina * irpf / 100)
    return resultado

resultado_irpf = calcular_irpf(nomina, irpf)
print(f"El IRPF de esa nómina es de: {resultado_irpf}")

resultado_neto = calcular_neto(nomina, irpf)
print(f"El neto de esa nómina es de: {resultado_neto}")

print(f"El bruto anual de esa nómina es de: " , (nomina * 14))
print(f"El irpf anual de esa nómina es de: " , ((nomina * irpf / 100) * 14))
print(f"El neto anual de esa nómina es de: " , (nomina * 14) - ((nomina * irpf / 100) * 14))

