from tkinter import *
from tkinter.ttk import Button
root = Tk()

#Creamos el marco
marco_principal = Frame()

#Empaquetamos el marco
marco_principal.pack()

#Redimensionamos el marco el marco
marco_principal.config(width="800", height="600")
#marco_principal.winfo_geometry()

marco_principal.config(bg ='purple')

# Create Button and add some text

button = Button(root, text = 'PRESIONA!!!!')
# pady is used for giving some padding in y direction
button.pack(side = TOP,pady = 5)
#button.config(background ='yellow')



root.mainloop()