"""
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Cliente y la clase Banco.

Luego debemos definir los atributos y los métodos de cada clase:
"""

class Cliente:

    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self,monto):
        self.monto = self.monto+monto

    def extraer(self,monto):
        self.monto = self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre,"tiene",self.monto)


class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Nubia")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Noemí")
        self.cliente4 = Cliente("Darío")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(100)
        self.cliente3.depositar(100)
        self.cliente4.depositar(100)
        self.cliente3.extraer(50)
        self.cliente4.extraer(50)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()+self.cliente4.retornar_monto()
        print(f"El total de dinero del banco es: {total}")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()


# Bloque principal
banco1 = Banco()
banco1.operar()
banco1.depositos_totales()

