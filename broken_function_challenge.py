#!/usr/bin/env python3
import random

num= int(input("How many Shakespearean insults would you like?"))

insult_list= open("/home/student/mycode/insults.txt", "r")
insult= insult_list.readlines()

def insult_generator(num):
    print("You are a", end="")
    for x in range(num):
      print(random.choice(insult))

insult_generator(num)
