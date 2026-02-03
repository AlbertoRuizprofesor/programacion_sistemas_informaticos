"""
Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.
 
nombre: Alberto
Puesto: Docente
Nómina: 2400
IRPF: si los ingresos anuales son mayores de 30.000 21% y sin menores 15% de retención
 
Resultado:
nombre: Alberto
Puesto: Docente
Nómina bruta: 2400
Nómina anual bruta: 24.000
Retención 15%: (la cantidad anual)
Salario neto (anual bruto-retencion)

"""

class Empleado:
    def __init__(self):
        print("APP CÁLCULO DE NÓMINA")
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.puesto = input("Ingrese el puesto del empleado: ")
        self.nomina = int(input("Ingrese la nómina bruta mensual del empleado: "))
        self.anualbruta = self.nomina * 12
        self.irpf 
        self.anualneto
        
    def irpf(self):
        if self.anualbruta > 30000:
            self.irpf = self.anualbruta * 0.15
        else:
            self.irpf = self.anualbruta * 0.21
        return self.irpf
    
    def anualneto(self):
        self.anualneto = self.anualbruta - self.irpf
        return self.anualneto
    
# Bloque principal
empleado1 = Empleado()
print("-------------------------------------------")
print(f"Nombre: {empleado1.nombre}")
print(f"Puesto: {empleado1.puesto}")
print(f"Nómina bruta: {empleado1.nomina}")
print(f"Nómina anual bruta: {empleado1.anualbruta}")
print(f"Retención: {empleado1.irpf()}")
print(f"Salario neto anual: {empleado1.anualneto()}")