# Simply a script to generate a loadout, no discord bot

import time
import random
import sys
import lists

ts = time.gmtime()


# Will print each character every 0.05s, and add a seperator with 0.5s delay
def slow_print_sleep(text):
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    print("-=" * 19 + "-")
    time.sleep(0.5)


print("Type 'y' to exclude items with no purchase or barter, or press enter key to include them..")
userInput = input("> ").lower().strip()
if userInput == 'y':
    if view1.value:
        for i in fir_only_armor_vests:
            del armor_vests[i]
        for i in fir_only_armor_rigs:
            del armor_rigs[i]
        for i in fir_only_helmets:
            del helmets[i]
        del rigs[fir_only_rigs]
        del backpacks[fir_only_backpacks]

# Dictionary containing all the randomized rolls
rolls = {
    "Weapon": random.choice(tuple(lists.weapons.keys())),
}

rolled_armor = random.choice(tuple(lists.armors.keys()))
if rolled_armor in lists.armor_vests:
    rolls["Armor Vest"] = rolled_armor
    rolls["Rig"] = random.choice(tuple(lists.rigs.keys()))
else:
    rolls["Armored Rig"] = rolled_armor

rolls.update({
    "Helmet": random.choice(tuple(lists.helmets.keys())),
    "Backpack": random.choice(tuple(lists.backpacks.keys())),
    "Gun mods": random.choice(tuple(lists.modifiers.keys())),
    "Ammo": random.choice(tuple(lists.modifiers.keys())),
    "Map": random.choice(tuple(lists.maps.keys())),
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
    rolled_bonus = random.choice(tuple(random.choice(lists.bonuses).keys()))
    slow_print_sleep(f"Bonus modifier: {rolled_bonus}")

    # Re-roll and print a new category of the user's choice
    if rolled_bonus == "Re-roll anything":
        def random_key(category):
            return random.choice(tuple(category.keys()))


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
