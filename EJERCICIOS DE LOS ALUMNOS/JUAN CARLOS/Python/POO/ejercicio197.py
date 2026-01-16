"""
Banco con 3 clientes internos.
Clientes hacen depósitos/extracciones vía Banco (relación composición).
"""

#Funciones
def borrarPantalla():
	print("\033c", end="")

def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} depositó {cantidad}. Saldo: {self.saldo}")

    def extraer(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"{self.nombre} extrajo {cantidad}. Saldo: {self.saldo}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para realizar la operación. ")

    def retornarMonto(self):
        return self.saldo

    def imprimir(self):
        print(f"El cliente: {self.nombre} tiene un saldo de: {self.saldo}")


class Banco:
    def __init__(self):
        # Clientes creados DIRECTAMENTE en Banco (composición fuerte)
        self.cliente1 = Cliente("Juan Pérez")
        self.cliente2 = Cliente("Ana García")
        self.cliente3 = Cliente("Luis López")
        self.cliente4 = Cliente("Pere Rebasa")
        self.cliente5 = Cliente("Ana Carpio")
        self.cliente6 = Cliente("Marco Santos")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)
        self.cliente4.depositar(400)
        self.cliente5.depositar(950)
        self.cliente6.depositar(20000)
        self.cliente6.extraer(30000)



    def total_depositado(self):
        total = self.cliente1.saldo + self.cliente2.saldo + self.cliente3.saldo + self.cliente4.saldo + self.cliente5.saldo + self.cliente6.saldo
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()
        self.cliente5.imprimir()
        self.cliente6.imprimir()


#Main
borrarPantalla()
banco = Banco()
banco.operar()
banco.total_depositado()

mensaje("Fin del programa")
