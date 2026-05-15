from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import NamedTuple, Self
from urllib.parse import urlparse

from typing_extensions import Literal

from config.config import settings as cfg

logger = logging.getLogger("discord")

#############################
# Constants                 #
#############################

# Directories
_ITEMS_DIR = cfg.data_dir / "items"
_GAMERULES_DIR = cfg.data_dir / "gamerules"

# Images
DICE_IMAGE: str = (
    "https://w7.pngwing.com/pngs/56/672/png-transparent-gurps-customer-service-dice-dice-throw-game-service-dice.png"
)
YOU_CHOOSE_IMAGE: str = "https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg"


#############################
# Classes                   #
#############################


class Trader(str, Enum):
    PRAPOR = "prapor"
    THERAPIST = "therapist"
    SKIER = "skier"
    PEACEKEEPER = "peacekeeper"
    MECHANIC = "mechanic"
    RAGMAN = "ragman"
    JAEGER = "jaeger"
    REF = "ref"

    @property
    def display_name(self: Self) -> str:
        return self.value.capitalize()


class TraderLevelRule(str, Enum):
    LL1 = ("Up to level 1 traders", 1)
    LL2 = ("Up to level 2 traders", 2)
    LL3 = ("Up to level 3 traders", 3)
    LL4 = ("Up to level 4 traders", 4)
    NO_RESTRICTIONS = ("No Restrictions", 0)

    level: int

    def __new__(cls, value: str, level: int):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.level = level
        return obj

    @classmethod
    def from_name(cls, name: str) -> "TraderLevelRule | None":
        try:
            return cls(name)
        except ValueError:
            return None


class Category(str, Enum):
    WEAPON = "Weapon"
    MELEE = "Melee"
    ASSAULT_CARBINE = "Assault Carbine"
    ASSAULT_RIFLE = "Assault Rifle"
    SMG = "SMG"
    SHOTGUN = "Shotgun"
    MARKSMAN_RIFLE = "Marksman Rifle"
    BOLT_ACTION = "Bolt-Action Rifle"
    PISTOL = "Pistol"
    MACHINE_GUN = "Machine Gun"
    GRENADE_LAUNCHER = "Grenade Launcher"
    ROCKET_LAUNCHER = "Rocket Launcher"
    ARMOR_VEST = "Armor Vest"
    ARMORED_RIG = "Armored Rig"
    RIG = "Rig"
    HELMET = "Helmet"
    BACKPACK = "Backpack"
    GUN_MOD = "Gun Mods"
    AMMO = "Ammo"
    MAP = "Map"
    RANDOM_MODIFIER = "Random Modifier"


class Obtain(NamedTuple):
    level: Literal[1, 2, 3, 4]  # Trader loyalty level
    quest_locked: bool  # Whether an item is locked behind a trader's quest or not
    barter: bool  # Whether an item is only obtainable via barter or not


@dataclass(slots=True, frozen=True)
class Item:
    name: str
    category: Category
    image_url: str
    always_obtainable: bool
    meta: bool
    flea: bool
    trader_info: dict[Trader, list[Obtain]]


@dataclass(slots=True, frozen=True)
class GameRule:
    name: str
    category: Category
    image_url: str
    meta: bool


#############################
# Functions                 #
#############################


def _parse_obtain(raw: list[dict]) -> list[Obtain]:
    return [Obtain(o["level"], o["quest_locked"], o["barter"]) for o in raw]


def _validate_image_url(url: str, name: str) -> str:
    """Validate image URL from JSON. Returns empty string on failure."""
    if not url or not url.strip():
        return ""

    try:
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            raise ValueError(f"No scheme or host: {url}")
    except Exception:
        logger.error(f"Invalid image URL for '{name}': '{url}'")
        return ""

    return url


def _load_items(path: Path) -> tuple[Item, ...]:
    with open(path) as f:
        data = json.load(f)
    items = []
    for d in data:
        trader_info = {Trader(trader): _parse_obtain(obtains) for trader, obtains in d["trader_info"].items() if trader}
        items.append(
            Item(
                name=d["name"],
                category=Category(d["category"]),
                image_url=_validate_image_url(d["image_url"], d["name"]),
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
    return tuple(
        GameRule(name=d["name"], category=Category(d["category"]), image_url=d["image_url"], meta=d["meta"]) for d in data
    )


#############################
# Weapons & Gamerules       #
#############################

logger.info("Loading items...")


class Items:
    Weapons = _load_items(_ITEMS_DIR / "weapons.json")
    ArmorVests = _load_items(_ITEMS_DIR / "armor_vests.json")
    ArmoredRigs = _load_items(_ITEMS_DIR / "armored_rigs.json")
    Rigs = _load_items(_ITEMS_DIR / "rigs.json")
    Helmets = _load_items(_ITEMS_DIR / "helmets.json")
    Backpacks = _load_items(_ITEMS_DIR / "backpacks.json")


logger.info("Loading game rules...")


class GameRules:
    GunMods = _load_rules(_GAMERULES_DIR / "gun_mods.json")
    Ammo = _load_rules(_GAMERULES_DIR / "ammo.json")
    Maps = _load_rules(_GAMERULES_DIR / "maps.json")
    GoodModifiers = _load_rules(_GAMERULES_DIR / "good_modifiers.json")
    OkModifiers = _load_rules(_GAMERULES_DIR / "ok_modifiers.json")
    BadModifiers = _load_rules(_GAMERULES_DIR / "bad_modifiers.json")


logger.info("Loaded items and game rules!")
