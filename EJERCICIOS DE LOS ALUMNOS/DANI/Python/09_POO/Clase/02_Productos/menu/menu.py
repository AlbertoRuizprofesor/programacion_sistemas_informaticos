# Importar
from electrodomestico.tipo.freidora import Freidora
from electrodomestico.tipo.frigorifico import  Frigorifico
from electrodomestico.tipo.lavadora import  Lavadora
from electronica.tipo.monitor import Monitor
from electronica.tipo.teclado import Teclado
from electronica.tipo.portatil import Portatil

def menu():
    print("-----MENU-----")
    print("1. Electrónica\n2. Electrodoméstico")
    opcion = int(input("¿Qué sección quieres ver? :"))
    
    # PRODUCTOS
    nombre = input("Nombre: ")
    fabricante = input("Fabricante: ")
    precio = float(input("Precio: "))
    
    # ELECTRONICA
    if opcion == 1:
        # modos = ["Gaming","Normal"]
        modo = "Gaming"
        
        print("\n-----MENU ELECTRÓNICA-----")
        print("1. Monitor\n2. Teclado\n3. Portátil")
        opcion = int(input("¿Qué sección quieres ver? :"))
        
        while True:
            match opcion:
                # MONITOR
                case 1:
                    pulgadas = 20
                    m = Monitor(nombre, fabricante, precio, modo, pulgadas)
                    m.imprimir()
                    break
                # TECLADO
                case 2:
                    ergonomico = "Si"
                    t = Teclado(nombre, fabricante, precio, modo, ergonomico)
                    t.imprimir()                    
                    break
                # PORTATIL
                case 3:
                    ram = "18GB"
                    p = Portatil(nombre, fabricante, precio, modo, ram)
                    p.imprimir() 
                    break
                case _:
                    print("Opción no valida")
                    continue
    # ELECTRODOMESTICO
    elif opcion == 2:
        consumo = "A"
        
        print("\n-----MENU ELECTRODOMESTICOS-----")
        print("1. Lavadora\n2. Frigorifico\n3. Freidora")
        opcion = int(input("¿Qué sección quieres ver? :"))
        
        while True:
            match opcion:
                # LAVADORA
                case 1:
                    tipo_carga = 7
                    l = Lavadora(nombre, fabricante, precio, consumo, tipo_carga)
                    l.imprimir()
                    break
                # FRIGORIFICO
                case 2:
                    tipo = "Enfria"
                    f = Frigorifico(nombre, fabricante, precio, consumo, tipo)
                    f.imprimir()                    
                    break
                # FREIDORA
                case 3:
                    temp_max = 200
                    f = Freidora(nombre, fabricante, precio, consumo, temp_max)
                    f.imprimir() 
                    break
                case _:
                    print("Opción no valida")
                    continue
    else:
        print("Opción no válida")
        return None