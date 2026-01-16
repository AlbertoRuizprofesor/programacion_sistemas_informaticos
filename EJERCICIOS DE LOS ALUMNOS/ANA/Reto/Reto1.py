#Reto1: POO***********************************************************************
#Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.
#nombre: Alberto 
#Puesto: Docente
#Nómina: 2400
#IRPF: si los ingresos anuales son mayores de 30.000 21% y sin menores de retencion

#resultado:
#nombre:Alberto
#puesto: Docente
#nòmina anual bruta:24.000
#retención 15% (la cantidad anual)
#salario neto (anual bruto-retencion)

class Nomina:
    def __init__(self, nombre, puesto, nomina):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina = nomina

    def nomina_anual_bruta(self):
        return self. nomina * 12

    def calcular_irpf(self):
        if self.nomina_anual_bruta() > 30000:
            return 0.21
        else:
            return 0.15

    def retencion_anual(self):
        return self.nomina_anual_bruta() * self.calcular_irpf()

    def salario_neto_anual(self):
        return self.nomina_anual_bruta() - self.retencion_anual()

    def mostrar_resultado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nómina anual bruta: {self.nomina_anual_bruta():.2f} €")
        print(f"Retención: {int(self.calcular_irpf()*100)}% ({self.retencion_anual():.2f} €)")
        print(f"Salario neto anual: {self.salario_neto_anual():.2f} €")

empleado = Nomina("Alberto", "Docente", 2000)
empleado.mostrar_resultado()


  
    


