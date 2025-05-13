import customtkinter as ctk
from tkinter import StringVar


def guardar_datos():
    print("Tipo de cuota:", tipo_var.get())
    print("Tipo de plazo:", plazo_var.get())


ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("800x600")
app.title("Formulario de Cuotas")

ventana_datos = ctk.CTkFrame(master=app)
ventana_datos.pack(padx=40, pady=40)
tipo_var = StringVar(value="Contado")
plazo_var = StringVar(value="Regulares")

label_tipo = ctk.CTkLabel(ventana_datos, text="Tipo de cuota:")
opcion_tipo = ctk.CTkOptionMenu(
    ventana_datos, variable=tipo_var, values=["Contado", "Crédito"]
)

label_plazo = ctk.CTkLabel(ventana_datos, text="Tipo de plazo:")
opcion_plazo = ctk.CTkOptionMenu(
    ventana_datos, variable=plazo_var, values=["Regulares", "Irregulares"]
)

button = ctk.CTkButton(ventana_datos, text="Guardar", command=guardar_datos)
button.grid(row=2, column=0, columnspan=2, pady=20)


label_tipo.grid(row=0, column=0, padx=10, pady=10, sticky="e")
opcion_tipo.grid(row=0, column=1, padx=10, pady=10, sticky="w")
label_plazo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
opcion_plazo.grid(row=1, column=1, padx=10, pady=10, sticky="w")


frame_tabla = ctk.CTkFrame(app)
frame_tabla.pack(pady=20, padx=20)

filas = 2
columnas = 2
celdas = []  # Para guardar los widgets si necesitás acceder a ellos luego

for i in range(filas):
    fila_actual = []
    for j in range(columnas):
        entrada = ctk.CTkEntry(
            frame_tabla, width=100, placeholder_text=f"Fila {i+1}, Col {j+1}"
        )
        entrada.grid(row=i, column=j, padx=5, pady=5)
        fila_actual.append(entrada)
    celdas.append(fila_actual)


app.mainloop()
