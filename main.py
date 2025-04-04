print("Hola Mundo")

import requests

response = requests.get("https://api.github.com")
print("Estado de la API de GitHub:", response.status_code)
