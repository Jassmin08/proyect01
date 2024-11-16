import tkinter as tk

# Función para actualizar la entrada
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Eliminar el texto actual
    entry.insert(tk.END, current + value)

# Función para calcular el resultado
def calculate():
    try:
        result = eval(entry.get())  # Evaluar la expresión matemática
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Función para borrar la entrada
def clear():
    entry.delete(0, tk.END)

# Función para abrir la ventana de frases motivadoras
def open_motivational_quotes():
    # Crear una nueva ventana para las frases
    quotes_window = tk.Toplevel(root)
    quotes_window.title("Frases Motivadoras")
    
    # Configurar fondo negro para la ventana emergente
    quotes_window.config(bg="#000000")
    
    # Frases motivadoras
    phrases = [
        "El único modo de hacer un gran trabajo es amar lo que haces.",
        "La vida es 10% lo que te sucede y 90% cómo reaccionas a ello.",
        "No te rindas, cada fracaso es un paso hacia el éxito.",
        "La perseverancia es la clave del éxito.",
        "Cree en ti mismo y todo será posible."
    ]
    
    # Crear etiquetas para las frases y añadirlas a la ventana
    for phrase in phrases:
        tk.Label(quotes_window, text=phrase, font=("Arial", 12), fg="#32CD32", padx=10, pady=10, bg="#000000").pack()

    # Botón de regreso para cerrar la ventana emergente
    tk.Button(quotes_window, text="Atrás", font=("Arial", 12), bg="#FF66B2", fg="white", 
              command=quotes_window.destroy).pack(pady=10)

    # Ajustar el tamaño de la ventana a las frases (sin tamaño fijo)
    quotes_window.update_idletasks()  # Necesario para obtener el tamaño correcto después de agregar widgets
    quotes_window.geometry(f"{quotes_window.winfo_width()}x{quotes_window.winfo_height()}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Configuración de la ventana principal
root.config(bg="#000000")  # Fondo negro
root.geometry("400x500")  # Tamaño de la ventana

# Configuración de la entrada
entry = tk.Entry(root, font=("Arial", 24), bg="#000000", fg="#FF0000", bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora con un corazón en cada número
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)  # Botón de Clear
]

# Crear los botones y añadirlos a la ventana
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), width=6, height=2, 
                       bg="#FF66B2", fg="white", bd=3, relief="ridge", 
                       activebackground="#FF3385", command=lambda t=text: button_click(t) if t != "=" and t != "C" else calculate() if t == "=" else clear())
    button.grid(row=row, column=col, padx=5, pady=5)

# Botón para abrir la ventana de frases motivadoras
frases_button = tk.Button(root, text="Frases", font=("Arial", 18), width=6, height=2,
                          bg="#FF66B2", fg="white", bd=3, relief="ridge",
                          activebackground="#FF3385", command=open_motivational_quotes)
frases_button.grid(row=5, column=1, padx=5, pady=5)  # Al lado del botón C

# Ejecutar la ventana principal
root.mainloop()
