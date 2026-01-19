# Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.

#  nombre: Alberto
#  Puesto: Docente
#  Nómina: 2400
#  IRPF: si los ingresos anuales son mayores de 30.000 21% y sin menores 15% de retención

#  Resultado:

# nombre: Alberto
# Puesto: Docente
# Nómina bruta: 2400
# Nómina anual bruta: 24.000
# Retención 15%: (la cantidad anual)
# Salario neto (anual bruto-retencion)


class Nomina:

    def __init__(self, nombre, puesto, nomina_mensual, ingresos_anuales):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_mensual = nomina_mensual
        self.ingresos_anuales = ingresos_anuales

    def calcular_retencion(self):
        if self.ingresos_anuales > 30000:
            return 0.21
        else:
            return 0.15

    def calcular_nomina_anual(self):
        return self.nomina_mensual * 14  # considerando pagas extras

    def calcular_retencion_anual(self):
        retencion = self.calcular_retencion()
        return self.calcular_nomina_anual() * retencion

    def calcular_salario_neto(self):
        return self.calcular_nomina_anual() - self.calcular_retencion_anual()

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nómina bruta mensual: {self.nomina_mensual}")
        print(f"Nómina anual bruta: {self.calcular_nomina_anual()}")
        print(
            f"Retención anual ({self.calcular_retencion()*100}%): {self.calcular_retencion_anual()}"
        )
        print(f"Salario neto anual: {self.calcular_salario_neto()}")


# bloque principal
nomina1 = Nomina("Alberto", "Docente", 2400, 28000)
nomina1.mostrar_detalles()
print("_________________________")
nomina2 = Nomina("Beatriz", "Administrativa", 3000, 35000)
nomina2.mostrar_detalles()
print("_________________________")
nomina3 = Nomina("Carlos", "Director", 5000, 60000)
nomina3.mostrar_detalles()
print("_________________________")
nomina4 = Nomina("Diana", "Técnico", 2200, 25000)
nomina4.mostrar_detalles()

# Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.
