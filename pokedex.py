import requests

poke_name=input("What Pokemon did you want to learn about? ").lower()

poke_api= f"https://pokeapi.co/api/v2/pokemon/{poke_name}/"

poke_json= requests.get(poke_api)

poke_json= poke_json.json()

print(poke_json)
