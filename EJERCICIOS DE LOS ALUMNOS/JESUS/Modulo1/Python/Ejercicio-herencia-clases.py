# ejercicio de herencia 

class Producto:
    def __init__(self,nombre,fabricante,precio):
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
    
    #def impri(self):
        #print(self.nombre,self.fabricante,self.precio)

class Electronica(Producto):
    def __init__(self,nombre,fabricante,precio):
        super().__init__(nombre,fabricante,precio)
        
        self.modo="Gamming"
        #print(self.nombre,self.fabricante,self.precio,self.modo)

class Electrodomestico(Producto):
    def __init__(self,nombre,fabricante,precio):
        super().__init__(nombre,fabricante,precio)
        self.consumo="Wat"

class Monitores(Electronica):
    def __init__(self,nombre,fabricante,precio,pulgada):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.pulgada=pulgada
        print(self.nombre,self.fabricante,self.precio,self.modo,self.pulgada)

class Teclado(Electronica):
    def __init__(self,nombre,fabricante,precio,ergonomico):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.ergonomico=ergonomico
        print(self.nombre,self.fabricante,self.precio,self.modo,self.ergonomico)

class Portatil(Electronica):
    def __init__(self,nombre,fabricante,precio,ram):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.ram=ram
        print(self.nombre,self.fabricante,self.precio,self.modo,self.ram)

class Lavadora(Electrodomestico):
    def __init__(self,nombre,fabricante,precio,carga):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.carga=carga
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.carga)
        

class Frigorifico(Electrodomestico):
    def __init__(self,nombre,fabricante,precio,tipo):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.tipo=tipo
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.tipo)

class Freidora(Electrodomestico):
    def __init__(self,nombre,fabricante,precio,temp_max):
        super().__init__(nombre,fabricante,precio)
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        self.tem_max=temp_max
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.tem_max)


portatil1=Portatil("qweq","HP",1800,"32GB")
#portatil1.impri()
teclado1=Teclado("qwjkde","logitec",90,"ergonomico")
monitor1=Monitores("qwqwe","Asus",200,"21 Pulgadas")
lavadora1=Lavadora("sadbh","Balay",300,"Carga superior")
#frigorifico1=Frigorifico()
#freidora1=Freidora()