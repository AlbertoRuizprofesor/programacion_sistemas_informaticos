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

class Empleados:
    def __init__(self, nombre, puesto, nomina_bruta):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_bruta = nomina_bruta
        self.nomina_anual_bruta =  self.nomina_bruta * 12
        self.irpf 
        self.salario_neto
        
        
    def nomina_anual_bruta(self):
        self.nomina_anual_bruta = self.nomina_bruta*12
        return self.nomina_anual_bruta
    
    def irpf(self):
        if self.nomina_anual_bruta > 30000:
            self.irpf = self.nomina_anual_bruta * 0.15
        else:
            self.irpf = self.nomina_anual_bruta * 0.21
        return self.irpf
            
    
    def salario_neto(self):
        self.salario_neto = self.nomina_anual_bruta - self.irpf
        return self.salario_neto
    
        
# Programa principal
empleado1 = Empleados("Nubia", "informática", 2000)
print("-------------------------------------------")
print(f"Nombre: {empleado1.nombre}")
print(f"Puesto: {empleado1.puesto}")
print(f"Nómina bruta: {empleado1.nomina_bruta}")
print(f"Nómina anual bruta: {empleado1.nomina_anual_bruta}")
print(f"Retención: {empleado1.irpf()}")
print(f"Salario neto anual: {empleado1.salario_neto()}")


