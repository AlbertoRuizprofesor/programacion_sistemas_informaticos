ventas_3d_2 =[
    [   #codigo 0: portatil
        ["ESPAÑA", 1200],
        ["ITALIA", 1400]
    ],
    [    #codigo 1: ratones
        ["ESPAÑA", 500],
        ["ITALIA", 400]
    ], 
    [    #monitores
        ["ESPAÑA", 800],
        ["ITALIA", 500]
    ]
]
productos = ["PORTATIL", "RATONES", "MONITORES"]

print(productos[0]) #Imprime "PORTATIL"
print(ventas_3d_2[0][0][0])  # Imprime "ESPAÑA"
print("prueba",ventas_3d_2[0][0])
print(ventas_3d_2[0][0][1])  # Imprime "1200"
print(ventas_3d_2[0][1][0])  # Imprime "ITALIA"
print(ventas_3d_2[0][1][1])  # Imprime "1400"
print(productos[1])  # Imprime "RATONES"
print(ventas_3d_2[1][0][0])  # Imprime "ESPAÑA"
print(ventas_3d_2[1][0][1])  # Imprime "500"    
print(ventas_3d_2[1][1][0])  # Imprime "ITALIA"
print(ventas_3d_2[1][1][1])  # Imprime "400"

