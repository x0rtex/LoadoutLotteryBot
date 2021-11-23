import time
import random

weaponList = [
    "ADAR 2-15",
    "AK-101",
    "AK-102",
    "AK-103",
    "AK-104",
    "AK-105",
    "AK-74",
    "AK-74M",
    "AK-74N",
    "AKM",
    "AKMN",
    "AKMS",
    "AKMSN",
    "AKS-74",
    "AKS-74N",
    "AKS-74U",
    "AKS-74UB",
    "AKS-74UN",
    "ASh-12",
    "AS VAL",
    "CMMG Mk47 Mutant",
    "DT MDR 5.56x45",
    "DT NDR .308",
    "HK 416A5",
    "Colt M4A1",
    "SIG MCX",
    "DS Arms SA-58",
    "Lone Star TX-15 DML",
    "Vepr AKM / VPO-209 (.366)",
    "Vepr KM / VPO-136 (7.62x39)",
    "Simonov OP-SKS",
    "Simonov SKS (No Dovetail)",
    "Vepr Hunter / VPO-101",
    "RPK-16",
    "HK MP5",
    "HK MP5K-N",
    "HK MP7A1",
    "HK MP7A2",
    "B&T MP9",
    "B&T MP9-N",
    "SIG MPX",
    "FN P90",
    "PP-19-01 Vityaz-SN",
    "PP-9 \"Klin\"",
    "PP-91 \"Kedr\"",
    "PP-9 \"Klin\"",
    "PPSH-41",
    "Saiga-9",
    "STM-9",
    "HK UMP 45",
    "KRISS Vector .45",
    "KRISS Vector 9x19",
    "Mossberg 590A1",
    "Remington M870",
    "MP-133",
    "MP-153",
    "MP-155",
    "Saiga-12",
    "TOZ-106",
    "TOZ KS-23M",
    "Springfield Armory M1a",
    "SWORD International Mk-18",
    "Kel-Tec RFB",
    "Remington R11 RSASS",
    "Knight's Armament Company SR-25",
    "LOBAEV Arms DVL-10 Saboteur",
    "Remington M700",
    "SV-98",
    "Orsis T-5000M",
    "Molot VPO-215 bolt-action",
    "APB",
    "APS",
    "FN 5-7",
    "Glock 17",
    "Glock 18C",
    "Colt M1911A1",
    "Colt M45A1",
    "Beretta M9A3",
    "Yarygin MP-443 Grach",
    "SIG P226R",
    "PB",
    "PL15",
    "PM (t) \"Makarov\"",
    "PM \"Makarov\"",
    "Serdyukov SR-1MP Gyurza",
    "TT pistol",
    "TT pistol (Gold)"
]
armorList = [
    "BNTI Module-3M body armor",
    "PACA soft armor",
    "6B2 armor (Flora)",
    "MF-UNTAR body armor",
    "BNTI Zhuk-3 press armor",
    "6B23-1 body armor (Digital Flora)",
    "BNTI Kirasa-N armor",
    "NFM THOR Concealable Vest body armor",
    "6B13 assault armor",
    "6B23-2 armor (Mountain Flora)",
    "Highcom Trooper TFO armor (Multicam)",
    "BNTI Korund-VM armor",
    "FORT Redut-M body armor",
    "6B13 M assault armor (Tan)",
    "IOTV Gen4 body armor (High Mobility Kit)",
    "BNTI Gzhel-K armor",
    "FORT Defender-2 body armor",
    "IOTV Gen4 body armor (Assault Kit)",
    "IOTV Gen4 body armor (Full Protection)",
    "FORT Redut-T5 body armor",
    "5.11 Tactical Hexgrid plate carrier",
    "NFM THOR Integrated Carrier body armor",
    "BNTI Zhuk-6a heavy armor",
    "LBT 6094A Slick Plate Carrier",
    "6b43 Zabralo-Sh 6A body armor"
]
armorRigList = [
    "6B5-16 Zh-86 \"Uley\" armored rig",
    "6B3TM-01M armored rig",
    "6B5-15 Zh-86 \"Uley\" armored rig",
    "ANA Tactical M2 armored rig",
    "CQC Osprey MK4A plate carrier (Assault, MTP)",
    "ANA Tactical M1 armored rig",
    "Crye Precision AVS plate carrier",
    "Ars Arma A18 Skanda plate carrier",
    "WARTECH TV-110 plate carrier",
    "5.11 Tactical TacTec plate carrier",
    "CQC Osprey MK4A plate carrier (Protection, MTP)",
    "Ars Arma CPC MOD.2 plate carrier",
    "Crye Precision AVS MBAV (Tagilla Edition)"
]
rigList = [
    "Scav Vest",
    "Security Vest",
    "DIY IDEA chest rig",
    "Spiritus Systems Bank Robber chest rig",
    "SOE Micro rig",
    "WARTECH TV-109 + TV-106 chest rig",
    "CSA chest rig",
    "UMTBS 6sh113 Scout-Sniper",
    "Splav Tarzan M22 chest rig",
    "Haley Strategic D3CRX Chest Harness",
    "Dynaforce Triton M43-A Chest Harness",
    "Blackhawk! Commando Chest Harness",
    "Direct Action Thunderbolt compact chest rig",
    "Gear Craft GC-BSS-MK1 chest rig",
    "Umka M33-SET1 hunter vest",
    "LBT-1961A Load Bearing chest rig",
    "Stich Profi Chest Rig MK2 (Recon, A-TACS FG)",
    "Stich Profi Chest Rig MK2 (Assault, A-TACS FG)",
    "BlackRock chest rig",
    "WARTECH MK3 TV-104 chest rig",
    "ANA Tactical Alpha chest rig",
    "Azimut SS Zhuk Chest Harness",
    "Velocity Systems Multi-Purpose Patrol Vest",
    "Belt-A + Belt-B gear rig"
]
helmetList = [
    "Armasight NVG head strap",
    "Wilcox Skull Lock head mount",
    "Tac-Kek FAST MT helmet",
    "TSh-4M-L soft tank crew helmet",
    "Kolpak-1S riot helmet",
    "ShPM Firefighter helmet",
    "PSh-97 \"Djeta\" riot helmet",
    "UNTAR helmet",
    "6B47 Ratnik-BSh helmet",
    "LZSh light helmet",
    "SSh-68 steel helmet",
    "FORT Kiver-M bulletproof helmet",
    "DevTac Ronin ballistic helmet",
    "SSSh-95 Sfera-S helmet",
    "MSA ACH TC-2001 MICH Series helmet",
    "MSA ACH TC-2002 MICH Series helmet",
    "MSA Gallet TC 800 High Cut combat helmet	",
    "Highcom Striker ACHHC IIIA helmet",
    "ZSh-1-2M helmet",
    "Highcom Striker ULACH IIIA helmet",
    "Diamond Age Bastion helmet",
    "Ops-Core FAST MT Super High Cut helmet	",
    "Crye Precision AirFrame helmet (Tan)",
    "Team Wendy EXFIL Ballistic Helmet (Coyote Tan)",
    "Team Wendy EXFIL Ballistic Helmet (Black)",
    "Galvion Caiman Hybrid helmet",
    "BNTI LShZ-2DTM helmet",
    "Maska-1Shch bulletproof helmet",
    "Altyn assault helmet",
    "Rys-T bulletproof helmet",
    "Vulkan-5 (LShZ-5) heavy helmet",
    "Stich Profi Chimera boonie hat",
    "Kinda cowboy hat",
    "Ushanka ear flap hat",
    "MIL-TEC panama hat",
    "\"Door Kicker\" Boonie hat",
    "Bomber Beanie",
    "Shattered light armored mask",
    "Tagilla's welding mask \"Gorilla\"",
]
backpackList = [
    "6Sh118 raid backpack",
    "LBT-2670 Slim Field Med Pack",
    "Mystery Ranch Blackjack 50 backpack (Multicam)",
    "Eberlestock F4 Terminator load bearing backpack (Tiger Stripe)",
    "SSO \"Attack 2\" raid backpack",
    "Pilgrim tourist backpack",
    "3V G Paratus 3-Day Operator's Tactical backpack",
    "Eberlestock G2 Gunslinger II backpack (Dry Earth)",
    "Oakley Mechanism heavy duty backpack (Black)",
    "Camelbak Tri-Zip backpack",
    "ANA Tactical Beta 2 Battle backpack",
    "Eberlestock F5 Switchblade backpack (Dry Earth)",
    "Hazard4 Drawbridge backpack",
    "Hazard4 Takedown sling backpack",
    "Hazard4 Pillbox backpack",
    "WARTECH Berkut BB-102 backpack",
    "LBT-8005A Day Pack backpack",
    "Scav backpack",
    "Flyye MBSS backpack",
    "Sanitar's bag",
    "Duffle bag",
    "LK 3F Transfer tourist backpack",
    "Transformer Bag",
    "VKBO army bag",
    "Tactical sling bag"
]
modifierList = [
    "Up to level 1 traders",
    "Up to level 2 traders",
    "Up to level 3 traders",
    "Up to level 4 traders",
    "No restrictions"
]
mapList = [
    "Factory",
    "Customs",
    "Interchange",
    "Reserve",
    "Shoreline",
    "Woods",
    "Labs"
]
bonusModifiers = [
    "Night time",
    "Hipfire only",
    "Flash grenades only",
    "No meds in pocket",
    "No suppresor",
    "+1 level to all traders",
    "Swap gun and ammo trader level",
    "Ironsights only"
]

