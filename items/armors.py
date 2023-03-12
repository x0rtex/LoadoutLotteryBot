from typing import Literal


class Armor:
    def __init__(
            self,
            name: str,
            image_url: str,
            category: Literal["Armor Vest", "Armored Rig"],
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


armor_vest_list = [

    No_Armor := Armor(
        name="No Armor",
        image_url="https://i.imgur.com/V2SWmZh.png",
        category="Armor Vest",
        trader=None,
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

    Module_3M := Armor(
        name="BNTI Module-3M body armor",
        image_url="https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/f/f8/3M_icon.png/revision/latest/scale-to-width-down/190?cb=20190519124804",
        category="Armor Vest",
        trader="Flea",
        trader_level=0,
        fir_only=False,
        quest_locked=False,
        meta=False,
    ),

]

armored_rig_list = [



]

armor_list = armor_vest_list + armored_rig_list
