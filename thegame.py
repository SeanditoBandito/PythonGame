#Imports
import sys
from time import sleep
import random
import swords
import tomes
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
sleep(2)
print("You set out on your journey to find the " + quest_sword + ".")
sleep(2)
print("You come across a tome that may hold the secret to finding the " + quest_sword + ".")
sleep(2)
print("Do you want to pick up the tome?")
tome_decision = input("Yes or No: ")

if tome_decision == "Yes":
    print("You pick up the tome and open it.")
    sleep(2)
    print("The tome reads: " + tomes.tomes[quest_sword])
    sleep(2)
    print("You close the tome and continue on your journey.")
    sleep(2)
else:
    print("You leave the tome and continue on your journey.")
    sleep(2)

