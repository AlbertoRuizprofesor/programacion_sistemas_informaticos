from datetime import datetime, timedelta

# Simulamos las tareas con fechas dinámicas para que siempre funcione
hoy = datetime.today().date()
ayer = (hoy - timedelta(days=1)).strftime("%Y-%m-%d")
mañana = (hoy + timedelta(days=2)).strftime("%Y-%m-%d")
mes_que_viene = (hoy + timedelta(days=30)).strftime("%Y-%m-%d")

tareas = [
    {"descripcion": "Práctica de Python (Ayer)", "fecha": ayer},
    {"descripcion": "Examen de Matemáticas (Mañana)", "fecha": mañana},
    {"descripcion": "Vacaciones (Mes que viene)", "fecha": mes_que_viene},
]

proximos_7 = hoy + timedelta(days=7)

print(f"--- Agenda del día: {hoy} ---")

for tarea in tareas:
    # Convertimos el texto "YYYY-MM-DD" a un objeto de fecha real
    fecha = datetime.strptime(tarea["fecha"], "%Y-%m-%d").date()
    
    if fecha < hoy:
        print(f" Vencida: {tarea['descripcion']} (fue el {fecha})")
    elif hoy <= fecha <= proximos_7:
        print(f" Próxima (7 días): {tarea['descripcion']} (es el {fecha})")
    else:
        print(f" Lejana: {tarea['descripcion']} (falta mucho: {fecha})")