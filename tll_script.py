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


rolled_weapon = random.choice(tuple(weapons.keys()))
rolled_armor = random.choice(tuple(armors.keys()) + tuple(armor_rigs.keys()))
rolled_rig = random.choice(tuple(rigs.keys()))
rolled_helmet = random.choice(tuple(helmets.keys()))
rolled_backpack = random.choice(tuple(backpacks.keys()))
rolled_gun_modifiers = random.choice(modifiers)
rolled_ammo_modifiers = random.choice(modifiers)
rolled_map = random.choice(tuple(maps.keys()))
rolled_bonus = random.choice(random.choice(bonuses))

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
if rolled_armor in armors:
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
        if rolled_armor in armors:
            print("'weapon' - 'armor' - 'rig' - 'helmet' - 'backpack' - 'mods' - 'ammo' - 'map'")
        else:
            print("'weapon' - 'armoredrig' - 'helmet' - 'backpack' - 'mods' - 'ammo' - 'map'")
        user_reroll = input("> ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if user_reroll == 'weapon':
        rolled_weapon = random.choice(weapons)
        slow_print("Re-rolled weapon:", rolled_weapon)
    elif user_reroll == 'armoredrig':
        rolled_armor = random.choice(armor_rigs)
        slow_print("Re-rolled armored rig:", rolled_armor)
    elif user_reroll == 'armor':
        rolled_armor = random.choice(armors)
        slow_print("Re-rolled armor:", rolled_armor)
    elif user_reroll == 'rig':
        rolled_rig = random.choice(rigs)
        slow_print("Re-rolled rig:", rolled_rig)
    elif user_reroll == 'helmet':
        rolled_helmet = random.choice(helmets)
        slow_print("Re-rolled helmet:", rolled_helmet)
    elif user_reroll == 'backpack':
        rolled_backpack = random.choice(backpacks)
        slow_print("Re-rolled backpack:", rolled_backpack)
    elif user_reroll == 'mods':
        rolled_gun_modifiers = random.choice(modifiers)
        slow_print("Re-rolled gun mods:", rolled_gun_modifiers)
    elif user_reroll == 'ammo':
        rolled_ammo_modifiers = random.choice(modifiers)
        slow_print("Re-rolled ammo:", rolled_ammo_modifiers)
    elif user_reroll == 'map':
        rolled_map = random.choice(maps)
        slow_print("Re-rolled map:", rolled_map)
    if rolled_bonus == "Re-roll anything":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
