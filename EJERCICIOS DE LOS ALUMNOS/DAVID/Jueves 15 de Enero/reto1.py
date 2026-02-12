class Nomina:
    def __init__(self, nombre, puesto, nomina_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina_mensual = nomina_mensual
        # Calculamos el bruto anual (suponiendo 12 pagas según el ejemplo de 24.000)
        self.anual_bruto = nomina_mensual * 12

    def calcular_y_mostrar(self):
        # Lógica del IRPF
        if self.anual_bruto > 30000:
            porcentaje_irpf = 21
        else:
            porcentaje_irpf = 15
        
        # Cálculo de la retención y neto
        retencion = self.anual_bruto * (porcentaje_irpf / 100)
        salario_neto_anual = self.anual_bruto - retencion

        # Mostrar resultados
        print("--- RESULTADO DE LA NÓMINA ---")
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Nómina bruta mensual: {self.nomina_mensual}")
        print(f"Nómina anual bruta: {self.anual_bruto}")
        print(f"Retención {porcentaje_irpf}%: {retencion:.2f}")
        print(f"Salario neto anual: {salario_neto_anual:.2f}")
        print("-" * 30)


# Bloque principal
empleado1 = Nomina("Alberto", "Docente", 2000) 
# Nota: Para que el anual sea 24,000 como en tu ejemplo, la mensual debe ser 2000.
# Si la mensual es 2400, el anual será 28,800.

empleado1.calcular_y_mostrar()