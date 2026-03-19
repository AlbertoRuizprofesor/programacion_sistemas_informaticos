class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def transferir(self, otra_cuenta, cantidad):
        if self.retirar(cantidad):
            otra_cuenta.ingresar(cantidad)
            return True
        return False

    def mostrar_saldo(self):
        return f"{self.titular}: {self.saldo:.2f} €"

c1 = CuentaBancaria("Ana", 100)
c2 = CuentaBancaria("Luis", 50)
c1.transferir(c2, 30)
print(c1.mostrar_saldo())
print(c2.mostrar_saldo())
