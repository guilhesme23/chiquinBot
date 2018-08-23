import requests
# Credencial API Youtube: AIzaSyChsmJaCAVJ9uo7gRc5QC1wJWm1mUhOZ-M
# Exemplo de request
r = requests.get('https://jsonplaceholder.typicode.com/posts').json()

def search_song(query=str):
  query = query.lower().replace(' ', '+')
  return query
