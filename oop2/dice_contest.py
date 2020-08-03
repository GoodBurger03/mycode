from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
mulligan = Cheat_Mulligan()
extra = Cheat_Extra_Die()

swapper_score = 0
loaded_dice_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()

  swapper.cheat()
  loaded_dice.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1
  elif sum(swapper.get_dice()) > sum(mulligan.get_dice()):
   swapper_score+= 1
  elif sum(swapper.get_dice()) > sum(extra.get_dice()):
   swapper_score+= 1
  elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()):
   loaded_dice_score+= 1
  elif sum(loaded_dice.get_dice()) > sum(mulligan.get_dice()):
   loaded_dice_score+= 1
  elif sum(loaded_dice.get_dice()) > sum(extra.get_dice()):
   loaded_dice_score+= 1
  elif sum(mulligan.get_dice()) > sum(swapper.get_dice()):
   mulligan_score+= 1
  elif sum(mulligan.get_dice()) > sum(loaded_dice.get_dice()):
   mulligan_score+= 1
  elif sum(mulligan.get_dice()) > sum(extra.get_dice()):
   mulligan_score+= 1
  elif sum(extra.get_dice()) > sum(swapper.get_dice()):
   extra_score+= 1
  elif sum(extra.get_dice()) > sum(loaded_dice.get_dice()):
   extra_score+= 1
  elif sum(extra.get_dice()) > sum(mulligan.get_dice()):
   extra_score+= 1
  else:
    pass 
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")

