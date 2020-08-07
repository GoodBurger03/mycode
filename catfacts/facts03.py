#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random
"""Run time code"""

def main():
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    cat_list = []

    for c in r.json()["all"]:
     cat_list.append(c.get("text"))
    print("\nHere is your daily random types of facts!") 
    print("<<<<<<<<<<<<<<<<<<00000000000000000000>>>>>>>>>>>>>>>>>>")
    print(random.choice(cat_list))
main()
