#Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

# Lo primero que hacemos es identificar las clases:

# Podemos identificar la clase Cliente y la clase Banco.

# Luego debemos definir los atributos y los métodos de cada clase:

class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto


    def retirar(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto
    
    def imprimir(self):
        print(self.nombre,"Tiene un saldo de ",self.monto)

class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")
        self.cliente4=Cliente("Yisus")
        self.cliente5=Cliente("Albertron")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.retirar(150)
        self.cliente4.depositar(449)
        self.cliente4.retirar(449)
        self.cliente5.depositar(2000)
        self.cliente5.retirar(1200)


    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()+self.cliente4.retornar_monto()+self.cliente5.retornar_monto()
        print("El total del dinero en el banco es: ",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()
        self.cliente5.imprimir()

#bloque principal
banco1=Banco()
banco1.operar()
banco1.depositos_totales()


    