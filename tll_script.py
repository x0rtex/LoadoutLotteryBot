# This is a script that will generate a loadout in Python's command line - no discord bot.

import time
import random
import sys

from lists import *

ts = time.gmtime()
user_reroll = ""


def slow_print(prefix, suffix):
    for i in (prefix + ' ' + suffix):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()


rolled_weapon = random.choice(weapon_list)
rolled_armor = random.choice(armor_list + armor_rig_list)
rolled_rig = random.choice(rig_list)
rolled_helmet = random.choice(helmet_list)
rolled_backpack = random.choice(backpack_list)
rolled_gun_modifiers = random.choice(modifier_list)
rolled_ammo_modifiers = random.choice(modifier_list)
rolled_map = random.choice(map_list)
rolled_bonus = random.choice(random.choice(bonus_list))

print("Welcome to Tarkov Loadout Lottery")
time.sleep(0.5)
input("Press enter to roll your loadout... ")
print("")
slow_print(time.strftime("%x %X", ts), "")
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Weapon:", rolled_weapon)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
# Armor can be worn with a rig, armored rig cannot be worn with an individual rig/armor
if rolled_armor in armor_list:
    slow_print("Armor:", rolled_armor)
    time.sleep(0.5)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(0.5)
    slow_print("Rig:", rolled_rig)
else:
    slow_print("Armored Rig:", rolled_armor)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Helmet:", rolled_helmet)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Backpack:", rolled_backpack)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Gun Mods:", rolled_gun_modifiers)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Ammo:", rolled_ammo_modifiers)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)
slow_print("Map:", rolled_map)
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)

userInput = input("\nType 'y' to roll bonus modifier, or press enter... ")
time.sleep(0.5)
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.5)

if userInput.upper() == "Y":
    slow_print("Bonus modifier:", rolled_bonus)
    time.sleep(0.5)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(0.5)

    if rolled_bonus == "Re-roll anything":
        print("Select one of the following to re-roll...")
        if rolled_armor in armor_list:
            print("'weapon' - 'armor' - 'rig' - 'helmet' - 'backpack' - 'mods' - 'ammo' - 'map'")
        else:
            print("'weapon' - 'armoredrig' - 'helmet' - 'backpack' - 'mods' - 'ammo' - 'map'")
        user_reroll = input("> ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user_reroll == 'weapon':
        rolled_weapon = random.choice(weapon_list)
        slow_print("Re-rolled weapon:", rolled_weapon)
    elif user_reroll == 'armoredrig':
        rolled_armor = random.choice(armor_rig_list)
        slow_print("Re-rolled armored rig:", rolled_armor)
    elif user_reroll == 'armor':
        rolled_armor = random.choice(armor_list)
        slow_print("Re-rolled armor:", rolled_armor)
    elif user_reroll == 'rig':
        rolled_rig = random.choice(rig_list)
        slow_print("Re-rolled rig:", rolled_rig)
    elif user_reroll == 'helmet':
        rolled_helmet = random.choice(helmet_list)
        slow_print("Re-rolled helmet:", rolled_helmet)
    elif user_reroll == 'backpack':
        rolled_backpack = random.choice(backpack_list)
        slow_print("Re-rolled backpack:", rolled_backpack)
    elif user_reroll == 'mods':
        rolled_gun_modifiers = random.choice(modifier_list)
        slow_print("Re-rolled gun mods:", rolled_gun_modifiers)
    elif user_reroll == 'ammo':
        rolled_ammo_modifiers = random.choice(modifier_list)
        slow_print("Re-rolled ammo:", rolled_ammo_modifiers)
    elif user_reroll == 'map':
        rolled_map = random.choice(map_list)
        slow_print("Re-rolled map:", rolled_map)
    if rolled_bonus == "Re-roll anything":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
