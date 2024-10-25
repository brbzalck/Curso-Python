### pip install requests types-requests ###
import requests

url = 'http://localhost:3333/'

response = requests.get(url)
print(response.status_code)
# print(response.headers) Pegando os h1-h6 do site
# print(response.content) Pegando(em bytes) o conteúdo do site
print(response.text) # Pegando o html em si do site
