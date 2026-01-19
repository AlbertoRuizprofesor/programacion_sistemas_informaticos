class Nomina:
    def __init__(self, nombre, puesto, nomina_mensual):
        self.nombre=nombre
        self.puesto=puesto
        self.nomina_mensual=nomina_mensual
    
    def calcular_nomina_anual(self):
        return self.nomina_mensual*10
    
    def calcula_irpf(self):
        anual=self.calcular_nomina_anual()
        if anual>30000:
            return 0.21
        else:
            return 0.15
    
    def calcular_retencion(self):
        return self.calcular_nomina_anual() * self.calcula_irpf()
    
    def calcular_salario_neto(self):
        return self.calcular_nomina_anual() - self.calcular_retencion()
    
    def mostrar_resultados(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nomina bruta mensual: {self.nomina_mensual}")
        print(f"Nomina anual bruta: {self.calcular_nomina_anual}")
        print(f"Retencion: {self.calcular_retencion}")
        print(f"Salario neto anual: {self.calcular_salario_neto}")
    
    
#MAIN

trabajador = Nomina("Rafa", "DevOp", 2300)
trabajador.mostrar_resultados()