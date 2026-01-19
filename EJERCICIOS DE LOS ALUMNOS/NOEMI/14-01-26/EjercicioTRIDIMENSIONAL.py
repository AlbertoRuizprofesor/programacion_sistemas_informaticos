#Ejercicio tabla cercana TRIDIMENSIONAL pura: añadir un producto.

ventas_3d_2= [
        [   #codigo 0: portatil
            ["España", 1200],
            ["Italia", 1400]
        ],


        [   
            #codigo 1: ratones
             ["España", 1500], #codigo 0 (0: españa, 1:1500)
             ["Italia", 1500]  #codigo 1 (0: italia, 1:400)
        ],

    [
         #codigo 2: pantallas
            ["España", 1300], 
            ["Italia", 300]
    ],
    


    [ #codigo 3: tarjeta grafica
        ["España", 400],
        ["Italia", 200]
    ]

]
productos=["Potatil","ratones","pantallas","tarjeta grafica"]

print(productos[0])   #imprime "portatil"
print(ventas_3d_2[0][0][0]) #imprime "España"
print("prueba", ventas_3d_2[0][0])  
print(ventas_3d_2[0][0][1]) #imprime "1300"
print(ventas_3d_2[0][1][0])  # Imprime "ITALIA"
print(ventas_3d_2[0][1][1])  # Imprime "1400"
print(productos[1])  # Imprime "RATONES"
print(ventas_3d_2[1][0][0])  # Imprime "ESPAÑA"
print(ventas_3d_2[1][0][1])  # Imprime "1500"    
print(ventas_3d_2[1][1][0])  # Imprime "ITALIA"
print(ventas_3d_2[1][1][1])  # Imprime "1500"
print(productos[2]) #imprime "PANTALLAS"
print(ventas_3d_2[2][0][0])   #imprime "España"
print(ventas_3d_2[2][0][1])   #imprime "1300"
print(ventas_3d_2[2][1][0])   #imprime "ITALIA"
print(ventas_3d_2[2][1][1])  #imprime "300"
print(productos[3]) #imprime "tarjeta grafica"
print(ventas_3d_2[3][0][0])  #imprime "ESPAÑA"
print(ventas_3d_2[3][0][1])   #imprime "400"
print(ventas_3d_2[3][1][0])  #imprime "ITALIA"
print(ventas_3d_2[3][1][1])  #imprime "200"
