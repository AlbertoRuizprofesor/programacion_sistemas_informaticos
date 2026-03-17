# Ejercicio 13. Cuenta Bancaria

class CuentaFinanciera:
    def __init__(self, dueño, fondos=0):
        self.dueño = dueño
        self.fondos = fondos

    def depositar(self, monto):
        if monto > 0:
            self.fondos += monto

    def extraer(self, monto):
        if 0 < monto <= self.fondos:
            self.fondos -= monto
            return True
        return False

    def mover_dinero(self, destino, monto):
        if self.extraer(monto):
            destino.depositar(monto)
            return True
        return False

    def ver_saldo(self):
        return f"{self.dueño}: {self.fondos:.2f} €"


cuenta_a = CuentaFinanciera("Carlos", 100)
cuenta_b = CuentaFinanciera("María", 50)

cuenta_a.mover_dinero(cuenta_b, 30)

print(cuenta_a.ver_saldo())
print(cuenta_b.ver_saldo())
