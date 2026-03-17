# Ejercicio 8. Gestión de inventario

def añadir_item(almacen, titulo, coste, unidades):
    almacen.append({"titulo": titulo, "coste": coste, "unidades": unidades})

def localizar_item(almacen, titulo):
    for item in almacen:
        if item["titulo"].lower() == titulo.lower():
            return item
    return None

def valor_inventario(almacen):
    acumulado = 0
    for item in almacen:
        acumulado += item["coste"] * item["unidades"]
    return acumulado

def unidades_bajas(almacen, minimo=5):
    return [x for x in almacen if x["unidades"] < minimo]


# --- PRUEBA ---
almacen = []
añadir_item(almacen, "Monitor", 120.0, 2)
añadir_item(almacen, "Altavoces", 35.0, 10)

print(localizar_item(almacen, "monitor"))
print(valor_inventario(almacen))
print(unidades_bajas(almacen))
