from enum import Enum
from typing import Optional, Literal

#
#   User-Specific Settings
#
#   ------ Trader Levels ------
#   (Rolled items must be available at or below the user's trader levels)
#
#   Prapor:                   1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Therapist:                1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Skier:                    1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Peacekeeper:              1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Mechanic:                 1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Ragman:                   1 / 2 / 3 / 4         (Always unlocked, starts at Loyalty Level 1)
#   Jaeger:               0 / 1 / 2 / 3 / 4         (Trader unlocks after quest completion, hence the '0' option)
#
#   ------ Other Settings ------
#
#   Roll mod/ammo levels:     True / False          (Roll gun mod trader levels and ammo trader levels?)
#   Flea Market Unlocked:     True / False          (Flea Market unlocks at level 15. Allow items that are only available on the Flea Market to be rolled?)
#   Allow Quest-Locked Items: True / False          (Some items are locked behind quest completion. Allow these items to be rolled?)
#   Meta only:                True / False          (Exclusively roll for 'meta' items?)
#   Allow thermals:           True / False          (Can thermal scope be rolled as a random modifier?)
#

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

class Weapons:
    def __init__(self,
            name: str,
            category: Category,
            image_url: str,
            flea: bool,
            trader: Optional[Trader],
            trader_level: Optional[Literal[1, 2, 3, 4]],
            quest_locked: bool,
            meta: bool
    ) -> None:
        self.name = name
        self.category = category
        self.image_url = image_url
        self.flea = flea
        self.trader = trader
        self.trader_level = trader_level
        self.quest_locked = quest_locked
        self.meta = meta

