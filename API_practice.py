#!/usr/bin/env python3
import requests


r = requests.get("http://api.open-notify.org/astros.json")
astros = r.json()   
   

print("People in space: ", astros['number'])

for x in astros["people"]:
    print(f"{x['name']} is on the {x['craft']}")


main()
