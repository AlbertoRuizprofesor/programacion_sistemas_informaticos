# Creacion del cliente
class Cliente:
    # Darle atributos al cliente
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.contraseña = "1234"
        self.monto = 1000

    # Menú
    def menu(self):
        import getpass # importar libreria para contraseñas
        intentos = 3
        
        while intentos > 0:
            # Ingresar la contraseña sin que se vea
            entrada = getpass.getpass("Ingresa la contraseña: ")
            
            if entrada != self.contraseña:
                print("\nContraseña incorrecta.")
                intentos -=1
            else:
                print("\n-----MENU----")
                print(f"Bienvenido {self.nombre.capitalize()}.")
                while True:
                    print("1. Ingresar\n2. Retirar.\n3. Comprobar.\n4. Salir")
                    opcion = int(input("Seleccione una opción: "))
                    
                    match opcion:
                        case 1:
                            self.depositar()
                        case 2:
                            self.extraer()
                        case 3:
                            self.retornar_monto()
                        case 4:
                            print("Salida exitosa.\n")
                            intentos = 0 # Cerrar el primer while
                            break # Cerrar el segundo while
                        case _:
                            print("Opción no válida.\n")

    def depositar(self):
        ingresar = float(input("¿Cuánto deseas ingresar? "))
        self.monto += ingresar
        print(f"Nuevo saldo: {self.monto}\n")

    def extraer(self):
        extraccion = float(input("¿Cuánto deseas sacar? "))
        
        # Comprobar si tiene la cantidad suficiente para poder sacar dinero
        if extraccion <= self.monto:
            self.monto -= extraccion
            print(f"Nuevo saldo: {self.monto}\n")
        else:
            print("No puedes sacar esa cantidad.\n")

    def retornar_monto(self):
        print(f"Sueldo actual: {self.monto}\n")
        return self.monto

class Banco:
    def __init__(self):
        self.cliente = Cliente()

    def operar(self):
        self.cliente.menu()