rolledWeapon = random.choice(weaponList)
rolledArmor = random.choice(armorList + armorRigList)
rolledRig = random.choice(rigList)
rolledHelmet = random.choice(helmetList)
rolledBackpack = random.choice(backpackList)
rolledGunModifiers = random.choice(modifierList)
rolledAmmoModifiers = random.choice(modifierList)
rolledMap = random.choice(mapList)
rolledBonus = random.choice(bonusModifiers)

print("Welcome to Tarkov Loadout Lottery")
time.sleep(1)
input("Press enter to roll your loadout... ")

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Weapon:", rolledWeapon)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
if rolledArmor in armorList:
    print("Armor:", rolledArmor)
    time.sleep(1)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(1)
    print("Rig:", rolledRig)
else:
    print("Armored Rig:", rolledArmor)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Helmet:", rolledHelmet)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Backpack:", rolledBackpack)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Gun Modifications:", rolledGunModifiers)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Ammunition:", rolledAmmoModifiers)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
print("Map:", rolledMap)
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)

userInput = input("Would you like the bonus modifier? (Y = yes, any other key = no) ")
time.sleep(1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(1)
if userInput.upper() == "Y":
    print("Bonus modifier:", rolledBonus)
    time.sleep(1)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(1)
print("\nThank you!")