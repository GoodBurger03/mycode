farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]





user = input ("What farm would you like to view? ")
animals = (farms[0]["agriculture"])
herd = (farms[1]["agriculture"])
school = (farms[2]["agriculture"])

if user.lower() == "NE":
   print(animals)
elif user.lower() == "W":
    print(herd)
elif user.lower() == "SE":
    print(school)
