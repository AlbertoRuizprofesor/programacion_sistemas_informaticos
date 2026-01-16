"""
RETO 1 POO: Nómina con clase Trabajador
- Carga nombre, puesto, nómina mensual
- Calcula anual bruta, IRPF (21% >30k, 15% <=30k), neto
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

class Trabajador:
    def __init__(self, nombre, puesto, nomina_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_mensual = nomina_mensual
        self.anual_bruto = nomina_mensual * 14

    def calcular_irpf(self):
        if self.anual_bruto > 30000:
            porcentaje = 21
        else:
            porcentaje = 15
        self.retencion = self.anual_bruto * (porcentaje / 100)
        self.anual_neta = self.anual_bruto - self.retencion
        return porcentaje

    def mostrar_nomina(self):
        porcentaje = self.calcular_irpf()
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nómina bruta mensual: {self.nomina_mensual:,.0f}")
        print(f"Nómina anual bruta: {self.anual_bruto:,.0f}")
        print(f"Retención {porcentaje}%: {self.retencion:,.0f}")
        print(f"Salario neto anual: {self.anual_neta:,.0f}")


#Main
trab1 = Trabajador("Alberto", "Docente", 2400)
mensaje("Nómina Alberto")
trab1.mostrar_nomina()

trab2 = Trabajador("Luis", "Director", 3500)  # >30k
mensaje("Nómina Luis")
trab2.mostrar_nomina()

mensaje("Fin programa")
