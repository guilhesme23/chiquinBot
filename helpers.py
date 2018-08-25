import requests
import os
import base64
from pprint import pprint

# Exemplo de request
r = requests.get('https://jsonplaceholder.typicode.com/posts').json()

def parse_query(query=str):
  query = query.lower().replace(' ', '+')
  return query

def get_auth():
  client_id = os.environ['CLIENT_ID']
  client_secret = os.environ['CLIENT_SECRET']
  secret = client_id + ':' + client_secret
  auth = base64.b64encode(secret.encode('utf-8'))
  headers = {'Authorization': 'Basic ' + auth.decode('utf-8')}
  auth = requests.post('https://accounts.spotify.com/api/token',data={'grant_type': 'client_credentials'},headers=headers).json()

  return auth['access_token']

def search_song(query):
  query = parse_query(query)
  auth = get_auth()
  uri = "https://api.spotify.com/v1/search"
  header = {'Authorization': 'Bearer ' + auth}

  response = requests.get(uri, {'q':query, 'type':'track', 'limit': 1}, headers=header).json()
  pprint(response)

  if not 'error' in response and response['tracks']['items']:
    result = (response['tracks']['items'][0]['name'],
              response['tracks']['items'][0]['external_urls']['spotify'])
    return result
  else:
    return ()