# Script version, no discord bot. Only uses lists.py

import time
import random
import sys
from lists import *

ts = time.gmtime()


# Will print each character every 0.05s, and add a seperator with 0.5s delay
def slow_print_sleep(text):
    for i in text:
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    print("-=" * 19 + "-")
    time.sleep(0.5)


# Dictionary containing all the randomized rolls
rolls = {
    "Weapon": random.choice(tuple(weapons.keys())),
}

rolled_armor = random.choice(tuple(armors.keys()))
if rolled_armor in armor_vests:
    rolls["Armor Vest"] = rolled_armor
    rolls["Rig"] = random.choice(tuple(rigs.keys()))
else:
    rolls["Armored Rig"] = rolled_armor

rolls.update({
    "Helmet": random.choice(tuple(helmets.keys())),
    "Backpack": random.choice(tuple(backpacks.keys())),
    "Gun mods": random.choice(modifiers),
    "Ammo": random.choice(modifiers),
    "Map": random.choice(tuple(maps.keys())),
})

# Prints all rolls categories
print("Welcome to Tarkov Loadout Lottery")
time.sleep(0.5)
input("Press enter to roll your loadout... ")
slow_print_sleep(f"\n{time.strftime('%x %X', ts)}")
for roll in rolls:
    slow_print_sleep(f"{roll}: {rolls[roll]}")

# User given the option to roll an optional bonus modifier from list
print("Type 'y' to roll optional bonus modifier, or press enter to quit...")
userInput = input("> ").lower().strip()
time.sleep(0.5)
print("-=" * 19 + "-")
time.sleep(0.5)
if userInput == "y":
    rolled_bonus = random.choice(random.choice(bonuses))
    slow_print_sleep(f"Bonus modifier: {rolled_bonus}")

    # Re-roll and print a new category of the user's choice
    if rolled_bonus == "Re-roll anything":
        def random_key(x):
            return random.choice(tuple(x.keys()))
        print("Select one of the following to re-roll...")
        print(", ".join(rolls.keys()))
        user_reroll = ""
        while user_reroll not in rolls:
            user_reroll = input("> ").title().strip()
            if user_reroll not in rolls:
                print("Invalid input, try again.")
        print("-=" * 19 + "-")
        rolls[user_reroll] = random_key(all[user_reroll])
        slow_print_sleep(f"Re-rolled {user_reroll.lower()}: {rolls[user_reroll]}")
