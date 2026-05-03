from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import NamedTuple

#############################
# Constants                 #
#############################

# Directories
_ITEMS_DIR = Path(__file__).parent.parent / "data" / "items"
_GAMERULES_DIR = Path(__file__).parent.parent / "data" / "gamerules"

# Weapon Types
ASSAULT_CARBINE: str = "Assault Carbine"
ASSAULT_RIFLE: str = "Assault Rifle"
SNIPER_RIFLE: str = "Bolt-Action Rifle"
MACHINE_GUN: str = "Machine Gun"
MARKSMAN_RIFLE: str = "Marksman Rifle"
PISTOL: str = "Pistol"
SMG: str = "SMG"
SHOTGUN: str = "Shotgun"
GRENADE_LAUNCHER: str = "Grenade Launcher"
MELEE: str = "Melee"

# Item Categories
WEAPON: str = "Weapon"
ARMOR_VEST: str = "Armor Vest"
ARMORED_RIG: str = "Armored Rig"
RIG: str = "Rig"
HELMET: str = "Helmet"
BACKPACK: str = "Backpack"
GUN_MOD: str = "Gun Mods"
AMMO: str = "Ammo"
MAP: str = "Map"
RANDOM_MODIFIER: str = "Random Modifier"
YOUR_CHOICE: str = "YOUR CHOICE!"

# Trader Names
PRAPOR: str = "Prapor"
THERAPIST: str = "Therapist"
SKIER: str = "Skier"
PEACEKEEPER: str = "Peacekeeper"
MECHANIC: str = "Mechanic"
RAGMAN: str = "Ragman"
JAEGER: str = "Jaeger"

# Trader Level Modifiers
LL1_TRADERS: str = "Up to level 1 traders"
LL2_TRADERS: str = "Up to level 2 traders"
LL3_TRADERS: str = "Up to level 3 traders"
LL4_TRADERS: str = "Up to level 4 traders"
NO_RESTRICTIONS: str = "No Restrictions"

# Trader Level Modifier Images
LL1_TRADERS_IMAGE: str = "https://i.imgur.com/I71LsPN.png"
LL2_TRADERS_IMAGE: str = "https://i.imgur.com/qmB6NSH.png"
LL3_TRADERS_IMAGE: str = "https://i.imgur.com/vupz2Hi.png"
LL4_TRADERS_IMAGE: str = "https://i.imgur.com/tROE6zs.png"
NO_RESTRICTIONS_IMAGE: str = "https://i.imgur.com/r5VRNUB.png"

# Images
DICE_IMAGE: str = "https://w7.pngwing.com/pngs/56/672/png-transparent-gurps-customer-service-dice-dice-throw-game-service-dice.png"
YOU_CHOOSE_IMAGE: str = (
    "https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg"
)


#############################
# Classes                   #
#############################


class Obtain(NamedTuple):
    level: 1 | 2 | 3 | 4  # Trader loyalty level
    quest_locked: bool  # Whether an item is locked behind a trader's quest or not
    barter: bool  # Whether an item is only obtainable via barter or not


@dataclass(slots=True, frozen=True)
class Item:
    name: str
    category: str
    image_url: str
    always_obtainable: bool
    meta: bool
    flea: bool
    trader_info: dict[str, list[Obtain]]


@dataclass(slots=True, frozen=True)
class GameRule:
    name: str
    category: str
    image_url: str
    meta: bool


#############################
# Functions                 #
#############################


def _parse_obtain(raw: list[dict]) -> list[Obtain]:
    return [Obtain(o["level"], o["quest_locked"], o["barter"]) for o in raw]


def _load_items(path: Path) -> tuple[Item, ...]:
    with open(path) as f:
        data = json.load(f)
    items = []
    for d in data:
        trader_info = {
            trader: _parse_obtain(obtains)
            for trader, obtains in d["trader_info"].items()
        }
        items.append(
            Item(
                name=d["name"],
                category=d["category"],
                image_url=d["image_url"],
                always_obtainable=d["always_obtainable"],
                meta=d["meta"],
                flea=d["flea"],
                trader_info=trader_info,
            )
        )
    return tuple(items)


def _load_rules(path: Path) -> tuple[GameRule, ...]:
    with open(path) as f:
        data = json.load(f)
    return tuple(GameRule(**d) for d in data)


#############################
# Weapons & Gamerules       #
#############################


class Items:
    Weapons = _load_items(_ITEMS_DIR / "weapons.json")
    ArmorVests = _load_items(_ITEMS_DIR / "armor_vests.json")
    ArmoredRigs = _load_items(_ITEMS_DIR / "armored_rigs.json")
    Rigs = _load_items(_ITEMS_DIR / "rigs.json")
    Helmets = _load_items(_ITEMS_DIR / "helmets.json")
    Backpacks = _load_items(_ITEMS_DIR / "backpacks.json")


class GameRules:
    GunMods = _load_rules(_GAMERULES_DIR / "gun_mods.json")
    Ammo = _load_rules(_GAMERULES_DIR / "ammo.json")
    Maps = _load_rules(_GAMERULES_DIR / "maps.json")
    GoodModifiers = _load_rules(_GAMERULES_DIR / "good_modifiers.json")
    OkModifiers = _load_rules(_GAMERULES_DIR / "ok_modifiers.json")
    BadModifiers = _load_rules(_GAMERULES_DIR / "bad_modifiers.json")
