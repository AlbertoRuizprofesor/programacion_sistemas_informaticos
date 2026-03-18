'''
Crea una clase CuentaBancaria con titular y saldo. 
Añade métodos ingresar, retirar y mostrar_saldo. 
Evita retirar más dinero del disponible. 
Idea clave: Añade un método transferir a otra cuenta. 
'''

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"\nINGRESAR DINERO \n{self.titular}, has ingresado {cantidad}. Saldo actual: {self.saldo}")
            
        else:
            print(f"{self.titular}: La cantidad a ingresar debe ser positiva.")
            
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"\nRETIRAR DINERO \n{self.titular}, no puedes retirar más dinero del disponible.")
            
        elif cantidad <= 0:
            print(f"{self.titular}: La cantidad a retirar debe ser positiva.")
            
        else:
            self.saldo -= cantidad
            print(f"\nRETIRAR DINERO \n{self.titular}, has retirado {cantidad}. Saldo actual: {self.saldo}")
            
    def mostrar_saldo(self):
        print(f"\nMOSTRAR SALDO \nTitular: {self.titular} \nSaldo: {self.saldo}")
        
    def transferir(self, cantidad, cuenta_destino):
        if cantidad > self.saldo:
            print(f"\nTRANSFERIR DINERO \n{self.titular}, no puedes transferir más dinero del disponible.")
            
        elif cantidad <= 0:
            print(f"{self.titular}: La cantidad a transferir debe ser positiva.")
            
        else:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print(f"\nTRANSFERIR DINERO \n{self.titular}, has transferido {cantidad} a {cuenta_destino.titular}\nSaldo actual: {self.saldo}")

# Main 
cuenta1 = CuentaBancaria("Nubia",0)
cuenta2 = CuentaBancaria("Darío",0)

cuenta1.ingresar(1000)
cuenta1.retirar(200)
cuenta1.transferir(300, cuenta2)
cuenta2.mostrar_saldo()