
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        # El :.2f sirve para mostrar solo 2 decimales
        return f"Empleado: {self.nombre} | Salario Total: {self.calcular_salario():.2f} €"

class Programador(Empleado):
    def __init__(self, nombre, salario_base, plus_proyecto):
        # super() llama al constructor del padre (Empleado)
        super().__init__(nombre, salario_base)
        self.plus_proyecto = plus_proyecto

    def calcular_salario(self):
        # Sobrescribe el método del padre sumando el plus
        return self.salario_base + self.plus_proyecto

class Disenador(Empleado):
    def __init__(self, nombre, salario_base, plus_herramientas):
        super().__init__(nombre, salario_base)
        self.plus_herramientas = plus_herramientas

    def calcular_salario(self):
        # Sobrescribe el método del padre sumando otro plus diferente
        return self.salario_base + self.plus_herramientas

# --- BLOQUE DE EJECUCIÓN ---

# 1. Creamos una lista para guardar a diferentes tipos de empleados
nomina = []

# 2. Instanciamos (creamos) los objetos
emp1 = Programador("Ana", 2500, 500)
emp2 = Disenador("Carlos", 2200, 300)
emp3 = Empleado("Persona Extra", 1500)

# 3. Los metemos en la lista
nomina.append(emp1)
nomina.append(emp2)
nomina.append(emp3)

# 4. Recorremos la lista y mostramos los salarios
print("--- RECIBOS DE NÓMINA ---")
for empleado in nomina:
    print(empleado)