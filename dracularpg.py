#!/usr/bin/python3

import dice
import random
from subprocess import call
from random import randint



hunters = [
  {
    "name": "Van Helsing",
    "health": 15,
    "damage": "1d8"
  },
  {
    "name": "Vampire hunter",
    "health": 10,
    "damage": "1d4"
  },
  {
    "name": "Vampire Succubus",
    "health": 5,
    "damage": "1d10"
  }
]

player_health = 25
inventory = []
spells = [
 {
  'name' : 'Hypnotize',
  'damage' : '2d6'
 },
 {
    'name' : 'Drain',
    'damage' : '5d8'
 }
]

spell_book = []


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
  cast [spell]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

#current_health = 200.00
#maxHealth = 200    # Max Health
#healthDashes = 20  # Max Displayed dashes
#def health_bar():
 # dashConvert = int(maxHealth/healthDashes)
 # currentDashes = int(current_health/dashConvert)
 # remainingHealth = healthDashes - currentDashes

 # DisplayHealth = '-' * currentDashes
  #leftover = ' ' * remainingHealth
  #percent = str(int((current_health/maxHealth)*100)) + "%"

 # print("|" + DisplayHealth + leftover + "|")
 # print("         " + percent)



def combat():
    foe_ID = randint(0,2)

    global player_health, inventory, spells, hunters
    round = 1
    foe_health = hunters[foe_ID]['health']

    print(f"You have run into {hunters[foe_ID]['name']} be careful! A DUEL IS ABOUT TO BEGIN!\n")
    while True:
        print(f"Round {round}")
        print("The Players Health is: [" + str(player_health) + "]")
        print("The Monsters Health is: [" + str(foe_health) + "]")

        print("Would you like to Cast your [spell] or use your potion [item]")
        move =  input().lower().split()
        if move[0] == 'use':  #
            if move[1] in inventory:  # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(f"You hit a {hunters[foe_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

def ReplaceItem(item,changeto, inventory):
    inventory = inventory
    inventory.remove(item)
    for i in range(len(inventory)-len(inventory)):
        inventory.append(changeto)
    return inventory


# an inventory, which is initially empty

def random_encounter():
    if((int(rooms[currentRoom]['tele'])) + 5) >= 20:
        combat()
# a dictionary linking a room to other rooms

rooms = {

       'Main Entrance': {
        'south': 'Observatory ',
        'east': 'Chapel',
        'item': 'vile of blood'
#        'tele': '0',
 #       'desc': 'This is the entrance to the castle, be careful it has been a long time since you have been home'
        },

        'Observatory ' : {
        'north': 'Main Entrance',
        'item': 'Vampire hunter',
        'spells': 'Silver Haze'
#        'tele': '0',    # Ask why the error invalid syntax keeps popping up fr this
        },
        'Chapel': {
        'west': 'Main Entrance',
        'south': 'Clock Tower',
        'item': 'coffin'
#        'tele': '0',
        }
        'Clock Tower' : {
        'north': 'Chapel'
        }
}

# start the player in the Main Entrance
currentRoom = 'Main Entrance'

showInstructions()

# loop forever
while True:

    showStatus()
#    health_bar()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            random_encounter()
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
        # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'use':
        # if inventory contains item
         if move[1] in inventory:
        # display a helpful message
            print(move[1] + ' used')
        # delete the item from the room

        # otherwise, if the item isn't there to get
         else:
        # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## Define how a player can win
         if currentRoom == 'Clock Tower' and 'Silver Haze Spell' in inventory and 'coffin' in inventory:
             print('You escaped the house with the ultra rare key and magic coffin... YOU WIN!')
             break
