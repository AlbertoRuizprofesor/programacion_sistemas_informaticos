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

    def __init__(self, nombre, puesto, nomina_mensual_bruta):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_mensual_bruta = nomina_mensual_bruta

    def mostrar_detalles(self):

        print(f"\nNombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nómina bruta mensual: {self.nomina_mensual_bruta}")

        nomina_anual_bruta = self.nomina_mensual_bruta * 14
        print(f"Nómina anual bruta: {nomina_anual_bruta}")

        if nomina_anual_bruta > 40000:
            irpf = 0.21
        else:
            irpf = 0.15

        retencion_mensual = self.nomina_mensual_bruta * irpf
        retencion_anual = self.nomina_mensual_bruta * 14 * irpf

        print(f"Retencion del ({irpf*100}%)")

        print(f"Sueldo Neto Mensual: {self.nomina_mensual_bruta-retencion_mensual}")

        print(f"Salario neto anual: {(self.nomina_mensual_bruta*14)-retencion_anual}")
        print("_________________________")
        print("")


# Bloque Principal
nomina1 = Nomina("Alberto", "Docente", 2400)
nomina1.mostrar_detalles()

nomina2 = Nomina("Beatriz", "Administrativa", 3000)
nomina2.mostrar_detalles()

nomina3 = Nomina("Carlos", "Director", 5000)
nomina3.mostrar_detalles()

nomina4 = Nomina("Diana", "Técnico", 2200)
nomina4.mostrar_detalles()

# Realizar con programación en objeto una nomina, ejemplo,
# realizarlo con el constructor y una sola funcion o metodo.
