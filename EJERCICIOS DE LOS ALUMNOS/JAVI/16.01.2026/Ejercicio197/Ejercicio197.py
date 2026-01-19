"""
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. 
También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Cliente y la clase Banco.
Luego debemos definir los atributos y los métodos de cada clase:
"""

class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.saldo=0

    def depositar(self,saldo):
        self.saldo=self.saldo+saldo

    def extraer(self,saldo):
        self.saldo=self.saldo-saldo

    def retornar_saldo(self):
        return self.saldo

    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.saldo)


class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_saldo()+self.cliente2.retornar_saldo()+self.cliente3.retornar_saldo()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


# bloque principal

banco1=Banco()
banco1.operar()
banco1.depositos_totales()

