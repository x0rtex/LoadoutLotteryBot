from typing import NamedTuple
from dataclasses import dataclass

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
YOU_CHOOSE_IMAGE: str = "https://clipartix.com/wp-content/uploads/2018/03/you-clipart-2018-14.jpg"


class TraderInfo(NamedTuple):
    level: 1 | 2 | 3 | 4  # Trader loyalty level
    quest_locked: bool  # Whether an item is locked behind a trader's quest or not
    barter: bool  # Whether an item is only obtainable via barter or not


@dataclass(slots=True, frozen=True)
class Item:
    name: str
    category: str
    image_url: str
    unlocked: bool
    meta: bool
    flea: bool
    trader_info: dict[str, TraderInfo]


ALL_WEAPONS: tuple = (
    Item(
        name=YOUR_CHOICE,
        category=WEAPON,
        image_url=YOU_CHOOSE_IMAGE,
        unlocked=True,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Bars A-2607 95Kh18 knife",
        category=MELEE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/Bars_A-2607-_95x18.png/revision/latest/scale-to-width-down/320?cb=20221225020013",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
    Item(
        name="ADAR 2-15 5.56x45",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/ADAR2-15Image.png/revision/latest/scale-to-width-down/180?cb=20190226190907",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Steyr AUG A1 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f9/Steyr_AUG_A1_5.56x45_assault_rifle.png/revision/latest/scale-to-width-down/320?cb=20221231014107",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Steyr AUG A3 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4a/AUG_A3_Image.png/revision/latest/scale-to-width-down/320?cb=20221231014349",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-101 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/AK101_Image.png/revision/latest/scale-to-width-down/180?cb=20180502204454",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-102 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/Ak102image.png/revision/latest/scale-to-width-down/180?cb=20180506001257",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-103 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/AK-103_7.62x39.png/revision/latest/scale-to-width-down/180?cb=20180429234506",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-104 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b2/AK-104Image.png/revision/latest/scale-to-width-down/180?cb=20180503235112",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AK-105 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/AK-105_5.45x39.png/revision/latest/scale-to-width-down/180?cb=20180429234412",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-74 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/AK-74Image.png/revision/latest/scale-to-width-down/180?cb=20181226154054",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AK-74M 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/AK-74M.png/revision/latest/scale-to-width-down/180?cb=20180513014125",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AK-74N 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Akn.png/revision/latest/scale-to-width-down/180?cb=20181028171233",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Kalashnikov AKM 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/Akm.png/revision/latest/scale-to-width-down/180?cb=20180206133400",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMN 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Akmn.png/revision/latest/scale-to-width-down/180?cb=20180206133117",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMS 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Akms.png/revision/latest/scale-to-width-down/180?cb=20180427005729",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKMSN 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/Akmsn.png/revision/latest/scale-to-width-down/180?cb=20180503233021",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/AKS-74.png/revision/latest/scale-to-width-down/180?cb=20181230153732",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={},
    ),
    Item(
        name="Kalashnikov AKS-74N 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/AKS-74N.png/revision/latest/scale-to-width-down/180?cb=20180426173339",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74U 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Aks74u.png/revision/latest/scale-to-width-down/180?cb=20181028171406",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74UB 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/Aks74ub.png/revision/latest/scale-to-width-down/180?cb=20181028171415",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Kalashnikov AKS-74UN 5.45x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Aks74un.png/revision/latest/scale-to-width-down/180?cb=20181028171353",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="ASh-12 12.7x55",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/ASh_12.png/revision/latest/scale-to-width-down/180?cb=20211206013813",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="AS VAL 9x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1c/Asval.png/revision/latest/scale-to-width-down/180?cb=20190305220933",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="CMMG Mk47 Mutant 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Mk47_Mutant_View.png/revision/latest/scale-to-width-down/180?cb=20211203223357",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            SKIER: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Desert Tech MDR 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/DT_MDR_5.56x45_assault_rifle.png/revision/latest/scale-to-width-down/180?cb=20190411211744",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Desert Tech MDR 7.62x51",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/33/DT_MDR_308.png/revision/latest/scale-to-width-down/180?cb=20191228210602",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="HK 416A5 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/HK416Image.png/revision/latest/scale-to-width-down/180?cb=20181226145352",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=True, barter=False),
            MECHANIC: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M4A1 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/29/M4a1.png/revision/latest/scale-to-width-down/180?cb=20181028172147",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="FN SCAR-L (Mk 16) 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/00/SCAR-L_Insp.gif/revision/latest/scale-to-width-down/180?cb=20220101204420",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=2, quest_locked=True, barter=True),
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN SCAR-H (Mk 17) 7.62x51",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a8/ScarH_Image.gif/revision/latest/scale-to-width-down/180?cb=20220220215829",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="SIG MCX .300 BLK",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/-92ucz5kq_Y.jpg/revision/latest/scale-to-width-down/180?cb=20201226014736",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="DS Arms SA-58 7.62x51",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/DS_Arms_SA-58_OSW_Para_7.62x51.png/revision/latest/scale-to-width-down/180?cb=20181028172156",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Lone Star TX-15 DML 5.56x45",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/TX-15_View.PNG/revision/latest/scale-to-width-down/180?cb=20191103030150",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
            SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Molot VPO-209 .366 TKM",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b0/Vpo209.png/revision/latest/scale-to-width-down/180?cb=20181028171328",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Molot VPO-136 \"Vepr KM\" 7.62x39",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Vpo136.png/revision/latest/scale-to-width-down/180?cb=20181028171300",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Simonov OP-SKS 7.62x39",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/Opsks.png/revision/latest/scale-to-width-down/180?cb=20190414112410",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Simonov SKS 7.62x39 (No Dovetail)",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Sks.png/revision/latest/scale-to-width-down/180?cb=20190414112401",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="VPO-101 \"Vepr-Hunter\" 7.62x51",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/VeprHunterImage.png/revision/latest/scale-to-width-down/180?cb=20190410211507",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="RPK-16 5.45x39",
        category=MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/RPK-16.png/revision/latest/scale-to-width-down/180?cb=20181226153306",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP5 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Mp5.png/revision/latest/scale-to-width-down/180?cb=20180507221414",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP5K 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/45/HK_MP5K-N.png/revision/latest/scale-to-width-down/180?cb=20211206013958",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK MP7A1 4.6x30",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/HKMP7A1Image.png/revision/latest/scale-to-width-down/180?cb=20181111215340",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK MP7A2 4.6x30",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/52/HKMP7A2Image.png/revision/latest/scale-to-width-down/180?cb=20181111214757",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="B&T MP9 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/MP9_View.png/revision/latest/scale-to-width-down/180?cb=20211206014311",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="B&T MP9-N 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/B%26T_MP9-N_9x19_Submachinegun.png/revision/latest/scale-to-width-down/180?cb=20211206014309",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={},
    ),
    Item(
        name="SIG MPX 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f7/Mpx.png/revision/latest/scale-to-width-down/180?cb=20180219121907",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="FN P90 5.7x28",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/P90Image.png/revision/latest/scale-to-width-down/180?cb=20191109011038",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=True),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="PP-19-01 \"Vityaz\" 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/Pp19.png/revision/latest/scale-to-width-down/180?cb=20180219121911",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="PP-9 \"Klin\" 9x18PMM",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/48/Klin.png/revision/latest/scale-to-width-down/180?cb=20180219121903",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="PP-91 \"Kedr\" 9x18PM",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/Kedr.png/revision/latest/scale-to-width-down/180?cb=20180219121901",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PP-91-01 \"Kedr-B\" 9x18PM",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a4/Kedrb.png/revision/latest/scale-to-width-down/180?cb=20180219121902",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PPSh-41 7.62x25",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/PPSH-41_View.png/revision/latest/scale-to-width-down/180?cb=20211206010213",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Saiga-9 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/Saiga9.png/revision/latest/scale-to-width-down/180?cb=20180219121912",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Soyuz-TM STM-9 Gen.2 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/STM-9_Base_View.png/revision/latest/scale-to-width-down/180?cb=20211206010453",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK UMP .45 ACP",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/UMP45_View.png/revision/latest/scale-to-width-down/180?cb=20211206010703",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TDI KRISS Vector Gen.2 .45 ACP",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/Vector45_fir_unloaded_view.png/revision/latest/scale-to-width-down/180?cb=20211206011407",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="TDI KRISS Vector Gen.2 9x19",
        category=SMG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9e/Vector_9x19_View.png/revision/latest/scale-to-width-down/180?cb=20211206011601",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Mossberg 590A1 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/M590A1_View.png/revision/latest/scale-to-width-down/180?cb=20211206014100",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Remington Model 870 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/M870.png/revision/latest/scale-to-width-down/180?cb=20180426140946",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=True, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-133 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/Mr133.png/revision/latest/scale-to-width-down/180?cb=20180219121908",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-153 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/Mp153.png/revision/latest/scale-to-width-down/180?cb=20180219121906",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
            SKIER: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="MP-155 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/MP-155.png/revision/latest/scale-to-width-down/180?cb=20211205210153",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Baikal MP-43-1C 12ga double-barrel",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/MP-43-1C_12ga_double-barrel_shotgun.jpg/revision/latest/scale-to-width-down/180?cb=20211213051714",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="MP-43 12ga sawed-off double-barrel",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/60/MP-43_Sawed_Off_Image.png/revision/latest/scale-to-width-down/320?cb=20230822003753",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="MTs-255-12 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2d/EFT_UpcomingMTs255.png/revision/latest/scale-to-width-down/180?cb=20190515021208",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Saiga-12 12ga ver.10 12/76",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Saiga12.png/revision/latest/scale-to-width-down/180?cb=20180219121914",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="TOZ-106 20ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/Toz.png/revision/latest/scale-to-width-down/180?cb=20180219121918",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=False, barter=False),
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="TOZ KS-23M 23x75mm",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/KS-23M.png/revision/latest/scale-to-width-down/180?cb=20201019145716",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="HK G28 7.62x51",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/18/G28_Full.png/revision/latest/scale-to-width-down/180?cb=20211214013521",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=True),
            JAEGER: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Springfield Armory M1A 7.62x51",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/M1A_Icon.png/revision/latest/scale-to-width-down/180?cb=20180503234958",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="SWORD International Mk-18 .338 LM",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a2/Mk18.png/revision/latest/scale-to-width-down/180?cb=20210102132503",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={},
    ),
    Item(
        name="Kel-Tec RFB 7.62x51",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/KT_RFB.png/revision/latest/scale-to-width-down/180?cb=20201019134602",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Remington R11 RSASS 7.62x51",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9b/Rsass.png/revision/latest/scale-to-width-down/180?cb=20181122021513",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Knight's Armament Company SR-25 7.62x51",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/69/SR-25_View.png/revision/latest/scale-to-width-down/180?cb=20191227220256",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SVDS 7.62x54R",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8f/SVD-S.png/revision/latest/scale-to-width-down/180?cb=20190411211731",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="VSS Vintorez 9x39",
        category=MARKSMAN_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/Vss.png/revision/latest/scale-to-width-down/180?cb=20210114170659",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="LOBAEV Arms DVL-10 7.62x51",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/Dvl10.png/revision/latest/scale-to-width-down/180?cb=20180219121859",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Remington Model 700 7.62x51",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/M700Image.png/revision/latest/scale-to-width-down/180?cb=20181226171021",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True),
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Mosin 7.62x54R (Sniper)",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/MosinInspect.png/revision/latest/scale-to-width-down/180?cb=20180918200314",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=True)
        },
    ),
    Item(
        name="Mosin 7.62x54R (Infantry)",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d4/MosinInfantryImage.png/revision/latest/scale-to-width-down/180?cb=20181226165344",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SV-98 7.62x54R",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Sv98.png/revision/latest/scale-to-width-down/180?cb=20180427101420",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
            JAEGER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Orsis T-5000M 7.62x51",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/T-5000_View.png/revision/latest/scale-to-width-down/180?cb=20200216013517",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=3, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Molot VPO-215 \"Gornostay\" .366 TKM",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4e/VPO-215_View.png/revision/latest/scale-to-width-down/180?cb=20200216013459",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="HK USP .45 ACP",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ad/Usp1.png/revision/latest/scale-to-width-down/180?cb=20220118221605",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=2, quest_locked=False, barter=False)
        },
    ),
    Item(
        name="APB 9x18PM",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/APBImage.png/revision/latest/scale-to-width-down/400?cb=20200216023044",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Stechkin APS 9x18PM",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Stechkin_Automatic_Pistol_9x18PM.png/revision/latest/scale-to-width-down/200?cb=20200216021943",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN Five-seveN MK2 5.7x28",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/Five-seveN.gif/revision/latest/scale-to-width-down/200?cb=20191109004734",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 17 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Glock17.png/revision/latest/scale-to-width-down/200?cb=20200216022006",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 18C 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Glock18CImage.png/revision/latest/scale-to-width-down/200?cb=20200216022017",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Glock 19X 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/G19X_View.png/revision/latest?cb=20221231013454",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M1911A1 .45 ACP",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bd/M1911A1_View.png/revision/latest/scale-to-width-down/200?cb=20200508214809",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Colt M45A1 .45 ACP",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c3/M45A1.png/revision/latest/scale-to-width-down/200?cb=20201019153037",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={},
    ),
    Item(
        name="Beretta M9A3 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/EFT_UpcomingM9A3.png/revision/latest/scale-to-width-down/200?cb=20200216022039",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Yarygin MP-443 'Grach' 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/Grach.png/revision/latest/scale-to-width-down/200?cb=20200216022052",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SIG P226R 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c6/P226.png/revision/latest/scale-to-width-down/200?cb=20200216022104",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="PB 9x18PM",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Pb.png/revision/latest/scale-to-width-down/200?cb=20200216023013",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Lebedev PL-15 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/PL-15image.png/revision/latest/scale-to-width-down/200?cb=20211206010342",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Makarov PM (t) 9x18PM",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/Makarovt.png/revision/latest/scale-to-width-down/200?cb=20200216022116",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={},
    ),
    Item(
        name="Makarov PM 9x18PM",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/Makarov.png/revision/latest/scale-to-width-down/200?cb=20200216022127",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Serdyukov SR-1MP Gyurza 9x21",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cc/Sr1mp.png/revision/latest/scale-to-width-down/200?cb=20200216022136",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TT-33 7.62x25",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Tt.png/revision/latest/scale-to-width-down/200?cb=20200216022150",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="TT-33 7.62x25 (Golden)",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/46/TT_Weapon.Pistol_7.62x25_TT_gold_2.png/revision/latest/scale-to-width-down/200?cb=20200216022203",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={},
    ),
    Item(
        name="Chiappa Rhino 200DS 9x19",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/CR_200DS_1.png/revision/latest/scale-to-width-down/180?cb=20220416231853",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Chiappa Rhino 50DS .357",
        category=PISTOL,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9c/CR_50DS_.357_1.png/revision/latest/scale-to-width-down/180?cb=20220417132057",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=False),
            SKIER: TraderInfo(level=2, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="HK G36 5.56x45",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/G36_View.png/revision/latest/scale-to-width-down/180?cb=20220705223014",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Benelli M3 Super 90 dual-mode 12ga",
        category=SHOTGUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Benelli_M3_Super_90.png/revision/latest/scale-to-width-down/180?cb=20220703180524",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="Accuracy International AXMC .338 LM",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/AXMC_.338_LM.png/revision/latest/scale-to-width-down/180?cb=20220705212920",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            JAEGER: TraderInfo(level=4, quest_locked=True, barter=False),
        },
    ),
    Item(
        name="MP-18 7.62x54R",
        category=SNIPER_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/MP18_VIew.png/revision/latest/scale-to-width-down/180?cb=20220629224646",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Rifle Dynamics RD-704 7.62x39",
        category=ASSAULT_RIFLE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ce/RD-704.jpg/revision/latest/scale-to-width-down/180?cb=20220702095109",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            MECHANIC: TraderInfo(level=4, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SAG AK-545 5.45x39",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/SAG.545.png/revision/latest/scale-to-width-down/180?cb=20220701160057",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="SAG AK-545 Short 5.45x39",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/AK-545Short_View.png/revision/latest/scale-to-width-down/180?cb=202206292156099",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="FN40GL Mk2 40mm",
        category=GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b8/FNGL40inspect.png/revision/latest/scale-to-width-down/180?cb=20211206014144",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=True),
        },
    ),
    Item(
        name="Milkor M32A1 MSGL 40mm",
        category=GRENADE_LAUNCHER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/M32A1inspect.png/revision/latest/scale-to-width-down/180?cb=20220704113236",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Tokarev SVT-40 7.62x54R",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c2/SVT-40_STD_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064627",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=2, quest_locked=False, barter=False),
        },
    ),
    Item(
        name="Tokarev AVT-40 7.62x54R",
        category=ASSAULT_CARBINE,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/AVT-40_STD_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064626",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PRAPOR: TraderInfo(level=3, quest_locked=False, barter=True),
        },
    ),
    Item(
        name="Kalashikov PKM 7.62x54R",
        category=MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/db/PKM_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064623",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Kalashikov PKP 7.62x54R",
        category=MACHINE_GUN,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/be/Pkp-full.png/revision/latest/scale-to-width-down/320?cb=20230811193939",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
)

