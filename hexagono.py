import turtle

# Crear una tortuga y llamarla "miTortuga"
miTortuga = turtle.Turtle()

# Dibujar un hexágono
for i in range(6):
  miTortuga.forward(100)
  miTortuga.right(60)

# Ocultar la tortuga (opcional)
miTortuga.hideturtle()

# Salir de la ventana
turtle.done()
