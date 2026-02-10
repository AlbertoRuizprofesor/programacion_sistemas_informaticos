ventas_3d_2 = [
    [  # Z0: PORTATIL
        ["ESPAÑA", 1200], # Y0
        ["ITALIA", 1400]  # Y1
    ],
    [  # Z1: RATONES
        ["ESPAÑA", 500],  # Y0
        ["ITALIA", 400]   # Y1
    ],
    [  # Z2: MONITORES (Nuevo elemento)
        ["ESPAÑA", 800],  # Y0
        ["ITALIA", 700]   # Y1
    ]
]

productos = ["PORTATIL", "RATONES", "MONITORES"]

# --- ACCESO A DATOS ---

# Bloque PORTATIL
print(f"--- {productos[0]} ---")
print(ventas_3d_2[0][0][0], ":", ventas_3d_2[0][0][1])  # ESPAÑA: 1200
print(ventas_3d_2[0][1][0], ":", ventas_3d_2[0][1][1])  # ITALIA: 1400

# Bloque RATONES
print(f"\n--- {productos[1]} ---")
print(ventas_3d_2[1][0][0], ":", ventas_3d_2[1][0][1])  # ESPAÑA: 500
print(ventas_3d_2[1][1][0], ":", ventas_3d_2[1][1][1])  # ITALIA: 400

# Bloque MONITORES (Acceso al nuevo elemento)
print(f"\n--- {productos[2]} ---")
print(f"País: {ventas_3d_2[2][0][0]} | Venta: {ventas_3d_2[2][0][1]}") # ESPAÑA: 800
print(f"País: {ventas_3d_2[2][1][0]} | Venta: {ventas_3d_2[2][1][1]}") # ITALIA: 700