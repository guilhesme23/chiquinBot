import requests
import os
import base64
from pprint import pprint


class SpotifyConnector(object):
    def __init__(self):
        self.client_id = os.environ['CLIENT_ID']
        self.client_secret = os.environ['CLIENT_SECRET']

    def parse_query(self, query=str):
        query = query.lower().replace(' ', '+')
        return query

    def get_auth(self):
        client_id = os.environ['CLIENT_ID']
        client_secret = os.environ['CLIENT_SECRET']
        secret = client_id + ':' + client_secret
        auth = base64.b64encode(secret.encode('utf-8'))
        headers = {'Authorization': 'Basic ' + auth.decode('utf-8')}
        auth = requests.post(
            'https://accounts.spotify.com/api/token',
            data={'grant_type': 'client_credentials'},
            headers=headers).json()
        return auth['access_token']

    def search_song(self, query):
        query = self.parse_query(query)
        auth = self.get_auth()
        uri = "https://api.spotify.com/v1/search"
        header = {'Authorization': 'Bearer ' + auth}

        response = requests.get(
            uri,
            {'q': query, 'type': 'track', 'limit': 1},
            headers=header).json()
        pprint(response)

        if 'error' not in response and response['tracks']['items']:
            result = (
                response['tracks']['items'][0]['name'],
                response['tracks']['items'][0]['external_urls']['spotify'])
            return result
        else:
            return ()
