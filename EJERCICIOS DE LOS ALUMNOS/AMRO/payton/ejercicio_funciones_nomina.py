 #nominas-inputs

nomina=int(input("Introduce la nomina bruta: "))
irpf=int(input("Introduce el irpf: "))  

#definicion de funciones

def calcular_irpf(nomina, irpf):
    return nomina*irpf/100  

def Calcular_neto(nomina): 
    return nomina - calculo

#definicion de variables asignadas a funciones

calculo=calcular_irpf(nomina, irpf)
calculo_neto=Calcular_neto(nomina)

#calculo mensual

print(f"El irpf es: {calculo}")
print(f"El neto es: {calculo_neto}")

#calculo anual

print(f"El irpf anual es: {calculo*14}")
print(f"El neto anual es: {calculo_neto*14}")
print(f"El bruto anual es: {nomina*14}")  
