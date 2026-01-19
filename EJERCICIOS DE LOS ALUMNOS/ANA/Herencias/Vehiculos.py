class Transporte:
 def imprimir():
    print(f"el vehiculo es {self.nombre} rueda {self.rueda} su motor es {motor}")

class Vehiculo(Transporte):
  def __init__(self, nombre, ruedas, motor, pasajeros):
    super().__init__(nombre,ruedas,motor)
    self.pasajero = pasajeros

     def imprimir(self):
      super().imprimir()
      print(self.pasajeros)

class Coches(Vehiculos):
    
    def __init__(self, nombre, ruedas, motor, pasajeros,maletero):
    super().imprimir()
    self.maletero = maletero

    def imprimir(self):
      super().__init__(nombre,ruedas,motor,pasajeros,maleteros)

    def imprimir(self):
      super().imprimir()
      print(self.maletero)

coche1=Coche("BMW",4,"2500cc",51,200)
coche1.imprimir()

    

  

    