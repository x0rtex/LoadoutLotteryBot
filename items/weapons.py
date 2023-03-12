from typing import Literal

assault_carbine = "Assault Carbine"
assault_rifle = "Assault Rifle"
bolt_action_rifle = "Bolt-Action Rifle"
machine_gun = "Machine Gun"
marksman_rifle = "Marksman Rifle"
pistol = "Pistol"
smg = "SMG"
shotgun = "Shotgun"
grenade_launcher = "Grenade Launcher"
melee = "Melee"


class Weapons:
    def __init__(
            self,
            name: str,
            image_url: str,
            category: [assault_carbine, assault_rifle, bolt_action_rifle, machine_gun, marksman_rifle, pistol, smg, shotgun, grenade_launcher, melee],
            trader: Literal["Flea", "Prapor", "Therapist", "Fence", "Skier", "Peacekeeper", "Mechanic", "Ragman", "Jaeger", None],
            trader_level: Literal[0, 1, 2, 3, 4],
            fir_only: bool,
            quest_locked: bool,
            meta: bool,
    ):
        self.name = name
        self.image_url = image_url
        self.category = category
        self.trader = trader
        self.trader_level = trader_level
        self.fir_only = fir_only
        self.quest_locked = quest_locked
        self.meta = meta


weapon_list = [

    Melee := Weapons(
        name=melee,
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8a/Antique_Axe.png/revision/latest/scale-to-width-down/200?cb=20181110013042",
        category=melee,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    ADAR := Weapons(
        name="ADAR 2-15",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3c/ADAR2-15Image.png/revision/latest/scale-to-width-down/180?cb=20190226190907",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AK_101 := Weapons(
        name="Kalashnikov AK-101",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/31/AK101_Image.png/revision/latest/scale-to-width-down/180?cb=20180502204454",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),

    AK_102 := Weapons(
        name="Kalashnikov AK-102",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ca/Ak102image.png/revision/latest/scale-to-width-down/180?cb=20180506001257",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AK_103 := Weapons(
        name="Kalashnikov AK-103",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e1/AK-103_7.62x39.png/revision/latest/scale-to-width-down/180?cb=20180429234506",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AK_104 := Weapons(
        name="Kalashnikov AK-104",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b2/AK-104Image.png/revision/latest/scale-to-width-down/180?cb=20180503235112",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AK_105 := Weapons(
        name="Kalashnikov AK-105",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8b/AK-105_5.45x39.png/revision/latest/scale-to-width-down/180?cb=20180429234412",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AK_74 := Weapons(
        name="Kalashnikov AK-74",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/AK-74Image.png/revision/latest/scale-to-width-down/180?cb=20181226154054",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AK_74M := Weapons(
        name="Kalashnikov AK-74M",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/AK-74M.png/revision/latest/scale-to-width-down/180?cb=20180513014125",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AK_74N := Weapons(
        name="Kalashnikov AK-74N",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Akn.png/revision/latest/scale-to-width-down/180?cb=20181028171233",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    AKM := Weapons(
        name="Kalashnikov AKM",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0f/Akm.png/revision/latest/scale-to-width-down/180?cb=20180206133400",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKMN := Weapons(
        name="Kalashnikov AKMN",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Akmn.png/revision/latest/scale-to-width-down/180?cb=20180206133117",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    AKMS := Weapons(
        name="Kalashnikov AKMS",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/Akms.png/revision/latest/scale-to-width-down/180?cb=20180427005729",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKMSN := Weapons(
        name="Kalashnikov AKMSN",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e6/Akmsn.png/revision/latest/scale-to-width-down/180?cb=20180503233021",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKS_74 := Weapons(
        name="Kalashnikov AKS-74",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/AKS-74.png/revision/latest/scale-to-width-down/180?cb=20181230153732",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKS_74N := Weapons(
        name="Kalashnikov AKS-74N",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4f/AKS-74N.png/revision/latest/scale-to-width-down/180?cb=20180426173339",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKS_74U := Weapons(
        name="Kalashnikov AKS-74U",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/84/Aks74u.png/revision/latest/scale-to-width-down/180?cb=20181028171406",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKS_74UB := Weapons(
        name="Kalashnikov AKS-74UB",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/Aks74ub.png/revision/latest/scale-to-width-down/180?cb=20181028171415",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AKS_74UN := Weapons(
        name="Kalashnikov AKS-74UN",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b3/Aks74un.png/revision/latest/scale-to-width-down/180?cb=20181028171353",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    ASh_12 := Weapons(
        name="ASh-12",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f1/ASh_12.png/revision/latest/scale-to-width-down/180?cb=20211206013813",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AS_VAL := Weapons(
        name="AS VAL",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1c/Asval.png/revision/latest/scale-to-width-down/180?cb=20190305220933",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Mk47 := Weapons(
        name="CMMG Mk47 Mutant",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/Mk47_Mutant_View.png/revision/latest/scale-to-width-down/180?cb=20211203223357",
        category=assault_rifle,
        trader="Skier",
        trader_level=4,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    MDR_556 := Weapons(
        name="DT MDR 5.56x45",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/13/DT_MDR_5.56x45_Assault_Rifle.png/revision/latest/scale-to-width-down/180?cb=20190411211744",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MDR_762 := Weapons(
        name="DT MDR 7.62x51",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/33/DT_MDR_308.png/revision/latest/scale-to-width-down/180?cb=20191228210602",
        category=assault_rifle,
        trader="Peacekeeper",
        trader_level=4,
        fir_only=False,
        quest_locked=True,
        meta=True,
    ),
    
    HK_416 := Weapons(
        name="HK 416A5",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/HK416Image.png/revision/latest/scale-to-width-down/180?cb=20181226145352",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    M4A1 := Weapons(
        name="Colt M4A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/29/M4a1.png/revision/latest/scale-to-width-down/180?cb=20181028172147",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    SCAR_L := Weapons(
        name="FN SCAR-L (Mk 16)",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/00/SCAR-L_Insp.gif/revision/latest/scale-to-width-down/180?cb=20220101204420",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    SCAR_H := Weapons(
        name="FN SCAR-H (Mk 17)",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a8/ScarH_Image.gif/revision/latest/scale-to-width-down/180?cb=20220220215829",
        category=assault_rifle,
        trader="Peacekeeper",
        trader_level=4,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MCX := Weapons(
        name="SIG MCX",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/-92ucz5kq_Y.jpg/revision/latest/scale-to-width-down/180?cb=20201226014736",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    SA_58 := Weapons(
        name="DS Arms SA-58",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ae/DS_Arms_SA-58_OSW_Para_7.62x51.png/revision/latest/scale-to-width-down/180?cb=20181028172156",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    TX_15 := Weapons(
        name="Lone Star TX-15 DML",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/TX-15_View.PNG/revision/latest/scale-to-width-down/180?cb=20191103030150",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    VPO_209 := Weapons(
        name="Vepr AKM / VPO-209 (.366)",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b0/Vpo209.png/revision/latest/scale-to-width-down/180?cb=20181028171328",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    VPO_136 := Weapons(
        name="VPO-136 \"Vepr KM\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/e9/Vpo136.png/revision/latest/scale-to-width-down/180?cb=20181028171300",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    OP_SKS := Weapons(
        name="Simonov OP-SKS",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/08/Opsks.png/revision/latest/scale-to-width-down/180?cb=20190414112410",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    SKS := Weapons(
        name="Simonov SKS (No Dovetail)",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/72/Sks.png/revision/latest/scale-to-width-down/180?cb=20190414112401",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    VPO_101 := Weapons(
        name="VPO-101 \"Vepr-Hunter\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f0/VeprHunterImage.png/revision/latest/scale-to-width-down/180?cb=20190410211507",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    RPK_16 := Weapons(
        name="RPK-16",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/RPK-16.png/revision/latest/scale-to-width-down/180?cb=20181226153306",
        category=machine_gun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MP5 := Weapons(
        name="HK MP5",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Mp5.png/revision/latest/scale-to-width-down/180?cb=20180507221414",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MP5K := Weapons(
        name="HK MP5K-N",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/45/HK_MP5K-N.png/revision/latest/scale-to-width-down/180?cb=20211206013958",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MP7A1 := Weapons(
        name="HK MP7A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/HKMP7A1Image.png/revision/latest/scale-to-width-down/180?cb=20181111215340",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MP7A2 := Weapons(
        name="HK MP7A2",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/52/HKMP7A2Image.png/revision/latest/scale-to-width-down/180?cb=20181111214757",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    MP9 := Weapons(
        name="B&T MP9",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0e/MP9_View.png/revision/latest/scale-to-width-down/180?cb=20211206014311",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MP9_N := Weapons(
        name="B&T MP9-N",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fd/B%26T_MP9-N_9x19_Submachinegun.png/revision/latest/scale-to-width-down/180?cb=20211206014309",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    MPX := Weapons(
        name="SIG MPX",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f7/Mpx.png/revision/latest/scale-to-width-down/180?cb=20180219121907",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    P90 := Weapons(
        name="FN P90",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/P90Image.png/revision/latest/scale-to-width-down/180?cb=20191109011038",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    PP_19 := Weapons(
        name="PP-19-01 Vityaz-SN",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fb/Pp19.png/revision/latest/scale-to-width-down/180?cb=20180219121911",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Klin := Weapons(
        name="PP-9 \"Klin\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/48/Klin.png/revision/latest/scale-to-width-down/180?cb=20180219121903",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Kedr := Weapons(
        name="PP-91 \"Kedr\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/Kedr.png/revision/latest/scale-to-width-down/180?cb=20180219121901",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Kedr_B := Weapons(
        name="PP-91-01 \"Kedr-B\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a4/Kedrb.png/revision/latest/scale-to-width-down/180?cb=20180219121902",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    PPSH := Weapons(
        name="PPSH-41",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d0/PPSH-41_View.png/revision/latest/scale-to-width-down/180?cb=20211206010213",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Saiga_9 := Weapons(
        name="Saiga-9",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/Saiga9.png/revision/latest/scale-to-width-down/180?cb=20180219121912",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    STM_9 := Weapons(
        name="Soyuz-TM STM-9",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/STM-9_Base_View.png/revision/latest/scale-to-width-down/180?cb=20211206010453",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    UMP_45 := Weapons(
        name="HK UMP 45",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/UMP45_View.png/revision/latest/scale-to-width-down/180?cb=20211206010703",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Vector_45 := Weapons(
        name="KRISS Vector .45",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bf/Vector45_fir_unloaded_view.png/revision/latest/scale-to-width-down/180?cb=20211206011407",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Vector_9x19 := Weapons(
        name="KRISS Vector 9x19",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9e/Vector_9x19_View.png/revision/latest/scale-to-width-down/180?cb=20211206011601",
        category=smg,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Mossberg_590A1 := Weapons(
        name="Mossberg 590A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/56/M590A1_View.png/revision/latest/scale-to-width-down/180?cb=20211206014100",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    M870 := Weapons(
        name="Remington M870",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/91/M870.png/revision/latest/scale-to-width-down/180?cb=20180426140946",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    MP_133 := Weapons(
        name="MP-133",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/fe/Mr133.png/revision/latest/scale-to-width-down/180?cb=20180219121908",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    MP_153 := Weapons(
        name="MP-153",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/3b/Mp153.png/revision/latest/scale-to-width-down/180?cb=20180219121906",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    MP_155 := Weapons(
        name="MP-155",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4d/MP-155.png/revision/latest/scale-to-width-down/180?cb=20211205210153",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    MP_43 := Weapons(
        name="Baikal MP-43-1C",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2b/MP-43-1C_12ga_double-barrel_shotgun.jpg/revision/latest/scale-to-width-down/180?cb=20211213051714",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    MTs_255 := Weapons(
        name="MTs-255-12",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/2d/EFT_UpcomingMTs255.png/revision/latest/scale-to-width-down/180?cb=20190515021208",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Saiga_12 := Weapons(
        name="Saiga-12",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cd/Saiga12.png/revision/latest/scale-to-width-down/180?cb=20180219121914",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    TOZ_106 := Weapons(
        name="TOZ-106",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/Toz.png/revision/latest/scale-to-width-down/180?cb=20180219121918",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    KS_23M := Weapons(
        name="TOZ KS-23M",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/85/KS-23M.png/revision/latest/scale-to-width-down/180?cb=20201019145716",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    G28 := Weapons(
        name="HK G28",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/18/G28_Full.png/revision/latest/scale-to-width-down/180?cb=20211214013521",
        category=marksman_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),

    M1A := Weapons(
        name="Springfield Armory M1A",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5f/M1A_Icon.png/revision/latest/scale-to-width-down/180?cb=20180503234958",
        category=marksman_rifle,
        trader="Peacekeeper",
        trader_level=3,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),

    MK_18 := Weapons(
        name="SWORD International Mk-18",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/a2/Mk18.png/revision/latest/scale-to-width-down/180?cb=20210102132503",
        category=marksman_rifle,
        trader="Jaeger",
        trader_level=4,
        fir_only=True,
        quest_locked=True,
        meta=True,
    ),

    RFB := Weapons(
        name="Kel-Tec RFB",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/68/KT_RFB.png/revision/latest/scale-to-width-down/180?cb=20201019134602",
        category=marksman_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    RSASS := Weapons(
        name="Remington R11 RSASS",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9b/Rsass.png/revision/latest/scale-to-width-down/180?cb=20181122021513",
        category=marksman_rifle,
        trader="Peacekeeper",
        trader_level=4,
        fir_only=False,
        quest_locked=True,
        meta=True,
    ),

    SR_25 := Weapons(
        name="Knight's Armament Company SR-25",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/69/SR-25_View.png/revision/latest/scale-to-width-down/180?cb=20191227220256",
        category=marksman_rifle,
        trader="Peacekeeper",
        trader_level=3,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),

    SVDS := Weapons(
        name="SVDS",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/8f/SVD-S.png/revision/latest/scale-to-width-down/180?cb=20190411211731",
        category=marksman_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    VSS := Weapons(
        name="VSS Vintorez",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/Vss.png/revision/latest/scale-to-width-down/180?cb=20210114170659",
        category=marksman_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),

    DVL_10 := Weapons(
        name="LOBAEV Arms DVL-10 Saboteur",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6c/Dvl10.png/revision/latest/scale-to-width-down/180?cb=20180219121859",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    M700 := Weapons(
        name="Remington M700",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/2/26/M700Image.png/revision/latest/scale-to-width-down/180?cb=20181226171021",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Mosin_Sniper := Weapons(
        name="Mosin Sniper Rifle",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/02/MosinInspect.png/revision/latest/scale-to-width-down/180?cb=20180918200314",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Mosin_Infantry := Weapons(
        name="Mosin Infantry Rifle",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/d4/MosinInfantryImage.png/revision/latest/scale-to-width-down/180?cb=20181226165344",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    SV_98 := Weapons(
        name="SV-98",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7d/Sv98.png/revision/latest/scale-to-width-down/180?cb=20180427101420",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    T_5000M := Weapons(
        name="Orsis T-5000M",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/e/ea/T-5000_View.png/revision/latest/scale-to-width-down/180?cb=20200216013517",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    VPO_215 := Weapons(
        name="Molot VPO-215 \"Gornostay\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4e/VPO-215_View.png/revision/latest/scale-to-width-down/180?cb=20200216013459",
        category=bolt_action_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    USP := Weapons(
        name="HK USP",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/a/ad/Usp1.png/revision/latest/scale-to-width-down/180?cb=20220118221605",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    APB := Weapons(
        name="APB",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/ba/APBImage.png/revision/latest/scale-to-width-down/400?cb=20200216023044",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    APS := Weapons(
        name="Stechkin APS",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Stechkin_Automatic_Pistol_9x18PM.png/revision/latest/scale-to-width-down/200?cb=20200216021943",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    FN_5_7 := Weapons(
        name="FN 5-7",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/d/de/Five-seveN.gif/revision/latest/scale-to-width-down/200?cb=20191109004734",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Glock_17 := Weapons(
        name="Glock 17",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/54/Glock17.png/revision/latest/scale-to-width-down/200?cb=20200216022006",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Glock_18C := Weapons(
        name="Glock 18C",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/81/Glock18CImage.png/revision/latest/scale-to-width-down/200?cb=20200216022017",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Glock_19X := Weapons(
        name="Glock 19X",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/6/6b/G19X_View.png/revision/latest?cb=20221231013454",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    M1911A1 := Weapons(
        name="Colt M1911A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/bd/M1911A1_View.png/revision/latest/scale-to-width-down/200?cb=20200508214809",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    M45A1 := Weapons(
        name="Colt M45A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c3/M45A1.png/revision/latest/scale-to-width-down/200?cb=20201019153037",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    M9A3 := Weapons(
        name="Beretta M9A3",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/8/86/EFT_UpcomingM9A3.png/revision/latest/scale-to-width-down/200?cb=20200216022039",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Grach := Weapons(
        name="Yarygin MP-443 Grach",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/0/0b/Grach.png/revision/latest/scale-to-width-down/200?cb=20200216022052",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    P226R := Weapons(
        name="SIG P226R",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c6/P226.png/revision/latest/scale-to-width-down/200?cb=20200216022104",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    PB := Weapons(
        name="PB",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c4/Pb.png/revision/latest/scale-to-width-down/200?cb=20200216023013",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    PL15 := Weapons(
        name="PL15",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/3/38/PL-15image.png/revision/latest/scale-to-width-down/200?cb=20211206010342",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Makarov_T := Weapons(
        name="PM (t) \"Makarov\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c7/Makarovt.png/revision/latest/scale-to-width-down/200?cb=20200216022116",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Makarov := Weapons(
        name="PM \"Makarov\"",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/4c/Makarov.png/revision/latest/scale-to-width-down/200?cb=20200216022127",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    SR_1MP := Weapons(
        name="Serdyukov SR-1MP Gyurza",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/cc/Sr1mp.png/revision/latest/scale-to-width-down/200?cb=20200216022136",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    TT := Weapons(
        name="TT",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/1b/Tt.png/revision/latest/scale-to-width-down/200?cb=20200216022150",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    TT_Gold := Weapons(
        name="TT (Golden)",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/46/TT_Pistol_7.62x25_TT_gold_2.png/revision/latest/scale-to-width-down/200?cb=20200216022203",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    CR_200DS := Weapons(
        name="CR 200DS 9x19mm",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/CR_200DS_1.png/revision/latest/scale-to-width-down/180?cb=20220416231853",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    CR_50DS := Weapons(
        name="CR 50DS .357 Magnum",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9c/CR_50DS_.357_1.png/revision/latest/scale-to-width-down/180?cb=20220417132057",
        category=pistol,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    G36 := Weapons(
        name="HK G36",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/5b/G36_View.png/revision/latest/scale-to-width-down/180?cb=20220705223014",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    Super_90 := Weapons(
        name="Benelli M3 Super 90",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/5/55/Benelli_M3_Super_90.png/revision/latest/scale-to-width-down/180?cb=20220703180524",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AXMC := Weapons(
        name="Accuracy International AXMC",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/c5/AXMC_.338_LM.png/revision/latest/scale-to-width-down/180?cb=20220705212920",
        category=bolt_action_rifle,
        trader="Jaeger",
        trader_level=4,
        fir_only=False,
        quest_locked=True,
        meta=False,
    ),
    
    MP_18 := Weapons(
        name="MP-18 single-shot rifle",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/9/9d/MP18_VIew.png/revision/latest/scale-to-width-down/180?cb=20220629224646",
        category=shotgun,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    RD_704 := Weapons(
        name="Rifle Dynamics RD-704",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/c/ce/RD-704.jpg/revision/latest/scale-to-width-down/180?cb=20220702095109",
        category=assault_rifle,
        trader="Mechanic",
        trader_level=4,
        fir_only=False,
        quest_locked=False,
        meta=True,
    ),
    
    SAG := Weapons(
        name="SAG AK",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/1/19/SAG.545.png/revision/latest/scale-to-width-down/180?cb=20220701160057",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    SAG_Short := Weapons(
        name="SAK AK Short",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/70/AK-545Short_View.png/revision/latest/scale-to-width-down/180?cb=202206292156099",
        category=assault_carbine,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),
    
    AUG_A1 := Weapons(
        name="AUG A1",
        image_url="",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    AUG_A3 := Weapons(
        name="AUG A3",
        image_url="",
        category=assault_rifle,
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    FN40GL := Weapons(
        name="FN40GL",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/b/b8/FNGL40inspect.png/revision/latest/scale-to-width-down/180?cb=20211206014144",
        category=grenade_launcher,
        trader="Peacekeeper",
        trader_level=4,
        fir_only=True,
        quest_locked=True,
        meta=False,
    ),

    M32A1 := Weapons(
        name="M32A1",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/7/7a/M32A1inspect.png/revision/latest/scale-to-width-down/180?cb=20220704113236",
        category=grenade_launcher,
        trader=None,
        trader_level=0,
        fir_only=True,
        quest_locked=False,
        meta=True,
    ),

]
