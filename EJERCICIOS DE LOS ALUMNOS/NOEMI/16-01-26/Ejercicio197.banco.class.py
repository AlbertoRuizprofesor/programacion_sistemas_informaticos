#Ejercicio 197: 

class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0
    
    def depositar(self,monto):
        self.monto=self.monto+monto
        
    def extraer(self,monto):
        self.monto=self.monto-monto
        
    def retornar_monto(self):
        return self.monto
    
    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

class Banco:
    
    def __init__(self):
        self.cliente1=Cliente("Noemi")    
        self.cliente2=Cliente("Jose")
        self.cliente3=Cliente("Sheila")
        self.cliente4=Cliente("Cova")
        self.cliente5=Cliente("Pilar")
    
    def operar(self):
        self.cliente1.depositar(500)     
        self.cliente2.depositar(300)       
        self.cliente3.depositar(460)       
        self.cliente4.depositar(20)       
        self.cliente5.depositar(60) 
        
    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()+self.cliente4.retornar_monto()+self.cliente5.retornar_monto()       
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        self.cliente4.imprimir()
        self.cliente5.imprimir()
        

banco1=Banco()
banco1.operar()
banco1.depositos_totales()