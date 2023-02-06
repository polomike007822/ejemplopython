from tabulate import tabulate

paises = [["Argentina"], ["Bolivia"], ["Chile"], ["Colombia"], ["Costa Rica"], ["Cuba"], ["Ecuador"], ["El Salvador"], ["España"], ["Guatemala"], ["Honduras"], ["México"], ["Nicaragua"], ["Panamá"], ["Paraguay"], ["Perú"], ["Puerto Rico"], ["República Dominicana"], ["Uruguay"], ["Venezuela"]]

# Añadir un número de índice a cada fila de la tabla
for i, pais in enumerate(paises):
  pais.insert(0, i+1)

print(tabulate(paises, headers=["Índice", "Países de habla hispana"]))