class Contabilidad:
    def __init__(self, factura, producto, precio):
        self.factura=factura
        self.producto=producto
        self.precio=precio
    
    def mostrar_resultado(self):
        unitario=0.21 * self.precio
        iva=unitario*0.21
        resultado=self.precio+iva
        print(f" factura: {self.factura} \n precio: {self.precio} \n iva: {iva} \n total: {resultado}")

facturas=Contabilidad(1,"portatil hp game", 2000)
facturas.mostrar_resultado()       
