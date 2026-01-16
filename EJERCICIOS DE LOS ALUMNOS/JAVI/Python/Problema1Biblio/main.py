"""
Confeccionar una aplicación que permita cargar por teclado una lista de enteros, 
obtener y mostrar el mayor y calcular su suma. Definir un módulo con las funciones
de carga, identificar el mayor y sumar. En el módulo principal del programa
importar el otro módulo y llamar a sus funciones.

Para ser un poco más ordenados crearemos una carpeta llamada proyecto1 y 
dentro de la misma crearemos los dos módulos llamados:
"""

import operacioneslista

lista=operacioneslista.cargar()
operacioneslista.imprimir_mayor(lista)
operacioneslista.imprimir_suma(lista)
