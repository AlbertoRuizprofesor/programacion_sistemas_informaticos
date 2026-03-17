# Ejercicio

# me pide dos inputs, uno la nomina, otro el irpf, vamos a usar 2 funciones,
# uno que calcule el irpf, el otro que me diga el neto que voy a cobrar, además
# quiero saber el bruto anual, el irpf anual y el neto anual, teniendo en cuenta que son 14 pagas.


sueldo = float(input("Dime tu sueldo, bruto, es para una cosa: "))
irpf = float(input("Dime el porcentaje del IRPF: "))


def irpfMensual(sueldo, irpf):
    hacienda = sueldo * irpf / 100
    return hacienda


def sueldoNeto(sueldo, tequitan):
    neto = sueldo - tequitan
    return neto


teQuitan = irpfMensual(sueldo, irpf)
sNeto = sueldoNeto(sueldo, teQuitan)
print(f"El irpf es de tus {sueldo} es de {teQuitan}")
print(f"Tu sueldo neto es de {sNeto}")
print(f"Tu sueldo neto anual es {14 * sNeto}")
print(f"Tu sueldo bruto seria {sueldo*14} y hacienda se lleva al año: {14 * teQuitan}")
