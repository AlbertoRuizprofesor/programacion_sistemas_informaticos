# Ejercicio 17. Gestor de tareas

from datetime import datetime, timedelta

pendientes = [
    {"texto": "Enviar informe", "limite": "2026-03-18"},
    {"texto": "Preparar presentación", "limite": "2026-03-10"},
]

hoy = datetime.today().date()
semana = hoy + timedelta(days=7)

for tarea in pendientes:
    fecha_limite = datetime.strptime(tarea["limite"], "%Y-%m-%d").date()

    if fecha_limite < hoy:
        print("Atrasada:", tarea["texto"])
    elif hoy <= fecha_limite <= semana:
        print("Próxima:", tarea["texto"])