all_weapons = (
    Weapons(
        name="Melee",
        category=Category.MELEE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Antique_Axe.png/revision/latest/scale-to-width-down/200?cb=20181110013042",
        flea=True, trader=Trader.PRAPOR, trader_level=1, quest_locked=False, meta=False
    ),
    Weapons(
        name="ADAR 2-15",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/ADAR2-15Image.png/revision/latest/scale-to-width-down/180?cb=20190226190907",
        flea=True, trader=Trader.SKIER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="AUG A1 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f9/Steyr_AUG_A1_5.56x45_assault_rifle.png/revision/latest/scale-to-width-down/320?cb=20221231014107",
        flea=True, trader=Trader.PEACEKEEPER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="AUG A3 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4a/AUG_A3_Image.png/revision/latest/scale-to-width-down/320?cb=20221231014349",
        flea=True, trader=Trader.PEACEKEEPER, trader_level=3, quest_locked=False, meta=False
    ),

    Weapons(
        name="Kalashnikov AK-101",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/AK101_Image.png/revision/latest/scale-to-width-down/180?cb=20180502204454",
        flea=True, trader=Trader.MECHANIC, trader_level=3, quest_locked=False, meta=True
    ),
    Weapons(
        name="Kalashnikov AK-102",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/Ak102image.png/revision/latest/scale-to-width-down/180?cb=20180506001257",
        flea=True, trader=Trader.MECHANIC, trader_level=3, quest_locked=False, meta=False
    ),
    Weapons(
        name="Kalashnikov AK-103",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/AK-103_7.62x39.png/revision/latest/scale-to-width-down/180?cb=20180429234506",
        flea=True, trader=Trader.PRAPOR, trader_level=3, quest_locked=False, meta=False
    ),
    Weapons(
        name="Kalashnikov AK-104",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b2/AK-104Image.png/revision/latest/scale-to-width-down/180?cb=20180503235112",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AK-105",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/AK-105_5.45x39.png/revision/latest/scale-to-width-down/180?cb=20180429234412",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AK-74",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/AK-74Image.png/revision/latest/scale-to-width-down/180?cb=20181226154054",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AK-74M",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/AK-74M.png/revision/latest/scale-to-width-down/180?cb=20180513014125",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AK-74N",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Akn.png/revision/latest/scale-to-width-down/180?cb=20181028171233",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="Kalashnikov AKM",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/Akm.png/revision/latest/scale-to-width-down/180?cb=20180206133400",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKMN",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Akmn.png/revision/latest/scale-to-width-down/180?cb=20180206133117",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="Kalashnikov AKMS",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Akms.png/revision/latest/scale-to-width-down/180?cb=20180427005729",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKMSN",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/Akmsn.png/revision/latest/scale-to-width-down/180?cb=20180503233021",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKS-74",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/AKS-74.png/revision/latest/scale-to-width-down/180?cb=20181230153732",
        flea=True,
        trader=None,
        trader_level=None,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKS-74N",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/AKS-74N.png/revision/latest/scale-to-width-down/180?cb=20180426173339",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKS-74U",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Aks74u.png/revision/latest/scale-to-width-down/180?cb=20181028171406",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKS-74UB",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/Aks74ub.png/revision/latest/scale-to-width-down/180?cb=20181028171415",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Kalashnikov AKS-74UN",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Aks74un.png/revision/latest/scale-to-width-down/180?cb=20181028171353",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="ASh-12",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/ASh_12.png/revision/latest/scale-to-width-down/180?cb=20211206013813",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=4,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="AS VAL",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1c/Asval.png/revision/latest/scale-to-width-down/180?cb=20190305220933",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=4,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="CMMG Mk47 Mutant",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Mk47_Mutant_View.png/revision/latest/scale-to-width-down/180?cb=20211203223357",
        flea=False,
        trader=Trader.SKIER,
        trader_level=4,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="DT MDR 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/DT_MDR_5.56x45_ASSAULT_RIFLE.png/revision/latest/scale-to-width-down/180?cb=20190411211744",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="DT MDR 7.62x51",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/33/DT_MDR_308.png/revision/latest/scale-to-width-down/180?cb=20191228210602",
        flea=False,
        trader=Trader.PEACEKEEPER,
        trader_level=4,
        quest_locked=True,
        meta=True,
    ),
    Weapons(
        name="HK 416A5",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/HK416Image.png/revision/latest/scale-to-width-down/180?cb=20181226145352",
        flea=True,
        trader=Trader.MECHANIC,
        trader_level=4,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="Colt M4A1",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/29/M4a1.png/revision/latest/scale-to-width-down/180?cb=20181028172147",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=2,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="FN SCAR-L (Mk 16)",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/00/SCAR-L_Insp.gif/revision/latest/scale-to-width-down/180?cb=20220101204420",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="FN SCAR-H (Mk 17)",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a8/ScarH_Image.gif/revision/latest/scale-to-width-down/180?cb=20220220215829",
        flea=False,
        trader=Trader.PEACEKEEPER,
        trader_level=4,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="SIG MCX .300 BLK",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/-92ucz5kq_Y.jpg/revision/latest/scale-to-width-down/180?cb=20201226014736",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="DS Arms SA-58",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/DS_Arms_SA-58_OSW_Para_7.62x51.png/revision/latest/scale-to-width-down/180?cb=20181028172156",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Lone Star TX-15 DML",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/TX-15_View.PNG/revision/latest/scale-to-width-down/180?cb=20191103030150",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=True,
        meta=False,
    ),
    Weapons(
        name="Molot VPO-209",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b0/Vpo209.png/revision/latest/scale-to-width-down/180?cb=20181028171328",
        flea=True,
        trader=Trader.SKIER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Molot VPO-136 \"Vepr KM\"",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Vpo136.png/revision/latest/scale-to-width-down/180?cb=20181028171300",
        flea=True,
        trader=Trader.SKIER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Simonov OP-SKS",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/Opsks.png/revision/latest/scale-to-width-down/180?cb=20190414112410",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Simonov SKS (No Dovetail)",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Sks.png/revision/latest/scale-to-width-down/180?cb=20190414112401",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="VPO-101 \"Vepr-Hunter\"",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/VeprHunterImage.png/revision/latest/scale-to-width-down/180?cb=20190410211507",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="RPK-16",
        category=Category.MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/RPK-16.png/revision/latest/scale-to-width-down/180?cb=20181226153306",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=4,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK MP5",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Mp5.png/revision/latest/scale-to-width-down/180?cb=20180507221414",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK MP5K",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/45/HK_MP5K-N.png/revision/latest/scale-to-width-down/180?cb=20211206013958",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK MP7A1",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/HKMP7A1Image.png/revision/latest/scale-to-width-down/180?cb=20181111215340",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK MP7A2",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/52/HKMP7A2Image.png/revision/latest/scale-to-width-down/180?cb=20181111214757",
        flea=True,
        trader=None,
        trader_level=None,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="B&T MP9",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/MP9_View.png/revision/latest/scale-to-width-down/180?cb=20211206014311",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=True,
        meta=False,
    ),
    Weapons(
        name="B&T MP9-N",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/B%26T_MP9-N_9x19_Submachinegun.png/revision/latest/scale-to-width-down/180?cb=20211206014309",
        flea=True,
        trader=None,
        trader_level=None,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="SIG MPX",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f7/Mpx.png/revision/latest/scale-to-width-down/180?cb=20180219121907",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="FN P90",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/P90Image.png/revision/latest/scale-to-width-down/180?cb=20191109011038",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="PP-19-01 Vityaz-SN",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/Pp19.png/revision/latest/scale-to-width-down/180?cb=20180219121911",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="PP-9 \"Klin\"",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/48/Klin.png/revision/latest/scale-to-width-down/180?cb=20180219121903",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="PP-91 \"Kedr\"",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/Kedr.png/revision/latest/scale-to-width-down/180?cb=20180219121901",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="PP-91-01 \"Kedr-B\"",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a4/Kedrb.png/revision/latest/scale-to-width-down/180?cb=20180219121902",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="PPSH-41",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/PPSH-41_View.png/revision/latest/scale-to-width-down/180?cb=20211206010213",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Saiga-9",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/Saiga9.png/revision/latest/scale-to-width-down/180?cb=20180219121912",
        flea=True,
        trader=Trader.SKIER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Soyuz-TM STM-9",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/STM-9_Base_View.png/revision/latest/scale-to-width-down/180?cb=20211206010453",
        flea=True,
        trader=Trader.SKIER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK UMP 45",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/UMP45_View.png/revision/latest/scale-to-width-down/180?cb=20211206010703",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="KRISS Vector .45",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/Vector45_fir_unloaded_view.png/revision/latest/scale-to-width-down/180?cb=20211206011407",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=True,
        meta=False,
    ),
    Weapons(
        name="KRISS Vector 9x19",
        category=Category.SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9e/Vector_9x19_View.png/revision/latest/scale-to-width-down/180?cb=20211206011601",
        flea=True,
        trader=Trader.SKIER,
        trader_level=2,
        quest_locked=True,
        meta=False,
    ),
    Weapons(
        name="Mossberg 590A1 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/M590A1_View.png/revision/latest/scale-to-width-down/180?cb=20211206014100",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Remington M870 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/M870.png/revision/latest/scale-to-width-down/180?cb=20180426140946",
        flea=True,
        trader=Trader.SKIER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="MP-133 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/Mr133.png/revision/latest/scale-to-width-down/180?cb=20180219121908",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="MP-153 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/Mp153.png/revision/latest/scale-to-width-down/180?cb=20180219121906",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="MP-155 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/MP-155.png/revision/latest/scale-to-width-down/180?cb=20211205210153",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Baikal MP-43-1C 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/MP-43-1C_12ga_double-barrel_shotgun.jpg/revision/latest/scale-to-width-down/180?cb=20211213051714",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="MTs-255-12 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2d/EFT_UpcomingMTs255.png/revision/latest/scale-to-width-down/180?cb=20190515021208",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Saiga-12 12ga ver.10 12/76",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Saiga12.png/revision/latest/scale-to-width-down/180?cb=20180219121914",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="TOZ-106 20ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/Toz.png/revision/latest/scale-to-width-down/180?cb=20180219121918",
        flea=True,
        trader=Trader.SKIER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="TOZ KS-23M 23x75mm",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/KS-23M.png/revision/latest/scale-to-width-down/180?cb=20201019145716",
        flea=False,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK G28 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/18/G28_Full.png/revision/latest/scale-to-width-down/180?cb=20211214013521",
        flea=False,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="Springfield Armory M1A 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/M1A_Icon.png/revision/latest/scale-to-width-down/180?cb=20180503234958",
        flea=False,
        trader=Trader.MECHANIC,
        trader_level=2,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="SWORD International Mk-18 .338 LM",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a2/Mk18.png/revision/latest/scale-to-width-down/180?cb=20210102132503",
        flea=False,
        trader=Trader.JAEGER,
        trader_level=4,
        quest_locked=True,
        meta=True,
    ),
    Weapons(
        name="Kel-Tec RFB 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/KT_RFB.png/revision/latest/scale-to-width-down/180?cb=20201019134602",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Remington R11 RSASS 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9b/Rsass.png/revision/latest/scale-to-width-down/180?cb=20181122021513",
        flea=False,
        trader=Trader.PEACEKEEPER,
        trader_level=4,
        quest_locked=True,
        meta=True,
    ),
    Weapons(
        name="Knight's Armament Company SR-25 7.62x51",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/69/SR-25_View.png/revision/latest/scale-to-width-down/180?cb=20191227220256",
        flea=False,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="SVDS 7.62x54R",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8f/SVD-S.png/revision/latest/scale-to-width-down/180?cb=20190411211731",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="VSS Vintorez 9x39",
        category=Category.MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/Vss.png/revision/latest/scale-to-width-down/180?cb=20210114170659",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=True,
    ),
    Weapons(
        name="LOBAEV Arms DVL-10 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/Dvl10.png/revision/latest/scale-to-width-down/180?cb=20180219121859",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Remington M700 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/M700Image.png/revision/latest/scale-to-width-down/180?cb=20181226171021",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Mosin 7.62x54R (Sniper)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/MosinInspect.png/revision/latest/scale-to-width-down/180?cb=20180918200314",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Mosin 7.62x54R (Infantry)",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d4/MosinInfantryImage.png/revision/latest/scale-to-width-down/180?cb=20181226165344",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="SV-98 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Sv98.png/revision/latest/scale-to-width-down/180?cb=20180427101420",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Orsis T-5000M 7.62x51",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/T-5000_View.png/revision/latest/scale-to-width-down/180?cb=20200216013517",
        flea=True,
        trader=Trader.SKIER,
        trader_level=3,
        quest_locked=True,
        meta=False,
    ),
    Weapons(
        name="Molot VPO-215 \"Gornostay\" .366 TKM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4e/VPO-215_View.png/revision/latest/scale-to-width-down/180?cb=20200216013459",
        flea=True,
        trader=Trader.JAEGER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="HK USP .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ad/Usp1.png/revision/latest/scale-to-width-down/180?cb=20220118221605",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="APB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/APBImage.png/revision/latest/scale-to-width-down/400?cb=20200216023044",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Stechkin APS 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Stechkin_Automatic_Pistol_9x18PM.png/revision/latest/scale-to-width-down/200?cb=20200216021943",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="FN Five-seveN 5.7x28",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/Five-seveN.gif/revision/latest/scale-to-width-down/200?cb=20191109004734",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Glock 17 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Glock17.png/revision/latest/scale-to-width-down/200?cb=20200216022006",
        flea=True,
        trader=Trader.MECHANIC,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Glock 18C 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Glock18CImage.png/revision/latest/scale-to-width-down/200?cb=20200216022017",
        flea=True,
        trader=Trader.MECHANIC,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Glock 19X 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/G19X_View.png/revision/latest?cb=20221231013454",
        flea=True,
        trader=Trader.SKIER,
        trader_level=2,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Colt M1911A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bd/M1911A1_View.png/revision/latest/scale-to-width-down/200?cb=20200508214809",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Colt M45A1 .45 ACP",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c3/M45A1.png/revision/latest/scale-to-width-down/200?cb=20201019153037",
        flea=True,
        trader=None,
        trader_level=None,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Beretta M9A3 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/EFT_UpcomingM9A3.png/revision/latest/scale-to-width-down/200?cb=20200216022039",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Yarygin MP-443 \"Grach\" 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/Grach.png/revision/latest/scale-to-width-down/200?cb=20200216022052",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="SIG P226R 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c6/P226.png/revision/latest/scale-to-width-down/200?cb=20200216022104",
        flea=True,
        trader=Trader.PEACEKEEPER,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="PB 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Pb.png/revision/latest/scale-to-width-down/200?cb=20200216023013",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Lebedev PL15 9x19",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/PL-15image.png/revision/latest/scale-to-width-down/200?cb=20211206010342",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Makarov PM (t) 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/Makarovt.png/revision/latest/scale-to-width-down/200?cb=20200216022116",
        flea=True,
        trader=None,
        trader_level=None,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Makarov PM 9x18PM",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/Makarov.png/revision/latest/scale-to-width-down/200?cb=20200216022127",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="Serdyukov SR-1MP Gyurza 9x21",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cc/Sr1mp.png/revision/latest/scale-to-width-down/200?cb=20200216022136",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=3,
        quest_locked=False,
        meta=False,
    ),
    Weapons(
        name="TT-33 7.62x25",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Tt.png/revision/latest/scale-to-width-down/200?cb=20200216022150",
        flea=True, trader=Trader.PRAPOR, trader_level=1, quest_locked=False, meta=False
    ),
    Weapons(
        name="TT-33 7.62x25 (Golden)",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/46/TT_Pistol_7.62x25_TT_gold_2.png/revision/latest/scale-to-width-down/200?cb=20200216022203",
        flea=True, trader=None, trader_level=None, quest_locked=False, meta=False
    ),
    Weapons(
        name="Chiappa Rhino 200DS 9x19mm",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/CR_200DS_1.png/revision/latest/scale-to-width-down/180?cb=20220416231853",
        flea=True, trader=Trader.JAEGER, trader_level=1, quest_locked=False, meta=False
    ),
    Weapons(
        name="Chiappa Rhino 50DS .357",
        category=Category.PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9c/CR_50DS_.357_1.png/revision/latest/scale-to-width-down/180?cb=20220417132057",
        flea=True, trader=Trader.JAEGER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="HK G36 5.56x45",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/G36_View.png/revision/latest/scale-to-width-down/180?cb=20220705223014",
        flea=True, trader=Trader.PEACEKEEPER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="Benelli M3 Super 90 dual-mode 12ga",
        category=Category.SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Benelli_M3_Super_90.png/revision/latest/scale-to-width-down/180?cb=20220703180524",
        flea=True, trader=Trader.JAEGER, trader_level=2, quest_locked=True, meta=False
    ),
    Weapons(
        name="Accuracy International AXMC .338 LM",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/AXMC_.338_LM.png/revision/latest/scale-to-width-down/180?cb=20220705212920",
        flea=False, trader=Trader.JAEGER, trader_level=4, quest_locked=True, meta=False
    ),
    Weapons(
        name="MP-18 7.62x54R",
        category=Category.SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/MP18_VIew.png/revision/latest/scale-to-width-down/180?cb=20220629224646",
        flea=True, trader=Trader.JAEGER, trader_level=1, quest_locked=False, meta=False
    ),
    Weapons(
        name="Rifle Dynamics RD-704 7.62x39",
        category=Category.ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ce/RD-704.jpg/revision/latest/scale-to-width-down/180?cb=20220702095109",
        flea=False, trader=Trader.MECHANIC, trader_level=4, quest_locked=False, meta=True
    ),
    Weapons(
        name="SAG AK-545 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/SAG.545.png/revision/latest/scale-to-width-down/180?cb=20220701160057",
        flea=True, trader=Trader.SKIER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="SAG AK-545 Short 5.45x39",
        category=Category.ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/AK-545Short_View.png/revision/latest/scale-to-width-down/180?cb=202206292156099",
        flea=True, trader=Trader.SKIER, trader_level=2, quest_locked=False, meta=False
    ),
    Weapons(
        name="FN40GL Mk2 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b8/FNGL40inspect.png/revision/latest/scale-to-width-down/180?cb=20211206014144",
        flea=False, trader=Trader.PEACEKEEPER, trader_level=4, quest_locked=True, meta=False
    ),
    Weapons(
        name="Milkor M32A1 MSGL 40mm",
        category=Category.GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/M32A1inspect.png/revision/latest/scale-to-width-down/180?cb=20220704113236",
        flea=False, trader=None, trader_level=None, quest_locked=False, meta=False
    ),
)

