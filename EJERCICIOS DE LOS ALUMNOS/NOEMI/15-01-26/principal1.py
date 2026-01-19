from mayormenor import mayor #Desde el archivo mayormenor.py, importa solo la función mayor
                            #  esto "from mayormenor import mayor as Mayormenor" dice “Importa la función mayor del archivo mayormenor.py, pero llámala Mayormenor en este archivo”
                            
valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese el segundo valor: "))
print("El mayor de los valores es ",mayor(valor1,valor2))