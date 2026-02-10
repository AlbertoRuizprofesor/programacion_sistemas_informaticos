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
        print(f"{self.nombre} tiene depositado la suma de {self.monto}")


class Banco:

    def __init__(self):
        # Se mantienen los 3 originales y se añaden 2 más
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Diego")
        self.cliente4 = Cliente("Laura")
        self.cliente5 = Cliente("Fernando")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente4.depositar(500)
        self.cliente5.depositar(1000)
        
        # Operaciones de extracción (la original + 2 nuevas)
        self.cliente3.extraer(150)
        self.cliente4.extraer(200) # Nueva extracción
        self.cliente5.extraer(500) # Nueva extracción

    def depositos_totales(self):
        total = (self.cliente1.retornar_monto() + 
                 self.cliente2.retornar_monto() + 
                 self.cliente3.retornar_monto() +
                 self.cliente4.retornar_monto() +
                 self.cliente5.retornar_monto())
        
        print("--- Resumen del Banco ---")
        print("El total de dinero del banco es:", total)
        print("-" * 25)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()
        self.cliente5.imprimir()


# Bloque principal
banco1 = Banco()
banco1.operar()
banco1.depositos_totales()