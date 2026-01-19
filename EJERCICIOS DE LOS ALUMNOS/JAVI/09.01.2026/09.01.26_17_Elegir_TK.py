import tkinter as tk


def obtener_numeros():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        resultado.set("❌ Introduce números válidos")
        return None


def sumar():
    nums = obtener_numeros()
    if nums:
        resultado.set(nums[0] + nums[1])


def restar():
    nums = obtener_numeros()
    if nums:
        resultado.set(nums[0] - nums[1])


def multiplicar():
    nums = obtener_numeros()
    if nums:
        resultado.set(nums[0] * nums[1])


def dividir():
    nums = obtener_numeros()
    if nums:
        if nums[1] == 0:
            resultado.set("❌ No se puede dividir entre 0")
        else:
            resultado.set(nums[0] / nums[1])


# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Tkinter")
ventana.geometry("300x300")

# Entradas
tk.Label(ventana, text="Número 1").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Número 2").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="+", width=5, command=sumar).grid(row=0, column=0)
tk.Button(frame_botones, text="-", width=5, command=restar).grid(row=0, column=1)
tk.Button(frame_botones, text="×", width=5, command=multiplicar).grid(row=1, column=0)
tk.Button(frame_botones, text="÷", width=5, command=dividir).grid(row=1, column=1)

# Resultado
resultado = tk.StringVar()
resultado.set("Resultado")

tk.Label(ventana, textvariable=resultado, font=("Arial", 14)).pack(pady=15)

ventana.mainloop()
