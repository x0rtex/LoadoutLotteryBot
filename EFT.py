from enum import Enum
from typing import Optional, Literal, NamedTuple

#   User-Specific Settings Idea
#
#   The user can specify which traders they have access to in-game.
#   This allows the bot to only roll items which they can actually buy.
#
#   The user can also choose whether they want to roll quest-locked items or not. Since We cannot realistically expect
#   the user to fill in every quest they have or have not completed, so we handle this by letting them choose to enable
#   or disable ALL quest-locked items from being rolled.
#
#   ------ Trader Levels ------
#
#   (Rolled items must be available at or below the user's trader levels)
#
#   Prapor:                   1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Therapist:                1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Skier:                    1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Peacekeeper:              1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Mechanic:                 1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Ragman:                   1 / 2 / 3 / [4]         (Always unlocked, starts at Loyalty Level 1)
#   Jaeger:               0 / 1 / 2 / 3 / [4]         (Trader unlocks after quest completion, hence the '0' option)
#
#   ------ Other Settings ------
#
#   Flea Market Unlocked:      [True] /  False        (Flea Market unlocks at level 15. Allow items that are only available on the Flea Market to be rolled?)
#   Allow quest-locked Items:  [True] /  False        (Some items are locked behind quest completion. Allow these items to be rolled?)
#   Roll mod/ammo levels:      [True] /  False        (Roll gun mod trader levels and ammo trader levels?)
#   Allow thermals:             True  / [False]       (Can thermal scope be rolled as a random modifier?)
#   Meta only:                  True  / [False]       (Exclusively roll for 'meta' items?)
#
#   [] = Default Settings

class Category(Enum):
    ASSAULT_CARBINE = "Assault Carbine"
    ASSAULT_RIFLE = "Assault Rifle"
    SNIPER_RIFLE = "Bolt-Action Rifle"
    MACHINE_GUN = "Machine Gun"
    MARKSMAN_RIFLE = "Marksman Rifle"
    PISTOL = "Pistol"
    SMG = "SMG"
    SHOTGUN = "Shotgun"
    GRENADE_LAUNCHER = "Grenade Launcher"
    MELEE = "Melee"
    RIG = "Rig"
    ARMOR_VEST = "Armor Vest"
    ARMORED_RIG = "Armored Rig"
    HELMET = "Helmet"
    BACKPACK = "Backpack"
    MAP = "Map"
    RANDOM_MODIFIER = "Random Modifier"

class Trader(Enum):
    PRAPOR = "Prapor"
    THERAPIST = "Therapist"
    SKIER = "Skier"
    PEACEKEEPER = "Peacekeeper"
    MECHANIC = "Mechanic"
    RAGMAN = "Ragman"
    JAEGER = "Jaeger"

class TraderInfo(NamedTuple):
    level: Optional[Literal[0, 1, 2, 3, 4]] # Trader loyalty level (0 = locked)
    quest_locked: bool # Whether an item is locked behind a trader's quest or not
    barter: bool # Whether an item is only obtainable via barter or not

