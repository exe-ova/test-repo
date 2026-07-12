import requests

def get_currencies():
    base_url = 'https://api.nbrb.by/exrates/currencies'
    try:
        response = requests.get(base_url, timeout=4)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectTimeout as e:
        print(f'ConnectTimeout error: {e}')
    except requests.exceptions.ConnectionError as e:
        print(f'ConnectionError: {e}')
    except requests.exceptions.HTTPError as e:
        print(f'HTTP error: {e}')
    except Exception as e:
        print(f'Error: {e}')

print(get_currencies())
