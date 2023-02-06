from tabulate import tabulate

paises = [["Argentina"], ["Bolivia"], ["Chile"], ["Colombia"], ["Costa Rica"], ["Cuba"], ["Ecuador"], ["El Salvador"], ["España"], ["Guatemala"], ["Honduras"], ["México"], ["Nicaragua"], ["Panamá"], ["Paraguay"], ["Perú"], ["Puerto Rico"], ["República Dominicana"], ["Uruguay"], ["Venezuela"]]

print(tabulate(paises, headers=["Países de habla hispana"]))