class Armor:
    def __init__(self,
                 name: str,
                 category: Category,
                 image_url: str,
                 flea: bool,
                 trader: Optional[Trader],
                 trader_level: Optional[Literal[1, 2, 3, 4]],
                 quest_locked: bool,
                 meta: bool):
        self.name = name
        self.category = category
        self.image_url = image_url
        self.flea = flea
        self.trader = trader
        self.trader_level = trader_level
        self.quest_locked = quest_locked
        self.meta = meta

armor_vests = (
    Armor(
        name="No Armor",
        category=Category.ARMOR_VEST,
        image_url="https://i.imgur.com/V2SWmZh.png",
        flea=True, trader=Trader.PRAPOR, trader_level=1, quest_locked=False, meta=False,
    ),
    Armor(
        name="BNTI Module-3M body armor",
        category=Category.ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f8/3M_icon.png/revision/latest/scale-to-width-down/190?cb=20190519124804",
        flea=True, trader=None, trader_level=None, quest_locked=False, meta=False,
    ),
)

armored_rigs = (
    # stuff
)

all_armors = armor_vests + armored_rigs

class Rig:
    def __init__(
            self,
            name: str,
            image_url: str,
            flea: bool,
            trader: Optional[Trader],
            trader_level: Optional[Literal[1, 2, 3, 4]],
            meta: bool,
    ):
        self.name = name
        self.category = Category.RIG
        self.image_url = image_url
        self.flea = flea
        self.trader = trader
        self.trader_level = trader_level
        self.meta = meta

all_rigs = (
    Rig(
        name="No Rig",
        image_url="",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        meta=False,
    ),
)

class Helmet:
    def __init__(self, name: str, image_url: str, flea: bool, trader: Optional[Trader], trader_level: Optional[Literal[1, 2, 3, 4]], quest_locked: bool, meta: bool):
        self.name = name
        self.category = Category.HELMET
        self.image_url = image_url
        self.flea = flea
        self.trader = trader
        self.trader_level = trader_level
        self.quest_locked = quest_locked
        self.meta = meta

all_helmets = (
    Helmet(
        name="No Helmet",
        image_url="",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
    ),
)

class Backpack:
    def __init__(self, name: str, image_url: str, flea: bool, trader: Optional[Trader], trader_level: Optional[Literal[1, 2, 3, 4]], quest_locked: bool, meta: bool):
        self.name = name
        self.category = Category.BACKPACK
        self.image_url = image_url
        self.flea = flea
        self.trader = trader
        self.trader_level = trader_level
        self.quest_locked = quest_locked
        self.meta = meta

all_backpacks = (
    Backpack(
        name="No Backpack",
        image_url="",
        flea=True,
        trader=Trader.PRAPOR,
        trader_level=1,
        quest_locked=False,
        meta=False,
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