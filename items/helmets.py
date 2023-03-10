from typing import Literal


class Helmet:
    def __init__(
            self,
            name: str,
            image_url: str,
            trader: Literal["Prapor", "Therapist", "Fence", "Skier", "Peacekeeper", "Mechanic", "Ragman", "Jaeger", None],
            trader_level: Literal[1, 2, 3, 4, None],
            fir_only: bool,
            quest_locked: bool,
            meta: bool,
    ):
        self.name = name
        self.image_url = image_url
        self.trader = trader
        self.trader_level = trader_level
        self.fir_only = fir_only
        self.quest_locked = quest_locked
        self.meta = meta


Melee = Helmet(
    name="",
    image_url="",
    trader=None,
    trader_level=None,
    fir_only=False,
    quest_locked=False,
    meta=False,
)
