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
    WEAPON = "Weapon"
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
    level: Optional[Literal[0, 1, 2, 3, 4]]  # Trader loyalty level (0 = locked)
    quest_locked: bool  # Whether an item is locked behind a trader's quest or not
    barter: bool  # Whether an item is only obtainable via barter or not


class Item:
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


ALL_WEAPONS = (
    Item(
        name="YOUR CHOICE",
        category=Category.WEAPON,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="Melee",
        category=Category.MELEE,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=False,
        flea=False,
        trader_info=None
    ),
    Item(
        name="ADAR 2-15 5.56x45",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/ADAR2-15Image.png/revision/latest/scale-to-width-down/180?cb=20190226190907",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="AUG A1 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f9/Steyr_AUG_A1_5.56x45_assault_rifle.png/revision/latest/scale-to-width-down/320?cb=20221231014107",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="AUG A3 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4a/AUG_A3_Image.png/revision/latest/scale-to-width-down/320?cb=20221231014349",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-101 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/AK101_Image.png/revision/latest/scale-to-width-down/180?cb=20180502204454",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-102 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/Ak102image.png/revision/latest/scale-to-width-down/180?cb=20180506001257",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-103 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/AK-103_7.62x39.png/revision/latest/scale-to-width-down/180?cb=20180429234506",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-104 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b2/AK-104Image.png/revision/latest/scale-to-width-down/180?cb=20180503235112",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AK-105 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/AK-105_5.45x39.png/revision/latest/scale-to-width-down/180?cb=20180429234412",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-74 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/AK-74Image.png/revision/latest/scale-to-width-down/180?cb=20181226154054",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-74M 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/AK-74M.png/revision/latest/scale-to-width-down/180?cb=20180513014125",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AK-74N 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Akn.png/revision/latest/scale-to-width-down/180?cb=20181028171233",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AKM 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/Akm.png/revision/latest/scale-to-width-down/180?cb=20180206133400",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMN 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Akmn.png/revision/latest/scale-to-width-down/180?cb=20180206133117",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMS 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Akms.png/revision/latest/scale-to-width-down/180?cb=20180427005729",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMSN 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/Akmsn.png/revision/latest/scale-to-width-down/180?cb=20180503233021",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/AKS-74.png/revision/latest/scale-to-width-down/180?cb=20181230153732",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Item(
        name="Kalashnikov AKS-74N 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/AKS-74N.png/revision/latest/scale-to-width-down/180?cb=20180426173339",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74U 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Aks74u.png/revision/latest/scale-to-width-down/180?cb=20181028171406",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74UB 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/Aks74ub.png/revision/latest/scale-to-width-down/180?cb=20181028171415",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74UN 5.45x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Aks74un.png/revision/latest/scale-to-width-down/180?cb=20181028171353",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="ASh-12 12.7x55",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/ASh_12.png/revision/latest/scale-to-width-down/180?cb=20211206013813",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="AS VAL 9x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1c/Asval.png/revision/latest/scale-to-width-down/180?cb=20190305220933",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="CMMG Mk47 Mutant 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Mk47_Mutant_View.png/revision/latest/scale-to-width-down/180?cb=20211203223357",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.SKIER: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Desert Tech MDR 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/DT_MDR_5.56x45_ASSAULT_RIFLE.png/revision/latest/scale-to-width-down/180?cb=20190411211744",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Desert Tech MDR 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/33/DT_MDR_308.png/revision/latest/scale-to-width-down/180?cb=20191228210602",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="HK 416A5 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/HK416Image.png/revision/latest/scale-to-width-down/180?cb=20181226145352",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=True, barter=False),
            Trader.MECHANIC: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M4A1 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/29/M4a1.png/revision/latest/scale-to-width-down/180?cb=20181028172147",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="FN SCAR-L (Mk 16) 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/00/SCAR-L_Insp.gif/revision/latest/scale-to-width-down/180?cb=20220101204420",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=True, barter=True),
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN SCAR-H (Mk 17) 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a8/ScarH_Image.gif/revision/latest/scale-to-width-down/180?cb=20220220215829",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="SIG MCX .300 BLK",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/-92ucz5kq_Y.jpg/revision/latest/scale-to-width-down/180?cb=20201226014736",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="DS Arms SA-58 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/DS_Arms_SA-58_OSW_Para_7.62x51.png/revision/latest/scale-to-width-down/180?cb=20181028172156",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Lone Star TX-15 DML 5.56x45",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/TX-15_View.PNG/revision/latest/scale-to-width-down/180?cb=20191103030150",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
            Trader.SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Molot VPO-209 .366 TKM",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b0/Vpo209.png/revision/latest/scale-to-width-down/180?cb=20181028171328",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Molot VPO-136 \"Vepr KM\" 7.62x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Vpo136.png/revision/latest/scale-to-width-down/180?cb=20181028171300",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Simonov OP-SKS 7.62x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/Opsks.png/revision/latest/scale-to-width-down/180?cb=20190414112410",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Simonov SKS 7.62x39 (No Dovetail)",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Sks.png/revision/latest/scale-to-width-down/180?cb=20190414112401",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="VPO-101 \"Vepr-Hunter\" 7.62x51",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/VeprHunterImage.png/revision/latest/scale-to-width-down/180?cb=20190410211507",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="RPK-16 5.45x39",
        category=Category.MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/RPK-16.png/revision/latest/scale-to-width-down/180?cb=20181226153306",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP5 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Mp5.png/revision/latest/scale-to-width-down/180?cb=20180507221414",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP5K 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/45/HK_MP5K-N.png/revision/latest/scale-to-width-down/180?cb=20211206013958",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK MP7A1 4.6x30",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/HKMP7A1Image.png/revision/latest/scale-to-width-down/180?cb=20181111215340",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP7A2 4.6x30",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/52/HKMP7A2Image.png/revision/latest/scale-to-width-down/180?cb=20181111214757",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="B&T MP9 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/MP9_View.png/revision/latest/scale-to-width-down/180?cb=20211206014311",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="B&T MP9-N 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/B%26T_MP9-N_9x19_Submachinegun.png/revision/latest/scale-to-width-down/180?cb=20211206014309",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Item(
        name="SIG MPX 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f7/Mpx.png/revision/latest/scale-to-width-down/180?cb=20180219121907",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="FN P90 5.7x28",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/P90Image.png/revision/latest/scale-to-width-down/180?cb=20191109011038",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=True),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="PP-19-01 \"Vityaz\" 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/Pp19.png/revision/latest/scale-to-width-down/180?cb=20180219121911",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="PP-9 \"Klin\" 9x18PMM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/48/Klin.png/revision/latest/scale-to-width-down/180?cb=20180219121903",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="PP-91 \"Kedr\" 9x18PM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/Kedr.png/revision/latest/scale-to-width-down/180?cb=20180219121901",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PP-91-01 \"Kedr-B\" 9x18PM",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a4/Kedrb.png/revision/latest/scale-to-width-down/180?cb=20180219121902",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PPSh-41 7.62x25",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/PPSH-41_View.png/revision/latest/scale-to-width-down/180?cb=20211206010213",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Saiga-9 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/Saiga9.png/revision/latest/scale-to-width-down/180?cb=20180219121912",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Soyuz-TM STM-9 Gen.2 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/STM-9_Base_View.png/revision/latest/scale-to-width-down/180?cb=20211206010453",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK UMP .45 ACP",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/UMP45_View.png/revision/latest/scale-to-width-down/180?cb=20211206010703",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TDI KRISS Vector Gen.2 .45 ACP",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/Vector45_fir_unloaded_view.png/revision/latest/scale-to-width-down/180?cb=20211206011407",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="TDI KRISS Vector Gen.2 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9e/Vector_9x19_View.png/revision/latest/scale-to-width-down/180?cb=20211206011601",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Mossberg 590A1 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/M590A1_View.png/revision/latest/scale-to-width-down/180?cb=20211206014100",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Remington Model 870 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/M870.png/revision/latest/scale-to-width-down/180?cb=20180426140946",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=True, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-133 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/Mr133.png/revision/latest/scale-to-width-down/180?cb=20180219121908",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-153 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/Mp153.png/revision/latest/scale-to-width-down/180?cb=20180219121906",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.SKIER: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-155 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/MP-155.png/revision/latest/scale-to-width-down/180?cb=20211205210153",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Baikal MP-43-1C 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/MP-43-1C_12ga_double-barrel_shotgun.jpg/revision/latest/scale-to-width-down/180?cb=20211213051714",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="MTs-255-12 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2d/EFT_UpcomingMTs255.png/revision/latest/scale-to-width-down/180?cb=20190515021208",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Saiga-12 12ga ver.10 12/76",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Saiga12.png/revision/latest/scale-to-width-down/180?cb=20180219121914",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="TOZ-106 20ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/Toz.png/revision/latest/scale-to-width-down/180?cb=20180219121918",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="TOZ KS-23M 23x75mm",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/KS-23M.png/revision/latest/scale-to-width-down/180?cb=20201019145716",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK G28 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/18/G28_Full.png/revision/latest/scale-to-width-down/180?cb=20211214013521",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=True),
            Trader.JAEGER: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Springfield Armory M1A 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/M1A_Icon.png/revision/latest/scale-to-width-down/180?cb=20180503234958",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="SWORD International Mk-18 .338 LM",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a2/Mk18.png/revision/latest/scale-to-width-down/180?cb=20210102132503",
        force=False,
        meta=True,
        flea=False,
        trader_info=None,
    ),
    Item(
        name="Kel-Tec RFB 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/KT_RFB.png/revision/latest/scale-to-width-down/180?cb=20201019134602",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Remington R11 RSASS 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9b/Rsass.png/revision/latest/scale-to-width-down/180?cb=20181122021513",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Knight's Armament Company SR-25 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/69/SR-25_View.png/revision/latest/scale-to-width-down/180?cb=20191227220256",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SVDS 7.62x54R",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8f/SVD-S.png/revision/latest/scale-to-width-down/180?cb=20190411211731",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="VSS Vintorez 9x39",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/Vss.png/revision/latest/scale-to-width-down/180?cb=20210114170659",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="LOBAEV Arms DVL-10 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/Dvl10.png/revision/latest/scale-to-width-down/180?cb=20180219121859",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Remington Model 700 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/M700Image.png/revision/latest/scale-to-width-down/180?cb=20181226171021",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Mosin 7.62x54R (Sniper)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/MosinInspect.png/revision/latest/scale-to-width-down/180?cb=20180918200314",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True)
        },
    ),
    Item(
        name="Mosin 7.62x54R (Infantry)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d4/MosinInfantryImage.png/revision/latest/scale-to-width-down/180?cb=20181226165344",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SV-98 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Sv98.png/revision/latest/scale-to-width-down/180?cb=20180427101420",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
            Trader.JAEGER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Orsis T-5000M 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/T-5000_View.png/revision/latest/scale-to-width-down/180?cb=20200216013517",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Molot VPO-215 \"Gornostay\" .366 TKM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4e/VPO-215_View.png/revision/latest/scale-to-width-down/180?cb=20200216013459",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK USP .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ad/Usp1.png/revision/latest/scale-to-width-down/180?cb=20220118221605",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=2, quest_locked=False, barter=False)
        },
    ),
    Item(
        name="APB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/APBImage.png/revision/latest/scale-to-width-down/400?cb=20200216023044",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Stechkin APS 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Stechkin_Automatic_Pistol_9x18PM.png/revision/latest/scale-to-width-down/200?cb=20200216021943",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN Five-seveN MK2 5.7x28",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/Five-seveN.gif/revision/latest/scale-to-width-down/200?cb=20191109004734",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 17 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Glock17.png/revision/latest/scale-to-width-down/200?cb=20200216022006",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 18C 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Glock18CImage.png/revision/latest/scale-to-width-down/200?cb=20200216022017",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 19X 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/G19X_View.png/revision/latest?cb=20221231013454",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M1911A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bd/M1911A1_View.png/revision/latest/scale-to-width-down/200?cb=20200508214809",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M45A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c3/M45A1.png/revision/latest/scale-to-width-down/200?cb=20201019153037",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Item(
        name="Beretta M9A3 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/EFT_UpcomingM9A3.png/revision/latest/scale-to-width-down/200?cb=20200216022039",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Yarygin MP-443 'Grach' 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/Grach.png/revision/latest/scale-to-width-down/200?cb=20200216022052",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SIG P226R 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c6/P226.png/revision/latest/scale-to-width-down/200?cb=20200216022104",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Pb.png/revision/latest/scale-to-width-down/200?cb=20200216023013",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Lebedev PL-15 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/PL-15image.png/revision/latest/scale-to-width-down/200?cb=20211206010342",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Makarov PM (t) 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/Makarovt.png/revision/latest/scale-to-width-down/200?cb=20200216022116",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Item(
        name="Makarov PM 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/Makarov.png/revision/latest/scale-to-width-down/200?cb=20200216022127",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Serdyukov SR-1MP Gyurza 9x21",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cc/Sr1mp.png/revision/latest/scale-to-width-down/200?cb=20200216022136",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TT-33 7.62x25",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Tt.png/revision/latest/scale-to-width-down/200?cb=20200216022150",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TT-33 7.62x25 (Golden)",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/46/TT_Pistol_7.62x25_TT_gold_2.png/revision/latest/scale-to-width-down/200?cb=20200216022203",
        force=False,
        meta=False,
        flea=True,
        trader_info=None,
    ),
    Item(
        name="Chiappa Rhino 200DS 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/CR_200DS_1.png/revision/latest/scale-to-width-down/180?cb=20220416231853",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Chiappa Rhino 50DS .357",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9c/CR_50DS_.357_1.png/revision/latest/scale-to-width-down/180?cb=20220417132057",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.SKIER: TraderInfo(level=2, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="HK G36 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/G36_View.png/revision/latest/scale-to-width-down/180?cb=20220705223014",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Benelli M3 Super 90 dual-mode 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Benelli_M3_Super_90.png/revision/latest/scale-to-width-down/180?cb=20220703180524",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Accuracy International AXMC .338 LM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/AXMC_.338_LM.png/revision/latest/scale-to-width-down/180?cb=20220705212920",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.JAEGER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="MP-18 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/MP18_VIew.png/revision/latest/scale-to-width-down/180?cb=20220629224646",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Rifle Dynamics RD-704 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ce/RD-704.jpg/revision/latest/scale-to-width-down/180?cb=20220702095109",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.MECHANIC: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SAG AK-545 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/SAG.545.png/revision/latest/scale-to-width-down/180?cb=20220701160057",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SAG AK-545 Short 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/AK-545Short_View.png/revision/latest/scale-to-width-down/180?cb=202206292156099",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN40GL Mk2 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b8/FNGL40inspect.png/revision/latest/scale-to-width-down/180?cb=20211206014144",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="Milkor M32A1 MSGL 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/M32A1inspect.png/revision/latest/scale-to-width-down/180?cb=20220704113236",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
)


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


ARMOR_VESTS = (
    Item(
        name="YOUR CHOICE",
        category=Category.ARMOR_VEST,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="BNTI Module-3M body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f8/3M_icon.png/revision/latest/scale-to-width-down/190?cb=20190519124804",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="PACA Soft Armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/25/PACA_Soft_Armor.png/revision/latest/scale-to-width-down/320?cb=20190301085818",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="PACA Soft Armor (Rivals Edition)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/41/PACA_Soft_Armor_%28Rivals_Edition%29.PNG/revision/latest/scale-to-width-down/304?cb=20211231213516",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="6B2 body armor (Flora)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/87/6B2_View.png/revision/latest/scale-to-width-down/320?cb=20191227220309",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="MF-UNTAR body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/MF-UNTAR_Armor_vest.png/revision/latest/scale-to-width-down/320?cb=20180520205929",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BNTI Zhuk-3 body armor (Press)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/76/Zhuk-3_Press_armor.png/revision/latest/scale-to-width-down/296?cb=20190301085839",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.SKIER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="6B23-1 body armor (Digital Flora)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d3/6b23-1.png/revision/latest/scale-to-width-down/302?cb=20190301085852",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="DRD body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/DRD_body_armor_2.png/revision/latest/scale-to-width-down/320?cb=20220703010536",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="BNTI Kirasa-N body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/83/BNTI-Kirasa-N-armor.png/revision/latest/scale-to-width-down/312?cb=20190301085905",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="NFM THOR Concealable Reinforced Vest body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e7/Thor_View.png/revision/latest/scale-to-width-down/320?cb=20211205235338",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="HighCom Trooper TFO body armor (Multicam)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/09/Highcom_Trooper_TFO_armor_%28multicam%29.png/revision/latest/scale-to-width-down/319?cb=20190301085944",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="6B13 assault armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/6B13_assault_armor.gif/revision/latest/scale-to-width-down/320?cb=20190101213615",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B23-2 body armor (Mountain Flora)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7f/6B23-2_armorImage.png/revision/latest/scale-to-width-down/273?cb=20190301085921",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hexatac HPC Plate Carrier (Multicam Black)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/HPC3.PNG/revision/latest/scale-to-width-down/320?cb=20221230210248",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Korund-VM body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/db/KORUND.png/revision/latest/scale-to-width-down/320?cb=20201019171744",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="FORT Redut-M body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7b/FORT_Redut-M_body_armor.png/revision/latest/scale-to-width-down/320?cb=20190410224156",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B13 M modified assault armor (Tan)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/6B13_M.png/revision/latest/scale-to-width-down/281?cb=20190301085955",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="IOTV Gen4 body armor (High Mobility Kit)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2f/IOTV_HMK.png/revision/latest/scale-to-width-down/272?cb=20190710085120",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="BNTI Gzhel-K body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5a/GZHELK-Image.PNG/revision/latest/scale-to-width-down/320?cb=20180520205529",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="FORT Defender-2 body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/Defender-2_View.png/revision/latest/scale-to-width-down/320?cb=20200528221930",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="IOTV Gen4 body armor (Assault Kit)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/95/IOTV_Assault.png/revision/latest/scale-to-width-down/320?cb=20190710085240",
        force=False,
        meta=False,
        flea=False,
        trader_info=None,
    ),
    Item(
        name="IOTV Gen4 body armor (Full Protection Kit)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f5/IOTVFullImage.png/revision/latest/scale-to-width-down/320?cb=20190301090027",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="FORT Redut-T5 body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/FORT_Redut-T5_body_armor.png/revision/latest/scale-to-width-down/320?cb=20190410224442",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="5.11 Tactical Hexgrid plate carrier",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/11/HexPlateCarrier_View.png/revision/latest/scale-to-width-down/320?cb=20201230004256",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="LBT-6094A Slick Plate Carrier",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ee/SLICK-BIG-GIF.gif/revision/latest?cb=20220328142855",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="BNTI Zhuk-6a body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bc/Zhuk-6a_heavy_armor.PNG/revision/latest/scale-to-width-down/320?cb=20190301090039",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="NFM THOR Integrated Carrier body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/80/THOR_IC_View.PNG/revision/latest/scale-to-width-down/320?cb=20211206001354",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="6B43 6A Zabralo-Sh body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/6B4.png/revision/latest/scale-to-width-down/320?cb=20190301090056",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
            Trader.MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Kora-Kulon body armor",
        category=Category.ARMOR_VEST,
        image_url="https://i.imgur.com/qzkgWxT.png",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Kora-Kulon body armor (Digital Flora)",
        category=Category.ARMOR_VEST,
        image_url="https://i.imgur.com/txoBj01.png",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Interceptor OTV body armor (UCP)",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/OTV_PC_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064821",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
)

ARMORED_RIGS = (
    Item(
        name="WARTECH TV-115 plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/TV-115_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064819",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Eagle Allied Industries MBSS plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b4/MBSS_USECPLATE_Image.png/revision/latest/scale-to-width-down/320?cb=20230813072215",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Eagle Industries MMAC plate carrier (Ranger Green)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Mmac-view.png/revision/latest/scale-to-width-down/320?cb=20211229223039",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Shellback Tactical Banshee plate carrier (A-TACS AU)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/71/Shellback_Tactical_Banshee_plate_carrier.png/revision/latest/scale-to-width-down/320?cb=20221230035237",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Ars Arma A18 Skanda plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/78/A18_View.png/revision/latest/scale-to-width-down/320?cb=20191101010154",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="WARTECH TV-110 plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a9/Wartech_TV-110_plate_carrier.png/revision/latest/scale-to-width-down/320?cb=20190305205424",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="FirstSpear Strandhogg plate carrier (Ranger Green)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Strandhogg.png/revision/latest/scale-to-width-down/253?cb=20211229223415",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ECLiPSE RBAV-AF plate carrier (Ranger Green)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a0/RBAV-AF.png/revision/latest/scale-to-width-down/320?cb=20220705225122",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="CQC Osprey MK4A plate carrier (Assault, MTP)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b6/OspreyMk4_Assault_View.png/revision/latest/scale-to-width-down/320?cb=20211206002242",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B3TM-01M armored rig",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/12/6B3TM-01M.png/revision/latest/scale-to-width-down/320?cb=20191028200236",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B5-15 Zh-86 Uley armored rig",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/6B5-15.png/revision/latest/scale-to-width-down/320?cb=20181231121409",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical M2 plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2a/M2.png/revision/latest/scale-to-width-down/320?cb=20180520221351",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical M1 plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/66/ANA_Tactical_M1.png/revision/latest/scale-to-width-down/320?cb=20181227153645",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Crye Precision AVS plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/97/Crye_Precision_AVS_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20190517215229",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="5.11 Tactical TacTec plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/20/TactecImage.png/revision/latest/scale-to-width-down/320?cb=20180909205723",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Ars Arma CPC MOD.1 plate carrier",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/ArsArmaCPCMOD2.png/revision/latest?cb=20200502000042",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="Crye Precision CPC plate carrier (Goons Edition)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Crye_Precision_CPC_GE.png/revision/latest/scale-to-width-down/320?cb=20220705232026",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="S&S Precision PlateFrame plate carrier (Goons Edition)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b4/S%26S_Precision_PlateFrame_GE.png/revision/latest/scale-to-width-down/320?cb=20220705231743",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="CQC Osprey MK4A plate carrier (Protection, MTP)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/03/OspreyMk4_Protection_View.png/revision/latest/scale-to-width-down/320?cb=20211206002414",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="NPP KlASS Bagariy armored rig",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9a/NPP_Bagariy.png/revision/latest/scale-to-width-down/320?cb=20220705234540",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Tasmanian Tiger SK plate carrier (Multicam Black)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/eb/Tasmanian_Tiger_SK.png/revision/latest/scale-to-width-down/320?cb=20220705232948",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Crye Precision AVS plate carrier (Tagilla Edition)",
        category=Category.ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/92/MBAV_View.png/revision/latest/scale-to-width-down/320?cb=20211205220746",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
)

ALL_ARMORS = ARMOR_VESTS + ARMORED_RIGS


class Rig:
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


ALL_RIGS = (
    Item(
        name="YOUR CHOICE",
        category=Category.RIG,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="Scav Vest",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/ScavVest.png/revision/latest/scale-to-width-down/320?cb=20190517215830",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Security vest",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/Securityvest.png/revision/latest?cb=20201224194010",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Zulu Nylon Gear M4 Reduced Signature Chest Rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Zulu_M4_RSCR_Image.png/revision/latest?cb=20230813064822",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="DIY IDEA chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/63/DIY_IDEA_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20211206005252",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Spiritus Systems Bank Robber chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Bank_Robber_ins.png/revision/latest/scale-to-width-down/320?cb=20200315233111",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SOE Micro Rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/SOE.png/revision/latest/scale-to-width-down/320?cb=20191028034055",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Type 56 Chicom chest harness",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/Type_56_Chicom_Image.png/revision/latest?cb=20230813064823",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="WARTECH TV-109 + TV-106 chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/95/Wartech_gear_rig.png/revision/latest/scale-to-width-down/320?cb=20200624184927",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="CSA chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/CSAImage.png/revision/latest?cb=20210330190914",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="UMTBS 6sh112 Scout-Sniper",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/82/Scout_Sniper_rig.png/revision/latest/scale-to-width-down/301?cb=20171107182903",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Azimut SS \"Khamelion\" chest harness (Olive)",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/Azimut_SS_%22Khamelion%22_chest_harness_%28Olive%29_image.png/revision/latest/scale-to-width-down/320?cb=20221230000547",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Splav Tarzan M22 chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Tarzan.png/revision/latest?cb=20200314180047",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Haley Strategic D3CRX Chest Harness",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/D3CRX.PNG/revision/latest/scale-to-width-down/320?cb=20191030042338",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Dynaforce Triton M43-A chest harness",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/Triton_M43-A_Chest_Harness_ins.png/revision/latest/scale-to-width-down/320?cb=20190410162933",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BlackHawk! Commando chest harness",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3f/Blackhawk%21_commando.gif/revision/latest/scale-to-width-down/320?cb=20190615175249",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Direct Action Thunderbolt compact chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7c/Direct_Action_Thunderbolt_compact_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20201020141605",
        force=False,
        meta=True,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Gear Craft GC-BSS-MK1 chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/12/BSS_Mk1_View.png/revision/latest/scale-to-width-down/320?cb=20201226004117",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Umka M33-SET1 hunter vest",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b7/M33-SET1_vest.png/revision/latest/scale-to-width-down/320?cb=20210330132527",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-1961A Load Bearing Chest Rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/be/LBT_1961_View.png/revision/latest/scale-to-width-down/320?cb=20200528221933",
        force=False,
        meta=True,
        flea=True,
        trader_info=None
    ),
    Item(
        name="LBT-1961A Load Bearing Chest Rig (Goons Edition)",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b5/LBT-1961A_GE.png/revision/latest/scale-to-width-down/320?cb=20220705233654",
        force=False,
        meta=True,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Stich Profi Chest Rig MK2 (Recon, A-TACS FG)",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/StichMk2Recon_View.png/revision/latest/scale-to-width-down/320?cb=20211206001744",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Stich Profi Chest Rig MK2 (Assault, A-TACS FG)",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cb/StichMk2Assault_View_.png/revision/latest/scale-to-width-down/320?cb=20211206002034",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BlackRock chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/79/BlackRock.png/revision/latest/scale-to-width-down/320?cb=20190517215730",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="WARTECH MK3 TV-104 chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Mk3inspect.PNG/revision/latest/scale-to-width-down/320?cb=20190305205103",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="ANA Tactical Alpha chest rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bb/Alpha_Rig.png/revision/latest/scale-to-width-down/320?cb=20190517215939",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Azimut SS \"Zhuk\" chest harness",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/Azimut_SS_Jhuk_Chest_Harness.gif/revision/latest/scale-to-width-down/320?cb=20210331130740",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Velocity Systems MPPV Multi-Purpose Patrol Vest",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/MPPV_view.png/revision/latest/scale-to-width-down/320?cb=20191230104438",
        force=False,
        meta=True,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Belt-A + Belt-B gear rig",
        category=Category.RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f5/Belt-A_Belt-B_gear_rig.png/revision/latest/scale-to-width-down/320?cb=20181227112944",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
)


class Helmet:
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


ALL_HELMETS = (
    Item(
        name="YOUR CHOICE",
        category=Category.HELMET,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Helmet(
        name="Armasight NVG head strap",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/36/Armasight_NVG_Mask.png/revision/latest/scale-to-width-down/320?cb=20181231144238",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="Wilcox Skull Lock head mount",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3a/Slockimage.png/revision/latest?cb=20180319194159",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Helmet(
        name="Bomber beanie",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/Bomber_Beanie.png/revision/latest/scale-to-width-down/320?cb=20211205224712",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="Tac-Kek FAST MT helmet (Replica)",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/32/TK_FAST_View.png/revision/latest/scale-to-width-down/320?cb=20200529000443",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="TSh-4M-L soft tank crew helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/65/TankHelm.png/revision/latest?cb=20191228042121",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="Kolpak-1S riot helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Kolpak-1S.png/revision/latest/scale-to-width-down/320?cb=20180426010942",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="ShPM Firefighter helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/SHPM_Firefighter%27s_helmet.png/revision/latest/scale-to-width-down/320?cb=20181228185855",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="PSh-97 DJETA riot helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3d/PSH-97_-Jeta-_helmet_Image.png/revision/latest/scale-to-width-down/320?cb=20190102011443",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="LShZ light helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/57/LZSh_light_helmet.png/revision/latest/scale-to-width-down/320?cb=20180729193607",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="SSh-68 steel helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/da/SSH-68Image.png/revision/latest/scale-to-width-down/320?cb=20181226233100",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="Galvion Caiman Hybrid helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Caiman.png/revision/latest?cb=20201019155533",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
    Helmet(
        name="NFM HJELM helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/HJELM.png/revision/latest?cb=20211225183648",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="UNTAR helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/UNTAR_Helmet.png/revision/latest/scale-to-width-down/320?cb=20190112203853",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="6B47 Ratnik-BSh helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/6B47.gif/revision/latest/scale-to-width-down/320?cb=20180806190854",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Helmet(
        name="FORT Kiver-M bulletproof helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/89/Kiver-M_Helmet.png/revision/latest?cb=20191227210542",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="SSSh-94 SFERA-S helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b5/SferaInspect.PNG/revision/latest/scale-to-width-down/320?cb=20190112203909",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Helmet(
        name="DevTac Ronin ballistic helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/11/DEVTAC_Ronin_ballistic_helmet_Image.png/revision/latest/scale-to-width-down/320?cb=20190614231623",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Helmet(
        name="MSA ACH TC-2001 MICH Series helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/74/Mich_View.PNG/revision/latest/scale-to-width-down/320?cb=20191101222044",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="MSA ACH TC-2002 MICH Series helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/MICH_2002_View.PNG/revision/latest/scale-to-width-down/320?cb=20191114020056",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=True, barter=False),
        }
    ),
    Helmet(
        name="HighCom Striker ACHHC IIIA helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/ACHHC.gif/revision/latest/scale-to-width-down/320?cb=20180805175454",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="MSA Gallet TC 800 High Cut combat helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/78/MSA_TC_800.png/revision/latest/scale-to-width-down/320?cb=20200313215553",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="Diamond Age Bastion helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/57/Bastion_View.png/revision/latest/scale-to-width-down/320?cb=20200529021033",
        force=False,
        meta=True,
        flea=True,
        trader_info=None
    ),
    Helmet(
        name="Ops-Core FAST MT Super High Cut helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/16/FASTMT.gif/revision/latest/scale-to-width-down/320?cb=20180805220153",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="Crye Precision AirFrame helmet (Tan)",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Crye_Precision_Airframe_Tan_Image.png/revision/latest/scale-to-width-down/320?cb=20190102011851",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Helmet(
        name="Team Wendy EXFIL Ballistic Helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c8/Team_Wendy_EXFIL_Ballistic_Helmet.gif/revision/latest/scale-to-width-down/320?cb=20191229154600",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Helmet(
        name="ZSh-1-2M helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/dc/ZSH-1-2M.gif/revision/latest/scale-to-width-down/320?cb=20180809202110",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="HighCom Striker ULACH IIIA helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/34/ULACH.gif/revision/latest/scale-to-width-down/320?cb=20180806205056",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Helmet(
        name="BNTI LShZ-2DTM helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/73/LSHZ-2DTM3D.png/revision/latest/scale-to-width-down/320?cb=20191030044246",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Helmet(
        name="Maska-1SCh bulletproof helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/Maska_1Sch_helmet.gif/revision/latest/scale-to-width-down/320?cb=20190101152329",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Helmet(
        name="Altyn bulletproof helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f3/Altynimage.png/revision/latest/scale-to-width-down/320?cb=20180517203723",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Helmet(
        name="Rys-T bulletproof helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/77/RysTHelmet.png/revision/latest/scale-to-width-down/320?cb=20201019160756",
        force=False,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Helmet(
        name="Vulkan-5 (LShZ-5) bulletproof helmet",
        category=Category.HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/94/Vulkan-5_%28LShZ-5%29_heavy_helmet.png/revision/latest/scale-to-width-down/320?cb=20190411084258",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
)


class Backpack:
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


ALL_BACKPACKS = (
    Item(
        name="YOUR CHOICE",
        category=Category.BACKPACK,
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
        force=True,
        meta=True,
        flea=False,
        trader_info=None
    ),
    Item(
        name="6Sh118 raid backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/14/6SH118_View.png/revision/latest?cb=20230324190053",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="LBT-2670 Slim Field Med Pack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0a/LBT-2670_View.png/revision/latest?cb=20200314005924",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.THERAPIST: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Mystery Ranch Blackjack 50 backpack (Multicam)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/Mystery_Ranch_Blackjack_50_backpack.png/revision/latest/scale-to-width-down/320?cb=20200714203420",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Eberlestock F4 Terminator load bearing backpack (Tiger Stripe)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5e/F4_terminator_view.png/revision/latest/scale-to-width-down/315?cb=20201020145959",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SSO Attack 2 raid backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/07/Attack.PNG/revision/latest/scale-to-width-down/320?cb=20180517203915",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Tasmanian Tiger Trooper 35 backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/25/Tasmanian_trooper_35.png/revision/latest?cb=20230107201140",
        force=False,
        meta=True,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Pilgrim tourist backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/Pilgrim_Backpack.png/revision/latest/scale-to-width-down/312?cb=20190301071419",
        force=False,
        meta=False,
        flea=False,
        trader_info=None
    ),
    Item(
        name="3V Gear Paratus 3-Day Operator's Tactical backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/3V_G_Paratus.png/revision/latest/scale-to-width-down/320?cb=20190301072645",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Eberlestock G2 Gunslinger II backpack (Dry Earth)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/Gunslinger_II_backpack_image.png/revision/latest/scale-to-width-down/290?cb=20210330172156",
        force=False,
        meta=False,
        flea=False,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="Oakley Mechanism heavy duty backpack (Black)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/Oakley_Mechanism_.png/revision/latest/scale-to-width-down/320?cb=20191108103108",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical Beta 2 Battle backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ef/Beta2BP.png/revision/latest/scale-to-width-down/320?cb=20180802222134",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Gruppa 99 T30 backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/Gruppa_99_T30_BM.gif/revision/latest/scale-to-width-down/320?cb=20220705202041",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Eberlestock F5 Switchblade backpack (Dry Earth)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/Eberlestock_F5_backpack_view.png/revision/latest/scale-to-width-down/315?cb=20201020150753",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Camelbak Tri-Zip assault backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/df/CamelbackThreezeep.png/revision/latest/scale-to-width-down/320?cb=20190517215207",
        force=False,
        meta=True,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-1476A 3Day Pack (Woodland)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/LBT-1476A_VIEW.png/revision/latest/scale-to-width-down/320?cb=20211213223219",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Gruppa 99 T20 backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/be/Gruppa_99_T20_Image.gif/revision/latest/scale-to-width-down/320?cb=20220220203102",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Drawbridge backpack (Coyote Tan)",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/HazardDrawbridge_View.png/revision/latest/scale-to-width-down/320?cb=20211206001203",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Takedown sling backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/Hazard4_Takedown.gif/revision/latest/scale-to-width-down/320?cb=20210331130153",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Pillbox backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/HazardPillboxView.png/revision/latest/scale-to-width-down/320?cb=20211206001554",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Scav backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/96/Scav_Backpack_Inspect.png/revision/latest/scale-to-width-down/320?cb=20190517215051",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="WARTECH Berkut BB-102 backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/03/Wartech_Berkut_VV-102_backpack_ins.png/revision/latest?cb=20201031071733",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-8005A Day Pack backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8c/Day_pack2.PNG/revision/latest/scale-to-width-down/320?cb=20211206005550",
        force=False,
        meta=False,
        flea=True,
        trader_info={
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Sanitar's bag",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/75/Sanitar_Bag_View.png/revision/latest/scale-to-width-down/320?cb=20200727184258",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Flyye MBSS backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c0/Flyye_MBSS_Backpack2.png/revision/latest/scale-to-width-down/303?cb=20221117115315",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
            Trader.PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Mystery Ranch NICE COMM 3 BVS frame system",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/94/COMM_3_BVS.png/revision/latest/scale-to-width-down/320?cb=20220705200139",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Duffle bag",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/EfT_Item_Icon_116.png/revision/latest/scale-to-width-down/320?cb=20180707232346",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="LolKek 3F Transfer tourist backpack",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/LK_3F_backpack_view.png/revision/latest/scale-to-width-down/315?cb=20201020151157",
        force=False,
        meta=False,
        flea=True,
        trader_info=None
    ),
    Item(
        name="Transformer Bag",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/EfT_Item_Icon_316.png/revision/latest/scale-to-width-down/320?cb=20180707232426",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="VKBO army bag",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a6/Armybagimage.png/revision/latest/scale-to-width-down/320?cb=20230324190046",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Tactical sling bag",
        category=Category.BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Tactical_Sling_bag.png/revision/latest/scale-to-width-down/320?cb=20180707232914",
        force=True,
        meta=False,
        flea=True,
        trader_info={
            Trader.RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
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


ALL_MAPS = (
    Map(
        name="YOUR CHOICE",
        image_url="https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg",
    ),
    Map(
        name="Factory",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1a/Factory-Day_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811153020", 
    ),
    Map(
        name="Woods",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_woods.png/revision/latest/scale-to-width-down/382?cb=20171101223132", 
    ),
    Map(
        name="Customs",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/Customs_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811151055", 
    ),
    Map(
        name="Interchange",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_interchange.png/revision/latest/scale-to-width-down/382?cb=20200811153253", 
    ),
    Map(
        name="Shoreline",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d5/Banner_shoreline.png/revision/latest/scale-to-width-down/382?cb=20171101223501", 
    ),
    Map(
        name="Reserve",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f4/Reserve.png/revision/latest/scale-to-width-down/382?cb=20191101214624", 
    ),
    Map(
        name="The Lab",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d7/TheLabBanner.png/revision/latest/scale-to-width-down/382?cb=20181225171705", 
    ),
    Map(
        name="Lighthouse",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/dc/Banner_lighthouse.png/revision/latest/scale-to-width-down/382?cb=20211213001748", 
    ),
    Map(
        name="Streets of Tarkov",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/41/Banner_streets.png/revision/latest/scale-to-width-down/382?cb=20230131205551", 
    ),
)


class RandomModifier:
    def __init__(self,
                 name: str,
                 image_url: str,
                 ):
        self.name = name
        self.category = Category.RANDOM_MODIFIER
        self.image_url = image_url


GOOD_MODIFIERS = (
    RandomModifier(
        name="Weapon of your choice",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/Skill_special_bear_aksystems.png/revision/latest/scale-to-width-down/70?cb=20170329164605",
    ),
    RandomModifier(
        name="Helmet of your choice",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/14/Skill_mental_perception.png/revision/latest/scale-to-width-down/70?cb=20170329164851",
    ),
    RandomModifier(
        name="Backpack of your choice",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/63/Skill_physical_endurance.png/revision/latest/scale-to-width-down/70?cb=20170329164840",
    ),
    RandomModifier(
        name="Map of your choice",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/43/Map.png/revision/latest/scale-to-width-down/662?cb=20220102134631",
    ),
    RandomModifier(
        name="Ask your scav for some loot",
        image_url="https://pbs.twimg.com/media/DlXnlRvXoAAhOv2.jpg",
    ),
    RandomModifier(
        name="Pop any 3 stimulants at start of raid",
        image_url="https://i.imgur.com/lYmpWWL.png",
    ),
    RandomModifier(
        name="Pistol secondary",
        image_url="https://i.imgur.com/pIIl7j1.png",
    ),
    RandomModifier(
        name="Impact grenades only",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/RGN_View.png/revision/latest?cb=20211212210251",
    ),
)

OK_MODIFIERS = (
    RandomModifier(
        name="Use highest capacity magazine",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/MAG5-100.png/revision/latest/scale-to-width-down/1200?cb=20190414152250",
    ),
    RandomModifier(
        name="Attempt to befriend one random player",
        image_url="https://i.imgur.com/i3KRTCc.png",
    ),
    RandomModifier(
        name="Night raid (NVG if applicable)",
        image_url="https://i.redd.it/juv50kmkgm941.png",
    ),
    RandomModifier(
        name="Flash grenades only",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fc/Model_7290_Flash_Bang.png/revision/latest?cb=20211212182627",
    ),
    RandomModifier(
        name="M67 Hand grenades only",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e2/M67.png/revision/latest/scale-to-width-down/320?cb=20200216033043",
    ),
    RandomModifier(
        name="Use highest flesh damage round available",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/.45_RIP_View.png/revision/latest/scale-to-width-down/211?cb=20200508230152",
    ),
    RandomModifier(
        name="Use highest penetration round available",
        image_url="https://i.imgur.com/l2Zb9aH.png",
    ),
    RandomModifier(
        name="Have 800m+ sighting range",
        image_url="https://www.bestgamingsettings.com/wp-content/uploads/2020/02/EscapeFromTarkovSniping1.jpg",
    ),
)

BAD_MODIFIERS = (
    RandomModifier(
        name="Only smoke grenades",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/M18_Green_View.png/revision/latest?cb=20211212211007",
    ),
    RandomModifier(
        name="No suppressors",
        image_url="https://i.imgur.com/Otrn9Xc.png",
    ),
    RandomModifier(
        name="No insurance",
        image_url="https://i.imgur.com/E5xueS0.png",
    ),
    RandomModifier(
        name="Iron sights only",
        image_url="https://i.imgur.com/oE4qQ4b.png",
    ),
    RandomModifier(
        name="Hip fire only (unbind aim)",
        image_url="https://i.imgur.com/xh2Z6eT.jpg",
    ),
    RandomModifier(
        name="No surgery kits",
        image_url="https://i.imgur.com/ZLf9udj.png",
    ),
    RandomModifier(
        name="No docs/sicc/keytool/keycard holder",
        image_url="https://i.imgur.com/5Rusxe3.png",
    ),
    RandomModifier(
        name="Weapon must be stock",
        image_url="https://i.imgur.com/j3RShdo.png",
    ),
    RandomModifier(
        name="Single-fire only",
        image_url="https://i.imgur.com/yhRZB5H.png",
    ),
    RandomModifier(
        name="Hatchlings must be fought with a melee",
        image_url="https://academyoffencingmasters.com/blog/wp-content/uploads/2017/02/Valentine%E2%80%99s-Day-Love-and-Swordfighting-Duels.jpg",
    ),
    RandomModifier(
        name="No headphones",
        image_url="https://i.imgur.com/FOrgqJm.png",
    ),
    RandomModifier(
        name="Level 1 Meds",
        image_url="https://i.imgur.com/I71LsPN.png",
    ),
    RandomModifier(
        name="No grenades",
        image_url="https://i.imgur.com/8d22sUW.png",
    ),
)

ALL_MODIFIERS = (GOOD_MODIFIERS, OK_MODIFIERS, BAD_MODIFIERS)
