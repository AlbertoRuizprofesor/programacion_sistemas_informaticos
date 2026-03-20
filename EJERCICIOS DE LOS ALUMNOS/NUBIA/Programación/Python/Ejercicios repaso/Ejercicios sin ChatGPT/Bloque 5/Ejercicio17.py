'''
Crea una estructura para guardar tareas con descripción y fecha límite. 
Muestra cuáles están vencidas y cuáles vencen en los próximos 7 días. 
Idea clave: Usa datetime. 
'''

from datetime import datetime, timedelta

tareas = [
    {"descripcion": "Entregar deberes", "fecha_limite": datetime(2026, 3, 18)},
    {"descripcion": "Estudiar examen", "fecha_limite": datetime(2026, 3, 18)},
    {"descripcion": "Pagar matrícula", "fecha_limite": datetime(2026, 3, 25)}
]

hoy = datetime.today().date()
proxima_semana = hoy + timedelta(days=7)

for tarea in tareas:
    fecha_limite = tarea["fecha_limite"].date()
    if fecha_limite < hoy:
        print(f"Tarea vencida: {tarea['descripcion']} (Fecha límite: {fecha_limite})")
    elif hoy < fecha_limite <= proxima_semana:
        print(f"Tarea próxima a vencer: {tarea['descripcion']} (Fecha límite: {fecha_limite})")
    elif fecha_limite == hoy:
        print(f"La tarea vence hoy: {tarea['descripcion']}")