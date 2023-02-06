import requests
import io
from PIL import Image
from tabulate import tabulate
from urllib.request import urlretrieve

# Crear una lista de países y banderas
paises = [   
    ["Argentina", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/1200px-Flag_of_Argentina.svg.png"],
    ["Chile", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/1200px-Flag_of_Chile.svg.png"],
    ["Colombia", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/1200px-Flag_of_Colombia.svg.png"],
    ["Cuba", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Flag_of_Cuba.svg/1200px-Flag_of_Cuba.svg.png"],
    ["Ecuador", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/1200px-Flag_of_Ecuador.svg.png"],
    ["El Salvador", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_El_Salvador.svg/1200px-Flag_of_El_Salvador.svg.png"],
    ]

# Añadir un número de índice a cada fila de la tabla
for i, pais in enumerate(paises):
  pais.insert(0, i+1)

# Crear una tabla con número de índice, nombre de país y bandera
tabla = []
for fila in paises:
  indice = fila[0]
  nombre = fila[1]
  #enlace = fila[2]
  # Descargar la imagen de la bandera a partir de la URL y crear un objeto BytesIO a partir de los datos de la imagen
  response = requests.get(fila[2])
  #print(response.content)  
  bandera = Image.open(io.BytesIO(response.content))
  #print(bandera.format)
  tabla.append([indice, nombre, bandera])

# Imprimir la tabla
print(tabulate(tabla, headers=["Índice", "Países de habla hispana", "Bandera"]))

# Mostrar las imágenes de las banderas
for fila in tabla:
  fila[2].show()