import requests

def get_currencies() -> list:
    base_url = 'https://api.nbrb.by/exrates/currencies'
    try:
        response = requests.get(base_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise f'HTTP error: {e}'

print(get_currencies())
