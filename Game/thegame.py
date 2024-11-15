#Imports
import sys
import time
import random
import swords
from pprint import pprint

# Create a function to roll a d20 and set it as tha variable resultd20
def roll_d20():
    return random.randint(1, 20)
D20 = roll_d20()
def roll_d10():
    return random.randint(1, 10)
D10 = roll_d10()
    
# Pick a random sword from the dictionary swords
quest_sword = random.choice(list(swords.swords.keys()))


# Print the owner value of the variable quest_sword
print("You have been tasked with finding the " + quest_sword + " owned by " + swords.swords[quest_sword]["Owner"] + ".")