ALL_ARMOR_VESTS: tuple = (
    Item(
        name=YOUR_CHOICE,
        category=ARMOR_VEST,
        image_url=YOU_CHOOSE_IMAGE,
        unlocked=True,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="BNTI Module-3M body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f8/3M_icon.png/revision/latest/scale-to-width-down/190?cb=20190519124804",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="PACA Soft Armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/25/PACA_Soft_Armor.png/revision/latest/scale-to-width-down/320?cb=20190301085818",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="PACA Soft Armor (Rivals Edition)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/41/PACA_Soft_Armor_%28Rivals_Edition%29.PNG/revision/latest/scale-to-width-down/304?cb=20211231213516",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="6B2 body armor (Flora)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/87/6B2_View.png/revision/latest/scale-to-width-down/320?cb=20191227220309",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="MF-UNTAR body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/MF-UNTAR_Armor_vest.png/revision/latest/scale-to-width-down/320?cb=20180520205929",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BNTI Zhuk-3 body armor (Press)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/76/Zhuk-3_Press_armor.png/revision/latest/scale-to-width-down/296?cb=20190301085839",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            SKIER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="6B23-1 body armor (Digital Flora)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d3/6b23-1.png/revision/latest/scale-to-width-down/302?cb=20190301085852",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="DRD body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/DRD_body_armor_2.png/revision/latest/scale-to-width-down/320?cb=20220703010536",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="BNTI Kirasa-N body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/83/BNTI-Kirasa-N-armor.png/revision/latest/scale-to-width-down/312?cb=20190301085905",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="NFM THOR Concealable Reinforced Vest body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e7/Thor_View.png/revision/latest/scale-to-width-down/320?cb=20211205235338",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="HighCom Trooper TFO body armor (Multicam)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/09/Highcom_Trooper_TFO_armor_%28multicam%29.png/revision/latest/scale-to-width-down/319?cb=20190301085944",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="6B13 assault armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/6B13_assault_armor.gif/revision/latest/scale-to-width-down/320?cb=20190101213615",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B23-2 body armor (Mountain Flora)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7f/6B23-2_armorImage.png/revision/latest/scale-to-width-down/273?cb=20190301085921",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hexatac HPC Plate Carrier (Multicam Black)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/HPC3.PNG/revision/latest/scale-to-width-down/320?cb=20221230210248",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Korund-VM body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/db/KORUND.png/revision/latest/scale-to-width-down/320?cb=20201019171744",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="FORT Redut-M body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7b/FORT_Redut-M_body_armor.png/revision/latest/scale-to-width-down/320?cb=20190410224156",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B13 M modified assault armor (Tan)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/6B13_M.png/revision/latest/scale-to-width-down/281?cb=20190301085955",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="IOTV Gen4 body armor (High Mobility Kit)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2f/IOTV_HMK.png/revision/latest/scale-to-width-down/272?cb=20190710085120",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="BNTI Gzhel-K body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5a/GZHELK-Image.PNG/revision/latest/scale-to-width-down/320?cb=20180520205529",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="FORT Defender-2 body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/Defender-2_View.png/revision/latest/scale-to-width-down/320?cb=20200528221930",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="IOTV Gen4 body armor (Assault Kit)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/95/IOTV_Assault.png/revision/latest/scale-to-width-down/320?cb=20190710085240",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={},
    ),
    Item(
        name="IOTV Gen4 body armor (Full Protection Kit)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f5/IOTVFullImage.png/revision/latest/scale-to-width-down/320?cb=20190301090027",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="FORT Redut-T5 body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/FORT_Redut-T5_body_armor.png/revision/latest/scale-to-width-down/320?cb=20190410224442",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="5.11 Tactical Hexgrid plate carrier",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/11/HexPlateCarrier_View.png/revision/latest/scale-to-width-down/320?cb=20201230004256",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="LBT-6094A Slick Plate Carrier",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ee/SLICK-BIG-GIF.gif/revision/latest?cb=20220328142855",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="BNTI Zhuk-6a body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bc/Zhuk-6a_heavy_armor.PNG/revision/latest/scale-to-width-down/320?cb=20190301090039",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="NFM THOR Integrated Carrier body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/80/THOR_IC_View.PNG/revision/latest/scale-to-width-down/320?cb=20211206001354",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="6B43 6A Zabralo-Sh body armor",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/6B4.png/revision/latest/scale-to-width-down/320?cb=20190301090056",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
            MECHANIC: TraderInfo(level=3, quest_locked=False, barter=True),
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Kora-Kulon body armor",
        category=ARMOR_VEST,
        image_url="https://i.imgur.com/qzkgWxT.png",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="NPP KlASS Kora-Kulon body armor (Digital Flora)",
        category=ARMOR_VEST,
        image_url="https://i.imgur.com/txoBj01.png",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Interceptor OTV body armor (UCP)",
        category=ARMOR_VEST,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/OTV_PC_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064821",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
)

ALL_ARMORED_RIGS: tuple = (
    Item(
        name="WARTECH TV-115 plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/TV-115_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064819",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Eagle Allied Industries MBSS plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b4/MBSS_USECPLATE_Image.png/revision/latest/scale-to-width-down/320?cb=20230813072215",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Eagle Industries MMAC plate carrier (Ranger Green)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Mmac-view.png/revision/latest/scale-to-width-down/320?cb=20211229223039",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Shellback Tactical Banshee plate carrier (A-TACS AU)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/71/Shellback_Tactical_Banshee_plate_carrier.png/revision/latest/scale-to-width-down/320?cb=20221230035237",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Ars Arma A18 Skanda plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/78/A18_View.png/revision/latest/scale-to-width-down/320?cb=20191101010154",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="WARTECH TV-110 plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a9/Wartech_TV-110_plate_carrier.png/revision/latest/scale-to-width-down/320?cb=20190305205424",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="FirstSpear Strandhogg plate carrier (Ranger Green)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Strandhogg.png/revision/latest/scale-to-width-down/253?cb=20211229223415",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ECLiPSE RBAV-AF plate carrier (Ranger Green)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a0/RBAV-AF.png/revision/latest/scale-to-width-down/320?cb=20220705225122",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="CQC Osprey MK4A plate carrier (Assault, MTP)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b6/OspreyMk4_Assault_View.png/revision/latest/scale-to-width-down/320?cb=20211206002242",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B3TM-01M armored rig",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/12/6B3TM-01M.png/revision/latest/scale-to-width-down/320?cb=20191028200236",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B5-15 Zh-86 Uley armored rig",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/6B5-15.png/revision/latest/scale-to-width-down/320?cb=20181231121409",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical M2 plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2a/M2.png/revision/latest/scale-to-width-down/320?cb=20180520221351",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical M1 plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/66/ANA_Tactical_M1.png/revision/latest/scale-to-width-down/320?cb=20181227153645",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Crye Precision AVS plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/97/Crye_Precision_AVS_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20190517215229",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="5.11 Tactical TacTec plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/20/TactecImage.png/revision/latest/scale-to-width-down/320?cb=20180909205723",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Ars Arma CPC MOD.1 plate carrier",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/ArsArmaCPCMOD2.png/revision/latest?cb=20200502000042",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=True),
        }
    ),
    Item(
        name="Crye Precision CPC plate carrier (Goons Edition)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Crye_Precision_CPC_GE.png/revision/latest/scale-to-width-down/320?cb=20220705232026",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="S&S Precision PlateFrame plate carrier (Goons Edition)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b4/S%26S_Precision_PlateFrame_GE.png/revision/latest/scale-to-width-down/320?cb=20220705231743",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="CQC Osprey MK4A plate carrier (Protection, MTP)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/03/OspreyMk4_Protection_View.png/revision/latest/scale-to-width-down/320?cb=20211206002414",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="NPP KlASS Bagariy armored rig",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9a/NPP_Bagariy.png/revision/latest/scale-to-width-down/320?cb=20220705234540",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Tasmanian Tiger SK plate carrier (Multicam Black)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/eb/Tasmanian_Tiger_SK.png/revision/latest/scale-to-width-down/320?cb=20220705232948",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Crye Precision AVS plate carrier (Tagilla Edition)",
        category=ARMORED_RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/92/MBAV_View.png/revision/latest/scale-to-width-down/320?cb=20211205220746",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
)

