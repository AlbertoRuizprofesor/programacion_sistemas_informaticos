# ejercicio de herencia 

class Producto:
    def __init__(self):
        self.nombre=""
        self.fabricante=""
        self.precio=""
    
    #def impri(self):
        #print(self.nombre,self.fabricante,self.precio)

class Electronica(Producto):
    def __init__(self):
        super().__init__()
        
        self.modo="Gamming"
        #print(self.nombre,self.fabricante,self.precio,self.modo)

class Electrodomestico(Producto):
    def __init__(self):
        super().__init__()
        self.consumo="Wat"

class Monitores(Electronica):
    def __init__(self):
        super().__init__()
        self.nombre="rgergerg"
        self.fabricante="Asus"
        self.precio="200"
        self.pulgada="21"
        print(self.nombre,self.fabricante,self.precio,self.modo,self.pulgada)

class Teclado(Electronica):
    def __init__(self):
        super().__init__()
        self.nombre="465wf"
        self.fabricante="logitec"
        self.precio="80"
        self.ergonomico="ergonomico"
        print(self.nombre,self.fabricante,self.precio,self.modo,self.ergonomico)

class Portatil(Electronica):
    def __init__(self):
        super().__init__()
        self.nombre="123dasdasd"
        self.fabricante="HP"
        self.precio="1888"
        self.ram="32GB"
        print(self.nombre,self.fabricante,self.precio,self.modo,self.ram)

class Lavadora(Electrodomestico):
    def __init__(self):
        super().__init__()
        self.nombre="iqwjoqw"
        self.fabricante="Daewoo"
        self.precio="800"
        self.carga="superior"
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.carga)
        

class Frigorifico(Electrodomestico):
    def __init__(self):
        super().__init__()
        self.nombre="wrfasdf"
        self.fabricante="Balay"
        self.precio="400"
        self.tipo="NoFrost"
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.tipo)

class Freidora(Electrodomestico):
    def __init__(self):
        super().__init__()
        self.nombre="wefrwer"
        self.fabricante="Cecotec"
        self.precio="50"
        self.tem_max="200ºC"
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.tem_max)


portatil1=Portatil()
#portatil1.impri()
teclado1=Teclado()
monitor1=Monitores()
lavadora1=Lavadora()
frigorifico1=Frigorifico()
freidora1=Freidora()