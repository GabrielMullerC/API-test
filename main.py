import requests

def fetch_data(endpoint, filters={}):
    url = f'https://rickandmortyapi.com/api/{endpoint}'
    response = requests.get(url, params=filters)
    
    return response.json() if response.status_code == 200 else none


characters = fetch_data("character", filters={"name": "Rick"})

if characters:
    print("Characters fetched successfully!")
else:
    print("Failed to fetch characters.")

print(characters)