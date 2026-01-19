class Dado:
    def __init__(self):
        from random import randint
        self.valor = randint(1,6)

    def tirar(self):
        valores = []
        for x in range(3):
            valores.append(self.valor)
        return valores

    def imprimir(self):
        v = self.tirar()
        if v[0] == v[1] and v[0] == v[2]:
            print("Has ganado")
        else:
            print("Has perdido")

