from typing import Literal


class Armor:
    def __init__(
            self,
            name: str,
            image_url: str,
            category: Literal["Armor Vest", "Armored Rig"],
            trader: Literal["Prapor", "Therapist", "Fence", "Skier", "Peacekeeper", "Mechanic", "Ragman", "Jaeger", None],
            trader_level: Literal[1, 2, 3, 4, None],
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


Melee = Armor(
    name="",
    image_url="",
    category="",
    trader=None,
    trader_level=None,
    fir_only=False,
    quest_locked=False,
    meta=False,
)
