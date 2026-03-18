# Ejercicio 15. Jerarquía empleados

class Trabajador:
    def __init__(self, identificador, base):
        self.identificador = identificador
        self.base = base

    def calcular_pago(self):
        return self.base

    def __str__(self):
        return f"{self.identificador} -> {self.calcular_pago():.2f} €"


class Desarrollador(Trabajador):
    def __init__(self, identificador, base, extra_proyecto):
        super().__init__(identificador, base)
        self.extra_proyecto = extra_proyecto

    def calcular_pago(self):
        return self.base + self.extra_proyecto


class Creativo(Trabajador):
    def __init__(self, identificador, base, extra_herramientas):
        super().__init__(identificador, base)
        self.extra_herramientas = extra_herramientas

    def calcular_pago(self):
        return self.base + self.extra_herramientas
    

# -------------------------
# EJEMPLO 
# -------------------------

t1 = Desarrollador("Carlos", 1200, 300)
t2 = Creativo("Lucía", 1100, 150)
t3 = Trabajador("Pepe", 1000)

print(t1)
print(t2)
print(t3)