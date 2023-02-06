from tabulate import tabulate
from tkinter import Tk, Label, Frame, Scrollbar, Listbox

# Crear una lista de países y banderas
paises = [    ["Argentina", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/1200px-Flag_of_Argentina.svg.png"],
    ["Bolivia", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Flag_of_Bolivia.svg/1200px-Flag_of_Bolivia.svg.png"],
    ["Chile", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/1200px-Flag_of_Chile.svg.png"],
    ["Colombia", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/1200px-Flag_of_Colombia.svg.png"],
    ["Costa Rica", "https://upload.wikimedia.org/wikipedia/commons/thumb/bc/Flag_of_Costa_Rica(state).svg/1200px-Flag_of_Costa_Rica(state).svg.png"],
    ["Cuba", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Flag_of_Cuba.svg/1200px-Flag_of_Cuba.svg.png"],
    ["Ecuador", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/1200px-Flag_of_Ecuador.svg.png"],
    ["El Salvador", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_El_Salvador.svg/1200px-Flag_of_El_Salvador.svg.png"],]

# Añadir un número de índice a cada fila de la tabla
for i, pais in enumerate(paises):
  pais.insert(0, i+1)

# Crear la ventana principal
ventana = Tk()
ventana.title("Países de habla hispana")

# Crear un marco para contener la tabla
marco = Frame(ventana)
marco.pack()

# Crear un widget de lista para mostrar la tabla
lista = Listbox(marco, width=60)
lista.pack(side="left")

# Añadir los datos de la tabla al widget de lista
for fila in tabulate(paises, headers=["Índice", "Países de habla hispana", "Bandera"]).split("\n"):
  lista.insert("end", fila)

# Crear una barra de desplazamiento para el widget de lista
barra = Scrollbar(marco, orient="vertical")
barra.config(command=lista.yview)
barra.pack(side="right", fill="y")
lista.config(yscrollcommand=barra.set)

# Mostrar la ventana
ventana.mainloop()
