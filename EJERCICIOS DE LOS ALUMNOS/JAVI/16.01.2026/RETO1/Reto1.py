"""
RETO 1: POO**********************************************************************************************
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

class Nomina:
    def __init__(self, nombre, puesto, nomina_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_mensual = nomina_mensual

    def calcular_nomina_anual(self):
        return self.nomina_mensual * 12        
      
    def calcular_irpf(self):
        anual = self.calcular_nomina_anual()
        if anual > 30000:
            return anual * 0.21
        else:
            return anual * 0.15
       
    def calcular_retencion(self):
        return self.calcular_nomina_anual * self.calcular_irpf       

    def calcular_salario_neto(self):
        return self.calcular_nomina_anual - self.calcular_retencion
      
    def mostrar_resultado(self):
    print("Nombre: ", self.nombre)
    print("Puesto: ", self.puesto)
    print("Nomina bruta mensual: ", self.nomina_mensual())
    print("Nomina bruta anual: ", self.calcular_nomina_anual())
    print("Retención: ", self.calcular_retencion())
    print("Salario neto anual: ", self.calcular_salario_neto())


              

# Crear objeto
empleado = Nomina("Alberto", "Docente", 2400)

# Mostrar resultados
empleado.mostrar_resultado()

    

        