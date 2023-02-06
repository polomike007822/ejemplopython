import requests

# Hacer una solicitud a la API de CoinMarketCap para obtener el precio de Bitcoin
response = requests.get('https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest')

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
  # Cargar los datos en formato JSON
  data = response.json()
  # Acceder al precio de Bitcoin
  price = data['data']['quotes']['USD']['price']
  # Mostrar el precio de Bitcoin
  print('El precio de Bitcoin es: ${:.2f}'.format(price))
else:
  # Mostrar un mensaje de error si la solicitud no fue exitosa
  print('Error al obtener los datos')