# #Ahora plantearemos otro problema empleando herencia. 
# Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta. 
# Cada clase tiene como atributo valor1, valor2 y resultado. Los métodos a definir son cargar1 (que inicializa el atributo valor1), carga2 (que inicializa el atributo valor2), operar (que en el caso de la clase "Suma" suma los dos atributos y en el caso de la clase "Resta" hace la diferencia entre valor1 y valor2), y otro método mostrar_resultado.

# Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos. 
# En estos casos es bueno definir una clase padre que agrupe dichos atributos y responsabilidades comunes.

# La relación de herencia que podemos disponer para este problema es:

class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0
        self.resultado=0

    def cargar_val1(self):
        self.valor1=int(input("Ingresa el primer numero: "))


    def cargar_val2(self):
        self.valor2=int(input("Ingresa el segundo valor: "))

    def mostrar_result(self):
        print(self.resultado)


    def operar(self):
        pass
    