"""
The goal is for you to develop an interactive story in Latin.
Below is the code. 
The story is being told in English.
To begin, you should substitute your own, original Latin sentences for the English.
Do not translate the English into Latin, but be creative with vocabulary and grammar that you know.
"""

def start():
	print("You are Py, a villager of Codeia.")
	adventure = input("Do you want to go on an adventure? Type in yes or no.")

	if adventure == "yes":
		goAdventure()
  else:
    goToForest()

def goAdventure():
	where = input("Do you want to go to the forest or the mountain?")

	if where == "forest":
		goToForest()
	else:
		goToMountain()

def goToForest():
	print("You head to the dark ...")
	route = input("Do you take the long route or the short route?")

	if route == "short":
		getLost()
	else:
		goToMountain()

def goToMountain():
	print("You have reach the mountain of the ...")

def getLost():
	print("You got lost...")

# Don't forget to call the start function!
start()

