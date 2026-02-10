"""Ahora plantearemos otro problema empleando herencia.
Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta.
Cada clase tiene como atributo valor1, valor2 y resultado.
Los métodos a definir son
cargar1 (que inicializa el atributo valor1),
carga2 (que inicializa el atributo valor2),
operar (que en el caso de la clase "Suma" suma los dos atributos
y en el caso de la clase "Resta" hace la diferencia entre valor1 y valor2),
y otro método mostrar_resultado.
Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos.
En estos casos es bueno definir una clase padre que agrupe dichos atributos y responsabilidades comunes.
La relación de herencia que podemos disponer para este problema es:"""

class Operacion:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = float(input("Valor 1: "))

    def cargar2(self):
        self.valor2 = float(input("Valor 2: "))

    def mostrar_resultado(self):
        print(f"Resultado: {self.resultado:.2f}")

    def operar(self):
        pass


class Suma(Operacion):

    def operar(self):
        self.resultado = self.valor1 + self.valor2


class Resta(Operacion):

    def operar(self):
        self.resultado = self.valor1 - self.valor2


#Main
print("=== SUMA ===")
suma = Suma()
suma.cargar1()      # HEREDA
suma.cargar2()      # HEREDA
suma.operar()
suma.mostrar_resultado()  # HEREDA

print("\n=== RESTA ===")
resta = Resta()
resta.cargar1()
resta.cargar2()
resta.operar()
resta.mostrar_resultado()