class Weapons:
    def __init__(self,
            name: str,
            category: Optional[Category],
            image_url: str,
            force: bool, # Whether an item should be forced to be roll-able
            meta: bool, # Whether an item is considered 'meta' or not
            flea: bool, # Whether an item is obtainable from the flea market or not
            trader_info: Optional[dict[Trader, TraderInfo]], # Dict because item can be obtained from multiple traders
    ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.force = force
        self.meta = meta
        self.flea = flea
        self.trader_info = trader_info if trader_info is not None else {}

all_weapons = (
    Weapons(
        name="WILDCARD (YOUR CHOICE)",
        category=None,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Antique_Axe.png/revision/latest/scale-to-width-down/200?cb=20181110013042",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Weapons(
        name="Melee",
        category=Category.MELEE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Antique_Axe.png/revision/latest/scale-to-width-down/200?cb=20181110013042",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
    Weapons(
        name="ADAR 2-15 5.56x45",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/ADAR2-15Image.png/revision/latest/scale-to-width-down/180?cb=20190226190907",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="AUG A1 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f9/Steyr_AUG_A1_5.56x45_assault_rifle.png/revision/latest/scale-to-width-down/320?cb=20221231014107",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="AUG A3 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4a/AUG_A3_Image.png/revision/latest/scale-to-width-down/320?cb=20221231014349",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-101 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/AK101_Image.png/revision/latest/scale-to-width-down/180?cb=20180502204454",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-102 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/Ak102image.png/revision/latest/scale-to-width-down/180?cb=20180506001257",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-103 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/AK-103_7.62x39.png/revision/latest/scale-to-width-down/180?cb=20180429234506",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-104 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b2/AK-104Image.png/revision/latest/scale-to-width-down/180?cb=20180503235112",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=True, barter=True)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-105 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/AK-105_5.45x39.png/revision/latest/scale-to-width-down/180?cb=20180429234412",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-74 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/AK-74Image.png/revision/latest/scale-to-width-down/180?cb=20181226154054",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-74M 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/AK-74M.png/revision/latest/scale-to-width-down/180?cb=20180513014125",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=True)),
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Kalashnikov AK-74N 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Akn.png/revision/latest/scale-to-width-down/180?cb=20181028171233",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Kalashnikov AKM 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/Akm.png/revision/latest/scale-to-width-down/180?cb=20180206133400",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKMN 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Akmn.png/revision/latest/scale-to-width-down/180?cb=20180206133117",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKMS 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Akms.png/revision/latest/scale-to-width-down/180?cb=20180427005729",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKMSN 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/Akmsn.png/revision/latest/scale-to-width-down/180?cb=20180503233021",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKS-74 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/AKS-74.png/revision/latest/scale-to-width-down/180?cb=20181230153732",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Weapons(
        name="Kalashnikov AKS-74N 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/AKS-74N.png/revision/latest/scale-to-width-down/180?cb=20180426173339",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKS-74U 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Aks74u.png/revision/latest/scale-to-width-down/180?cb=20181028171406",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=True, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKS-74UB 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/Aks74ub.png/revision/latest/scale-to-width-down/180?cb=20181028171415",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Kalashnikov AKS-74UN 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Aks74un.png/revision/latest/scale-to-width-down/180?cb=20181028171353",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="ASh-12 12.7x55",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/ASh_12.png/revision/latest/scale-to-width-down/180?cb=20211206013813",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=4, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="AS VAL 9x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1c/Asval.png/revision/latest/scale-to-width-down/180?cb=20190305220933",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=4, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="CMMG Mk47 Mutant 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Mk47_Mutant_View.png/revision/latest/scale-to-width-down/180?cb=20211203223357",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.SKIER: (TraderInfo(level=4, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Desert Tech MDR 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/DT_MDR_5.56x45_ASSAULT_RIFLE.png/revision/latest/scale-to-width-down/180?cb=20190411211744",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Desert Tech MDR 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/33/DT_MDR_308.png/revision/latest/scale-to-width-down/180?cb=20191228210602",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=4, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="HK 416A5 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/HK416Image.png/revision/latest/scale-to-width-down/180?cb=20181226145352",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=True, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=4, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Colt M4A1 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/29/M4a1.png/revision/latest/scale-to-width-down/180?cb=20181028172147",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="FN SCAR-L (Mk 16) 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/00/SCAR-L_Insp.gif/revision/latest/scale-to-width-down/180?cb=20220101204420",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=True, barter=True)),
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="FN SCAR-H (Mk 17) 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a8/ScarH_Image.gif/revision/latest/scale-to-width-down/180?cb=20220220215829",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=4, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="SIG MCX .300 BLK",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/-92ucz5kq_Y.jpg/revision/latest/scale-to-width-down/180?cb=20201226014736",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="DS Arms SA-58 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/DS_Arms_SA-58_OSW_Para_7.62x51.png/revision/latest/scale-to-width-down/180?cb=20181028172156",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Lone Star TX-15 DML 5.56x45",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/TX-15_View.PNG/revision/latest/scale-to-width-down/180?cb=20191103030150",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=True)),
            Trader.SKIER: (TraderInfo(level=3, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Molot VPO-209 .366 TKM",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b0/Vpo209.png/revision/latest/scale-to-width-down/180?cb=20181028171328",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Molot VPO-136 \"Vepr KM\" 7.62x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Vpo136.png/revision/latest/scale-to-width-down/180?cb=20181028171300",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Simonov OP-SKS 7.62x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/Opsks.png/revision/latest/scale-to-width-down/180?cb=20190414112410",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Simonov SKS 7.62x39 (No Dovetail)",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Sks.png/revision/latest/scale-to-width-down/180?cb=20190414112401",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="VPO-101 \"Vepr-Hunter\" 7.62x51",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/VeprHunterImage.png/revision/latest/scale-to-width-down/180?cb=20190410211507",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="RPK-16 5.45x39",
        category=Category.MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/RPK-16.png/revision/latest/scale-to-width-down/180?cb=20181226153306",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=4, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="HK MP5 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Mp5.png/revision/latest/scale-to-width-down/180?cb=20180507221414",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="HK MP5K 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/45/HK_MP5K-N.png/revision/latest/scale-to-width-down/180?cb=20211206013958",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="HK MP7A1 4.6x30",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/HKMP7A1Image.png/revision/latest/scale-to-width-down/180?cb=20181111215340",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="HK MP7A2 4.6x30",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/52/HKMP7A2Image.png/revision/latest/scale-to-width-down/180?cb=20181111214757",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=4, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="B&T MP9 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/MP9_View.png/revision/latest/scale-to-width-down/180?cb=20211206014311",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="B&T MP9-N 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/B%26T_MP9-N_9x19_Submachinegun.png/revision/latest/scale-to-width-down/180?cb=20211206014309",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Weapons(
        name="SIG MPX 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f7/Mpx.png/revision/latest/scale-to-width-down/180?cb=20180219121907",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="FN P90 5.7x28",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/P90Image.png/revision/latest/scale-to-width-down/180?cb=20191109011038",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=True)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="PP-19-01 \"Vityaz\" 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/Pp19.png/revision/latest/scale-to-width-down/180?cb=20180219121911",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=True, barter=True)),
        },
    ),
    Weapons(
        name="PP-9 \"Klin\" 9x18PMM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/48/Klin.png/revision/latest/scale-to-width-down/180?cb=20180219121903",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="PP-91 \"Kedr\" 9x18PM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/Kedr.png/revision/latest/scale-to-width-down/180?cb=20180219121901",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="PP-91-01 \"Kedr-B\" 9x18PM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a4/Kedrb.png/revision/latest/scale-to-width-down/180?cb=20180219121902",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="PPSh-41 7.62x25",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/PPSH-41_View.png/revision/latest/scale-to-width-down/180?cb=20211206010213",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Saiga-9 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/Saiga9.png/revision/latest/scale-to-width-down/180?cb=20180219121912",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=1, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Soyuz-TM STM-9 Gen.2 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/STM-9_Base_View.png/revision/latest/scale-to-width-down/180?cb=20211206010453",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="HK UMP .45 ACP",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/UMP45_View.png/revision/latest/scale-to-width-down/180?cb=20211206010703",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="TDI KRISS Vector Gen.2 .45 ACP",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/Vector45_fir_unloaded_view.png/revision/latest/scale-to-width-down/180?cb=20211206011407",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=3, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="TDI KRISS Vector Gen.2 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9e/Vector_9x19_View.png/revision/latest/scale-to-width-down/180?cb=20211206011601",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=3, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Mossberg 590A1 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/M590A1_View.png/revision/latest/scale-to-width-down/180?cb=20211206014100",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Remington Model 870 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/M870.png/revision/latest/scale-to-width-down/180?cb=20180426140946",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=1, quest_locked=True, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="MP-133 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/Mr133.png/revision/latest/scale-to-width-down/180?cb=20180219121908",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="MP-153 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/Mp153.png/revision/latest/scale-to-width-down/180?cb=20180219121906",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.SKIER: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="MP-155 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/MP-155.png/revision/latest/scale-to-width-down/180?cb=20211205210153",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Baikal MP-43-1C 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/MP-43-1C_12ga_double-barrel_shotgun.jpg/revision/latest/scale-to-width-down/180?cb=20211213051714",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="MTs-255-12 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2d/EFT_UpcomingMTs255.png/revision/latest/scale-to-width-down/180?cb=20190515021208",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Saiga-12 12ga ver.10 12/76",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Saiga12.png/revision/latest/scale-to-width-down/180?cb=20180219121914",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="TOZ-106 20ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/Toz.png/revision/latest/scale-to-width-down/180?cb=20180219121918",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=1, quest_locked=False, barter=False)),
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="TOZ KS-23M 23x75mm",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/KS-23M.png/revision/latest/scale-to-width-down/180?cb=20201019145716",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="HK G28 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/18/G28_Full.png/revision/latest/scale-to-width-down/180?cb=20211214013521",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=True)),
            Trader.JAEGER: (TraderInfo(level=4, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Springfield Armory M1A 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/M1A_Icon.png/revision/latest/scale-to-width-down/180?cb=20180503234958",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="SWORD International Mk-18 .338 LM",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a2/Mk18.png/revision/latest/scale-to-width-down/180?cb=20210102132503",
        force=False,
        meta=True,
        flea=False,
        trader_info=None,
    ),
    Weapons(
        name="Kel-Tec RFB 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/KT_RFB.png/revision/latest/scale-to-width-down/180?cb=20201019134602",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Remington R11 RSASS 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9b/Rsass.png/revision/latest/scale-to-width-down/180?cb=20181122021513",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=4, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Knight's Armament Company SR-25 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/69/SR-25_View.png/revision/latest/scale-to-width-down/180?cb=20191227220256",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="SVDS 7.62x54R",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8f/SVD-S.png/revision/latest/scale-to-width-down/180?cb=20190411211731",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="VSS Vintorez 9x39",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/Vss.png/revision/latest/scale-to-width-down/180?cb=20210114170659",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="LOBAEV Arms DVL-10 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/Dvl10.png/revision/latest/scale-to-width-down/180?cb=20180219121859",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=3, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Remington Model 700 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/M700Image.png/revision/latest/scale-to-width-down/180?cb=20181226171021",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True)),
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="Mosin 7.62x54R (Sniper)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/MosinInspect.png/revision/latest/scale-to-width-down/180?cb=20180918200314",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=True))
        },
    ),
    Weapons(
        name="Mosin 7.62x54R (Infantry)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d4/MosinInfantryImage.png/revision/latest/scale-to-width-down/180?cb=20181226165344",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="SV-98 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Sv98.png/revision/latest/scale-to-width-down/180?cb=20180427101420",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=True)),
            Trader.JAEGER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Orsis T-5000M 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/T-5000_View.png/revision/latest/scale-to-width-down/180?cb=20200216013517",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=3, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Molot VPO-215 \"Gornostay\" .366 TKM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4e/VPO-215_View.png/revision/latest/scale-to-width-down/180?cb=20200216013459",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="HK USP .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ad/Usp1.png/revision/latest/scale-to-width-down/180?cb=20220118221605",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=2, quest_locked=False, barter=False))
        },
    ),
    Weapons(
        name="APB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/APBImage.png/revision/latest/scale-to-width-down/400?cb=20200216023044",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Stechkin APS 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Stechkin_Automatic_Pistol_9x18PM.png/revision/latest/scale-to-width-down/200?cb=20200216021943",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="FN Five-seveN MK2 5.7x28",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/Five-seveN.gif/revision/latest/scale-to-width-down/200?cb=20191109004734",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Glock 17 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Glock17.png/revision/latest/scale-to-width-down/200?cb=20200216022006",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Glock 18C 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Glock18CImage.png/revision/latest/scale-to-width-down/200?cb=20200216022017",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=3, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Glock 19X 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/G19X_View.png/revision/latest?cb=20221231013454",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Colt M1911A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bd/M1911A1_View.png/revision/latest/scale-to-width-down/200?cb=20200508214809",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Colt M45A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c3/M45A1.png/revision/latest/scale-to-width-down/200?cb=20201019153037",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Weapons(
        name="Beretta M9A3 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/EFT_UpcomingM9A3.png/revision/latest/scale-to-width-down/200?cb=20200216022039",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Yarygin MP-443 \"Grach\" 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/Grach.png/revision/latest/scale-to-width-down/200?cb=20200216022052",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="SIG P226R 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c6/P226.png/revision/latest/scale-to-width-down/200?cb=20200216022104",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="PB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Pb.png/revision/latest/scale-to-width-down/200?cb=20200216023013",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Lebedev PL-15 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/PL-15image.png/revision/latest/scale-to-width-down/200?cb=20211206010342",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Makarov PM (t) 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/Makarovt.png/revision/latest/scale-to-width-down/200?cb=20200216022116",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Weapons(
        name="Makarov PM 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/Makarov.png/revision/latest/scale-to-width-down/200?cb=20200216022127",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Serdyukov SR-1MP Gyurza 9x21",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cc/Sr1mp.png/revision/latest/scale-to-width-down/200?cb=20200216022136",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=2, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="TT-33 7.62x25",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Tt.png/revision/latest/scale-to-width-down/200?cb=20200216022150",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: (TraderInfo(level=1, quest_locked=False, barter=False)),
            Trader.MECHANIC: (TraderInfo(level=1, quest_locked=False, barter=True)),
        },
    ),
    Weapons(
        name="TT-33 7.62x25 (Golden)",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/46/TT_Pistol_7.62x25_TT_gold_2.png/revision/latest/scale-to-width-down/200?cb=20200216022203",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Weapons(
        name="Chiappa Rhino 200DS 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/CR_200DS_1.png/revision/latest/scale-to-width-down/180?cb=20220416231853",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Chiappa Rhino 50DS .357",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9c/CR_50DS_.357_1.png/revision/latest/scale-to-width-down/180?cb=20220417132057",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=False, barter=False)),
            Trader.SKIER: (TraderInfo(level=2, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="HK G36 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/G36_View.png/revision/latest/scale-to-width-down/180?cb=20220705223014",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Benelli M3 Super 90 dual-mode 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Benelli_M3_Super_90.png/revision/latest/scale-to-width-down/180?cb=20220703180524",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=2, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="Accuracy International AXMC .338 LM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/AXMC_.338_LM.png/revision/latest/scale-to-width-down/180?cb=20220705212920",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=4, quest_locked=True, barter=False)),
        },
    ),
    Weapons(
        name="MP-18 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/MP18_VIew.png/revision/latest/scale-to-width-down/180?cb=20220629224646",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: (TraderInfo(level=1, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="Rifle Dynamics RD-704 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ce/RD-704.jpg/revision/latest/scale-to-width-down/180?cb=20220702095109",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.MECHANIC: (TraderInfo(level=4, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="SAG AK-545 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/SAG.545.png/revision/latest/scale-to-width-down/180?cb=20220701160057",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="SAG AK-545 Short 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/AK-545Short_View.png/revision/latest/scale-to-width-down/180?cb=202206292156099",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: (TraderInfo(level=2, quest_locked=False, barter=False)),
        },
    ),
    Weapons(
        name="FN40GL Mk2 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b8/FNGL40inspect.png/revision/latest/scale-to-width-down/180?cb=20211206014144",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: (TraderInfo(level=4, quest_locked=True, barter=True)),
        },
    ),
    Weapons(
        name="Milkor M32A1 MSGL 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/M32A1inspect.png/revision/latest/scale-to-width-down/180?cb=20220704113236",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
)
"""
class Armor:
    def __init__(self,
            name: str,
            category: Optional[Category],
            image_url: str,
            force: bool,  # Whether an item should be forced to be roll-able
            meta: bool,  # Whether an item is considered 'meta' or not
            flea: bool,  # Whether an item is obtainable from the flea market or not
            trader_info: Optional[dict[Trader, TraderInfo]],
            # Dict because item can be obtained from multiple traders
            ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.force = force
        self.meta = meta
        self.flea = flea
        self.trader_info = trader_info if trader_info is not None else {}

armor_vests = (
    Armor(
        name="No Armor",
        category=Category.ARMOR_VEST,
        image_url="https://i.imgur.com/V2SWmZh.png",
    ),
    Armor(
        name="BNTI Module-3M body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f8/3M_icon.png/revision/latest/scale-to-width-down/190?cb=20190519124804",
    ),
)

armored_rigs = (
    # stuff
)

all_armors = armor_vests + armored_rigs

class Rig:
    def __init__(self,
            name: str,
            category: Optional[Category],
            image_url: str,
            force: bool,  # Whether an item should be forced to be roll-able
            meta: bool,  # Whether an item is considered 'meta' or not
            flea: bool,  # Whether an item is obtainable from the flea market or not
            trader_info: Optional[dict[Trader, TraderInfo]],  # Dict because item can be obtained from multiple traders
    ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.force = force
        self.meta = meta
        self.flea = flea
        self.trader_info = trader_info if trader_info is not None else {}

all_rigs = (
    Rig(
        name="No Rig",
        image_url="",
    ),
)

class Helmet:
    def __init__(self,
            name: str,
            category: Optional[Category],
            image_url: str,
            force: bool, # Whether an item should be forced to be roll-able
            meta: bool, # Whether an item is considered 'meta' or not
            flea: bool, # Whether an item is obtainable from the flea market or not
            trader_info: Optional[dict[Trader, TraderInfo]], # Dict because item can be obtained from multiple traders
    ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.force = force
        self.meta = meta
        self.flea = flea
        self.trader_info = trader_info if trader_info is not None else {}

all_helmets = (
    Helmet(
        name="No Helmet",
        image_url="",
    ),
)

class Backpack:
    def __init__(self,
            name: str,
            category: Optional[Category],
            image_url: str,
            force: bool, # Whether an item should be forced to be roll-able
            meta: bool, # Whether an item is considered 'meta' or not
            flea: bool, # Whether an item is obtainable from the flea market or not
            trader_info: Optional[dict[Trader, TraderInfo]], # Dict because item can be obtained from multiple traders
    ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.force = force
        self.meta = meta
        self.flea = flea
        self.trader_info = trader_info if trader_info is not None else {}

all_backpacks = (
    Backpack(
        name="No Backpack",
        image_url="",
    ),
)

class Map:
    def __init__(self,
            name: str,
            image_url: str
            ):
        self.name = name
        self.category = Category.MAP
        self.image_url = image_url

all_maps = (
    Map(name="Factory",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1a/Factory-Day_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811153020",),
    Map(name="Woods",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_woods.png/revision/latest/scale-to-width-down/382?cb=20171101223132",),
    Map(name="Customs",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/Customs_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811151055",),
    Map(name="Interchange",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_interchange.png/revision/latest/scale-to-width-down/382?cb=20200811153253",),
    Map(name="Shoreline",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d5/Banner_shoreline.png/revision/latest/scale-to-width-down/382?cb=20171101223501",),
    Map(name="Reserve",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f4/Reserve.png/revision/latest/scale-to-width-down/382?cb=20191101214624",),
    Map(name="The Lab",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d7/TheLabBanner.png/revision/latest/scale-to-width-down/382?cb=20181225171705",),
    Map(name="Lighthouse",image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/dc/Banner_lighthouse.png/revision/latest/scale-to-width-down/382?cb=20211213001748",),
    Map(name="Streets of Tarkov", image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/41/Banner_streets.png/revision/latest/scale-to-width-down/382?cb=20230131205551",),
)

class RandomModifier:
    def __init__(self,
            name: str,
            image_url: str,
            ):
        self.name = name
        self.category = Category.RANDOM_MODIFIER
        self.image_url = image_url

bad_modifiers = (
    # ...
)

ok_modifiers = (
    # ...
)

good_modifiers = (
    #
)

all_modifiers = (bad_modifiers, ok_modifiers, good_modifiers)
"""
