import tkinter as tk


def mostrar_tabla():
    try:
        tabla = int(entrada.get())
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, f"TABLA DEL {tabla}\n\n")

        for i in range(0, 13):
            resultado = tabla * i
            texto_resultado.insert(tk.END, f"{tabla} x {i} = {resultado}\n")
    except ValueError:
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, "Por favor, introduce un número válido.")


# Ventana principal
ventana = tk.Tk()
ventana.title("Tabla de multiplicar")
ventana.geometry("300x350")

# Etiqueta
label = tk.Label(
    ventana, text="Elige la tabla de multiplicar de un número:", wraplength=250
)
label.pack(pady=10)

# Entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Mostrar tabla", command=mostrar_tabla)
boton.pack(pady=10)

# Área de texto
texto_resultado = tk.Text(ventana, height=12, width=30)
texto_resultado.pack(pady=5)

ventana.mainloop()
