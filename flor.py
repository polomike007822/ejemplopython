import turtle


# Crear una tortuga y llamarla "miTortuga"
miTortuga = turtle.Turtle()

# Dibujar un trébol de cuatro hojas
for i in range(4):
  miTortuga.color("green") 
  miTortuga.forward(100)
  miTortuga.right(60)
  miTortuga.forward(100)
  miTortuga.right(120)
  miTortuga.forward(100)
  miTortuga.right(60)
  miTortuga.forward(100)
  miTortuga.right(30)

# Ocultar la tortuga (opcional)
miTortuga.hideturtle()

# Salir de la ventana
turtle.done()
