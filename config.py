import requests


def pegar_token():
    CLIENT_ID = 1542604859761144
    CLIENT_SECRET = 'pETn3JUznXc09c7YXOwNDobDoMxfYuSW'
    REDIRECT_URI = 'https://projetopython.mercadolivre'
    authorization_code = 'TG-672aa6ddee308c0001fd3bd3-1663176826'

    token_url = "https://api.mercadolivre.com/oauth/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(token_url, data=data)
    token_data = response.json()
    access_token = token_data['access_token']

    return access_token