ALL_ARMORS = ALL_ARMOR_VESTS + ALL_ARMORED_RIGS


ALL_RIGS: tuple = (
    Item(
        name=YOUR_CHOICE,
        category=RIG,
        image_url=YOU_CHOOSE_IMAGE,
        unlocked=True,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Scav Vest",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/ScavVest.png/revision/latest/scale-to-width-down/320?cb=20190517215830",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Security vest",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/Securityvest.png/revision/latest?cb=20201224194010",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Zulu Nylon Gear M4 Reduced Signature Chest Rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Zulu_M4_RSCR_Image.png/revision/latest?cb=20230813064822",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="DIY IDEA chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/63/DIY_IDEA_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20211206005252",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Spiritus Systems Bank Robber chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Bank_Robber_ins.png/revision/latest/scale-to-width-down/320?cb=20200315233111",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SOE Micro Rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/SOE.png/revision/latest/scale-to-width-down/320?cb=20191028034055",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Type 56 Chicom chest harness",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/Type_56_Chicom_Image.png/revision/latest?cb=20230813064823",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="WARTECH TV-109 + TV-106 chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/95/Wartech_gear_rig.png/revision/latest/scale-to-width-down/320?cb=20200624184927",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="CSA chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/CSAImage.png/revision/latest?cb=20210330190914",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="UMTBS 6sh112 Scout-Sniper",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/82/Scout_Sniper_rig.png/revision/latest/scale-to-width-down/301?cb=20171107182903",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Azimut SS \"Khamelion\" chest harness (Olive)",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/Azimut_SS_%22Khamelion%22_chest_harness_%28Olive%29_image.png/revision/latest/scale-to-width-down/320?cb=20221230000547",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Splav Tarzan M22 chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Tarzan.png/revision/latest?cb=20200314180047",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Haley Strategic D3CRX Chest Harness",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/D3CRX.PNG/revision/latest/scale-to-width-down/320?cb=20191030042338",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Dynaforce Triton M43-A chest harness",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/Triton_M43-A_Chest_Harness_ins.png/revision/latest/scale-to-width-down/320?cb=20190410162933",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BlackHawk! Commando chest harness",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3f/Blackhawk%21_commando.gif/revision/latest/scale-to-width-down/320?cb=20190615175249",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Direct Action Thunderbolt compact chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7c/Direct_Action_Thunderbolt_compact_chest_rig.png/revision/latest/scale-to-width-down/320?cb=20201020141605",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Gear Craft GC-BSS-MK1 chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/12/BSS_Mk1_View.png/revision/latest/scale-to-width-down/320?cb=20201226004117",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Umka M33-SET1 hunter vest",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b7/M33-SET1_vest.png/revision/latest/scale-to-width-down/320?cb=20210330132527",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            JAEGER: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-1961A Load Bearing Chest Rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/be/LBT_1961_View.png/revision/latest/scale-to-width-down/320?cb=20200528221933",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={}
    ),
    Item(
        name="LBT-1961A Load Bearing Chest Rig (Goons Edition)",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b5/LBT-1961A_GE.png/revision/latest/scale-to-width-down/320?cb=20220705233654",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Stich Profi Chest Rig MK2 (Recon, A-TACS FG)",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/StichMk2Recon_View.png/revision/latest/scale-to-width-down/320?cb=20211206001744",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Stich Profi Chest Rig MK2 (Assault, A-TACS FG)",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cb/StichMk2Assault_View_.png/revision/latest/scale-to-width-down/320?cb=20211206002034",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="BlackRock chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/79/BlackRock.png/revision/latest/scale-to-width-down/320?cb=20190517215730",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="WARTECH MK3 TV-104 chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Mk3inspect.PNG/revision/latest/scale-to-width-down/320?cb=20190305205103",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="ANA Tactical Alpha chest rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bb/Alpha_Rig.png/revision/latest/scale-to-width-down/320?cb=20190517215939",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Azimut SS \"Zhuk\" chest harness",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/Azimut_SS_Jhuk_Chest_Harness.gif/revision/latest/scale-to-width-down/320?cb=20210331130740",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Velocity Systems MPPV Multi-Purpose Patrol Vest",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/MPPV_view.png/revision/latest/scale-to-width-down/320?cb=20191230104438",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Belt-A + Belt-B gear rig",
        category=RIG,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f5/Belt-A_Belt-B_gear_rig.png/revision/latest/scale-to-width-down/320?cb=20181227112944",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
)

ALL_HELMETS: tuple = (
    Item(
        name=YOUR_CHOICE,
        category=HELMET,
        image_url=YOU_CHOOSE_IMAGE,
        unlocked=True,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Armasight NVG head strap",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/36/Armasight_NVG_Mask.png/revision/latest/scale-to-width-down/320?cb=20181231144238",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Wilcox Skull Lock head mount",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3a/Slockimage.png/revision/latest?cb=20180319194159",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
            MECHANIC: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Bomber beanie",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/Bomber_Beanie.png/revision/latest/scale-to-width-down/320?cb=20211205224712",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Tac-Kek FAST MT helmet (Replica)",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/32/TK_FAST_View.png/revision/latest/scale-to-width-down/320?cb=20200529000443",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="TSh-4M-L soft tank crew helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/65/TankHelm.png/revision/latest?cb=20191228042121",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Kolpak-1S riot helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Kolpak-1S.png/revision/latest/scale-to-width-down/320?cb=20180426010942",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="ShPM Firefighter helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/SHPM_Firefighter%27s_helmet.png/revision/latest/scale-to-width-down/320?cb=20181228185855",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="PSh-97 DJETA riot helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3d/PSH-97_-Jeta-_helmet_Image.png/revision/latest/scale-to-width-down/320?cb=20190102011443",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="LShZ light helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/57/LZSh_light_helmet.png/revision/latest/scale-to-width-down/320?cb=20180729193607",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SSh-68 steel helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/da/SSH-68Image.png/revision/latest/scale-to-width-down/320?cb=20181226233100",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Galvion Caiman Hybrid helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Caiman.png/revision/latest?cb=20201019155533",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
    Item(
        name="NFM HJELM helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/HJELM.png/revision/latest?cb=20211225183648",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="UNTAR helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/UNTAR_Helmet.png/revision/latest/scale-to-width-down/320?cb=20190112203853",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="6B47 Ratnik-BSh helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/6B47.gif/revision/latest/scale-to-width-down/320?cb=20180806190854",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="FORT Kiver-M bulletproof helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/89/Kiver-M_Helmet.png/revision/latest?cb=20191227210542",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SSSh-94 SFERA-S helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b5/SferaInspect.PNG/revision/latest/scale-to-width-down/320?cb=20190112203909",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="DevTac Ronin ballistic helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/11/DEVTAC_Ronin_ballistic_helmet_Image.png/revision/latest/scale-to-width-down/320?cb=20190614231623",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="MSA ACH TC-2001 MICH Series helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/74/Mich_View.PNG/revision/latest/scale-to-width-down/320?cb=20191101222044",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="MSA ACH TC-2002 MICH Series helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/MICH_2002_View.PNG/revision/latest/scale-to-width-down/320?cb=20191114020056",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="HighCom Striker ACHHC IIIA helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/ACHHC.gif/revision/latest/scale-to-width-down/320?cb=20180805175454",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="MSA Gallet TC 800 High Cut combat helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/78/MSA_TC_800.png/revision/latest/scale-to-width-down/320?cb=20200313215553",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Diamond Age Bastion helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/57/Bastion_View.png/revision/latest/scale-to-width-down/320?cb=20200529021033",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Ops-Core FAST MT Super High Cut helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/16/FASTMT.gif/revision/latest/scale-to-width-down/320?cb=20180805220153",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Crye Precision AirFrame helmet (Tan)",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Crye_Precision_Airframe_Tan_Image.png/revision/latest/scale-to-width-down/320?cb=20190102011851",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="Team Wendy EXFIL Ballistic Helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c8/Team_Wendy_EXFIL_Ballistic_Helmet.gif/revision/latest/scale-to-width-down/320?cb=20191229154600",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="ZSh-1-2M helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/dc/ZSH-1-2M.gif/revision/latest/scale-to-width-down/320?cb=20180809202110",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="HighCom Striker ULACH IIIA helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/34/ULACH.gif/revision/latest/scale-to-width-down/320?cb=20180806205056",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="BNTI LShZ-2DTM helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/73/LSHZ-2DTM3D.png/revision/latest/scale-to-width-down/320?cb=20191030044246",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Maska-1SCh bulletproof helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/Maska_1Sch_helmet.gif/revision/latest/scale-to-width-down/320?cb=20190101152329",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Altyn bulletproof helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f3/Altynimage.png/revision/latest/scale-to-width-down/320?cb=20180517203723",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Rys-T bulletproof helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/77/RysTHelmet.png/revision/latest/scale-to-width-down/320?cb=20201019160756",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="Vulkan-5 (LShZ-5) bulletproof helmet",
        category=HELMET,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/94/Vulkan-5_%28LShZ-5%29_heavy_helmet.png/revision/latest/scale-to-width-down/320?cb=20190411084258",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
)

ALL_BACKPACKS: tuple = (
    Item(
        name=YOUR_CHOICE,
        category=BACKPACK,
        image_url=YOU_CHOOSE_IMAGE,
        unlocked=True,
        meta=True,
        flea=False,
        trader_info={}
    ),
    Item(
        name="6Sh118 raid backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/14/6SH118_View.png/revision/latest?cb=20230324190053",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            PRAPOR: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="LBT-2670 Slim Field Med Pack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0a/LBT-2670_View.png/revision/latest?cb=20200314005924",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            THERAPIST: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Mystery Ranch Blackjack 50 backpack (Multicam)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/Mystery_Ranch_Blackjack_50_backpack.png/revision/latest/scale-to-width-down/320?cb=20200714203420",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Eberlestock F4 Terminator load bearing backpack (Tiger Stripe)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5e/F4_terminator_view.png/revision/latest/scale-to-width-down/315?cb=20201020145959",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="SSO Attack 2 raid backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/07/Attack.PNG/revision/latest/scale-to-width-down/320?cb=20180517203915",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Tasmanian Tiger Trooper 35 backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/25/Tasmanian_trooper_35.png/revision/latest?cb=20230107201140",
        unlocked=False,
        meta=True,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Pilgrim tourist backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/Pilgrim_Backpack.png/revision/latest/scale-to-width-down/312?cb=20190301071419",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={}
    ),
    Item(
        name="3V Gear Paratus 3-Day Operator's Tactical backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/3V_G_Paratus.png/revision/latest/scale-to-width-down/320?cb=20190301072645",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            PEACEKEEPER: TraderInfo(level=4, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Eberlestock G2 Gunslinger II backpack (Dry Earth)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/Gunslinger_II_backpack_image.png/revision/latest/scale-to-width-down/290?cb=20210330172156",
        unlocked=False,
        meta=False,
        flea=False,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=True, barter=False),
        }
    ),
    Item(
        name="Oakley Mechanism heavy duty backpack (Black)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/Oakley_Mechanism_.png/revision/latest/scale-to-width-down/320?cb=20191108103108",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="ANA Tactical Beta 2 Battle backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ef/Beta2BP.png/revision/latest/scale-to-width-down/320?cb=20180802222134",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=4, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Gruppa 99 T30 backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/Gruppa_99_T30_BM.gif/revision/latest/scale-to-width-down/320?cb=20220705202041",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Eberlestock F5 Switchblade backpack (Dry Earth)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/Eberlestock_F5_backpack_view.png/revision/latest/scale-to-width-down/315?cb=20201020150753",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Camelbak Tri-Zip assault backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/df/CamelbackThreezeep.png/revision/latest/scale-to-width-down/320?cb=20190517215207",
        unlocked=False,
        meta=True,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-1476A 3Day Pack (Woodland)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/LBT-1476A_VIEW.png/revision/latest/scale-to-width-down/320?cb=20211213223219",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=3, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Gruppa 99 T20 backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/be/Gruppa_99_T20_Image.gif/revision/latest/scale-to-width-down/320?cb=20220220203102",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Drawbridge backpack (Coyote Tan)",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/HazardDrawbridge_View.png/revision/latest/scale-to-width-down/320?cb=20211206001203",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Takedown sling backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/Hazard4_Takedown.gif/revision/latest/scale-to-width-down/320?cb=20210331130153",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=2, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Hazard 4 Pillbox backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/17/HazardPillboxView.png/revision/latest/scale-to-width-down/320?cb=20211206001554",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Scav backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/96/Scav_Backpack_Inspect.png/revision/latest/scale-to-width-down/320?cb=20190517215051",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="WARTECH Berkut BB-102 backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/03/Wartech_Berkut_VV-102_backpack_ins.png/revision/latest?cb=20201031071733",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="LBT-8005A Day Pack backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8c/Day_pack2.PNG/revision/latest/scale-to-width-down/320?cb=20211206005550",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Sanitar's bag",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/75/Sanitar_Bag_View.png/revision/latest/scale-to-width-down/320?cb=20200727184258",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Flyye MBSS backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c0/Flyye_MBSS_Backpack2.png/revision/latest/scale-to-width-down/303?cb=20221117115315",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
            PEACEKEEPER: TraderInfo(level=1, quest_locked=False, barter=True),
        }
    ),
    Item(
        name="Mystery Ranch NICE COMM 3 BVS frame system",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/94/COMM_3_BVS.png/revision/latest/scale-to-width-down/320?cb=20220705200139",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Duffle bag",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/EfT_Item_Icon_116.png/revision/latest/scale-to-width-down/320?cb=20180707232346",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="LolKek 3F Transfer tourist backpack",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/LK_3F_backpack_view.png/revision/latest/scale-to-width-down/315?cb=20201020151157",
        unlocked=False,
        meta=False,
        flea=True,
        trader_info={}
    ),
    Item(
        name="Transformer Bag",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/EfT_Item_Icon_316.png/revision/latest/scale-to-width-down/320?cb=20180707232426",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="VKBO army bag",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a6/Armybagimage.png/revision/latest/scale-to-width-down/320?cb=20230324190046",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            PRAPOR: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
    Item(
        name="Tactical sling bag",
        category=BACKPACK,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Tactical_Sling_bag.png/revision/latest/scale-to-width-down/320?cb=20180707232914",
        unlocked=True,
        meta=False,
        flea=True,
        trader_info={
            RAGMAN: TraderInfo(level=1, quest_locked=False, barter=False),
        }
    ),
)


@dataclass(slots=True, frozen=True)
class GameRule:
    name: str
    category: str
    image_url: str
    meta: bool


ALL_GUN_MODS: tuple = (
    GameRule(
        name=LL1_TRADERS,
        category=GUN_MOD,
        image_url=LL1_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL2_TRADERS,
        category=GUN_MOD,
        image_url=LL2_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL3_TRADERS,
        category=GUN_MOD,
        image_url=LL3_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL4_TRADERS,
        category=GUN_MOD,
        image_url=LL4_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=NO_RESTRICTIONS,
        category=GUN_MOD,
        image_url=NO_RESTRICTIONS_IMAGE,
        meta=True,
    )
)

ALL_AMMO: tuple = (
    GameRule(
        name=LL1_TRADERS,
        category=AMMO,
        image_url=LL1_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL2_TRADERS,
        category=AMMO,
        image_url=LL2_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL3_TRADERS,
        category=AMMO,
        image_url=LL3_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=LL4_TRADERS,
        category=AMMO,
        image_url=LL4_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name=NO_RESTRICTIONS,
        category=AMMO,
        image_url=NO_RESTRICTIONS_IMAGE,
        meta=True,
    )
)

ALL_MAPS: tuple = (
    GameRule(
        name=YOUR_CHOICE,
        category=MAP,
        image_url=YOU_CHOOSE_IMAGE,
        meta=True,
    ),
    GameRule(
        name="Factory",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1a/Factory-Day_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811153020",
        meta=True,
    ),
    GameRule(
        name="Woods",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_woods.png/revision/latest/scale-to-width-down/382?cb=20171101223132",
        meta=True,
    ),
    GameRule(
        name="Customs",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9f/Customs_Banner.png/revision/latest/scale-to-width-down/382?cb=20200811151055",
        meta=True,
    ),
    GameRule(
        name="Interchange",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3e/Banner_interchange.png/revision/latest/scale-to-width-down/382?cb=20200811153253",
        meta=True,
    ),
    GameRule(
        name="Shoreline",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d5/Banner_shoreline.png/revision/latest/scale-to-width-down/382?cb=20171101223501",
        meta=True,
    ),
    GameRule(
        name="Reserve",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f4/Reserve.png/revision/latest/scale-to-width-down/382?cb=20191101214624",
        meta=True,
    ),
    GameRule(
        name="The Lab",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d7/TheLabBanner.png/revision/latest/scale-to-width-down/382?cb=20181225171705",
        meta=True,
    ),
    GameRule(
        name="Lighthouse",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/dc/Banner_lighthouse.png/revision/latest/scale-to-width-down/382?cb=20211213001748",
        meta=True,
    ),
    GameRule(
        name="Streets of Tarkov",
        category=MAP,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/41/Banner_streets.png/revision/latest/scale-to-width-down/382?cb=20230131205551",
        meta=True,
    ),
)

GOOD_MODIFIERS: tuple = (
    GameRule(
        name="Ask your scav for some loot",
        category=RANDOM_MODIFIER,
        image_url="https://pbs.twimg.com/media/DlXnlRvXoAAhOv2.jpg",
        meta=True,
    ),
    GameRule(
        name="Pop any 3 stimulants at start of raid",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/lYmpWWL.png",
        meta=True,
    ),
    GameRule(
        name="Weapon.PISTOL secondary",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/pIIl7j1.png",
        meta=True,
    ),
    GameRule(
        name="Impact grenades only",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ac/RGN_View.png/revision/latest?cb=20211212210251",
        meta=True,
    ),
    GameRule(
        name="Re-roll 1 slot",
        category=RANDOM_MODIFIER,
        image_url=DICE_IMAGE,
        meta=True,
    ),
    GameRule(
        name="Re-roll 2 slots",
        category=RANDOM_MODIFIER,
        image_url=DICE_IMAGE,
        meta=True,
    ),
    GameRule(
        name="Carry at least 4 grenades, and use them liberally during the raid",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Vog25.png/revision/latest?cb=20200316073837",
        meta=True,
    ),
)

OK_MODIFIERS: tuple = (
    GameRule(
        name="Use highest capacity magazine",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/90/MAG5-100.png/revision/latest/scale-to-width-down/1200?cb=20190414152250",
        meta=True,
    ),
    GameRule(
        name="Attempt to befriend one random player",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/i3KRTCc.png",
        meta=True,
    ),
    GameRule(
        name="Night raid (NVG if applicable)",
        category=RANDOM_MODIFIER,
        image_url="https://i.redd.it/juv50kmkgm941.png",
        meta=True,
    ),
    GameRule(
        name="Flash grenades only",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fc/Model_7290_Flash_Bang.png/revision/latest?cb=20211212182627",
        meta=True,
    ),
    GameRule(
        name="M67 Hand grenades only",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e2/M67.png/revision/latest/scale-to-width-down/320?cb=20200216033043",
        meta=True,
    ),
    GameRule(
        name="Use highest flesh damage round available",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/.45_RIP_View.png/revision/latest?cb=20200508230152",
        meta=True,
    ),
    GameRule(
        name="Use highest penetration round available",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/338ap.png/revision/latest/scale-to-width-down/320?cb=20210102070935",
        meta=True,
    ),
    GameRule(
        name="Use thermal scope",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/Sig_ECHO1_Image.png/revision/latest/scale-to-width-down/320?cb=20230813064714",
        meta=True,
    ),
    GameRule(
        name="Swap weapons with a teammate at the start of the raid",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/scq6eWt.png",
        meta=False,
    ),
    GameRule(
        name="Attempt to dress up as a scav",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/yJcVKMJ.png",
        meta=False,
    ),
)

BAD_MODIFIERS: tuple = (
    GameRule(
        name="Only smoke grenades",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/M18_Green_View.png/revision/latest?cb=20211212211007",
        meta=False,
    ),
    GameRule(
        name="No suppressors",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/Otrn9Xc.png",
        meta=False,
    ),
    GameRule(
        name="No insurance",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/E5xueS0.png",
        meta=False,
    ),
    GameRule(
        name="Iron sights only",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/Kriss_FlipupRear_View.png/revision/latest/scale-to-width-down/320?cb=20201224175245",
        meta=False,
    ),
    GameRule(
        name="Hip fire only (unbind aim)",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/xh2Z6eT.jpg",
        meta=False,
    ),
    GameRule(
        name="No surgery kits",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/ZLf9udj.png",
        meta=False,
    ),
    GameRule(
        name="No docs/sicc/keytool/keycard holder",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/5Rusxe3.png",
        meta=False,
    ),
    GameRule(
        name="Weapon must be stock",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/j3RShdo.png",
        meta=False,
    ),
    GameRule(
        name="Single-fire only",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/yhRZB5H.png",
        meta=False,
    ),
    GameRule(
        name="Hatchlings must be fought with a melee",
        category=RANDOM_MODIFIER,
        image_url="https://academyoffencingmasters.com/blog/wp-content/uploads/2017/02/Valentine%E2%80%99s-Day-Love-and-Swordfighting-Duels.jpg",
        meta=True,
    ),
    GameRule(
        name="No headphones",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/FOrgqJm.png",
        meta=False,
    ),
    GameRule(
        name="Level 1 Meds",
        category=RANDOM_MODIFIER,
        image_url=LL1_TRADERS_IMAGE,
        meta=False,
    ),
    GameRule(
        name="No grenades",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/8d22sUW.png",
        meta=False,
    ),
    GameRule(
        name="Flashlight always on",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6a/X400image.png/revision/latest/scale-to-width-down/320?cb=20190628034042",
        meta=False,
    ),
    GameRule(
        name="Use helmet flashlight and keep it always turned on",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/tbmab5X.png",
        meta=False,
    ),
    GameRule(
        name="Only use stimulants for healing",
        category=RANDOM_MODIFIER,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/ETG_change.png/revision/latest?cb=20181228104842",
        meta=False,
    ),
    GameRule(
        name="Must attempt to extract camp one player",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/uMBkzX3.png",
        meta=False,
    ),
    GameRule(
        name="Scavs must be killed with a sawed-off double barrel as secondary",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/uMBkzX3.png",
        meta=False,
    ),
    GameRule(
        name="Must use \"Scav Down\" voice line every time you kill a scav",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/IrlJOQL.png",
        meta=False,
    ),
    GameRule(
        name="Must swap backpacks with teammate at the end of the raid (including the loot inside)",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/PB7E1Gf.jpeg",
        meta=False,
    ),
    GameRule(
        name="Fire your weapon into the air to signal your presence at the beginning of the raids",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/GcpDk0I.png",
        meta=False,
    ),
    GameRule(
        name="Change your interface language to Русский for the true Tarkovian experience",
        category=RANDOM_MODIFIER,
        image_url="https://i.imgur.com/xjUtGIM.png",
        meta=False,
    ),
)

ALL_MODIFIERS: tuple = (GOOD_MODIFIERS, OK_MODIFIERS, BAD_MODIFIERS)
