import requests

def get_currencies():
    base_url = 'https://api.nbrb.by/exrates/currencies'

    response = requests.get(base_url, timeout=5)

    return response.json()

print(get_currencies())
