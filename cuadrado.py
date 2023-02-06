import turtle



# Crear una tortuga y llamarla "miTortuga"
miTortuga = turtle.Turtle()

# Dibujar una estrella de cinco puntas
for i in range(5):
  miTortuga.color('red')
  miTortuga.forward(300)
  miTortuga.right(144)
  

# Ocultar la tortuga (opcional)
miTortuga.hideturtle()

# Salir de la ventana
turtle.done()

