class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(f"\n {self.nombre} tiene depositado la suma de {self.monto}")


class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")
        self.cliente4 = Cliente("María")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)
        self.cliente4.depositar(400)

    def depositos_totales(self):
        total = (
            self.cliente1.retornar_monto()
            + self.cliente2.retornar_monto()
            + self.cliente3.retornar_monto()
            + self.cliente4.retornar_monto()
        )
        print("\nEl total de dinero del banco es:", total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()


# bloque principal

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()
