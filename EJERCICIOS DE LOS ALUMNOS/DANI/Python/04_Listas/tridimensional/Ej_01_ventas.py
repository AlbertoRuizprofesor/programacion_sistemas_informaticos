ventas_3d_2 = [
                [ "PORTATIL",
                    ["ESPAÑA", 1200],
                    ["ITALIA", 1400] 
                ], 
                ["RATONES", 
                    ["PORTUGAL", 100],
                    ["FRANCIA", 400] 
                ]
            ]

print(ventas_3d_2[0]) # ['PORTATIL', ['ESPAÑA', 1200], ['ITALIA', 1400]]
print(ventas_3d_2[0][0]) # PORTATIL
print(ventas_3d_2[0][0][0]) # P
print(ventas_3d_2[0][1][0]) # ESPAÑA
print(ventas_3d_2[0][1][1]) # 1200
print(ventas_3d_2[0][2][0]) # ITALIA
print(ventas_3d_2[0][2][1]) # 1400
print(ventas_3d_2[0][2][0][0]) # I
