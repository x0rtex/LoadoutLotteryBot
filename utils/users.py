from dataclasses import asdict, dataclass, field
from typing import Self

from utils.eft import Trader


@dataclass(frozen=True)
class TraderLevels:
    prapor: int = 4
    therapist: int = 4
    skier: int = 4
    peacekeeper: int = 4
    mechanic: int = 4
    ragman: int = 4
    jaeger: int = 4
    ref: int = 4

    def get_level(self: Self, trader: Trader) -> int:
        return getattr(self, trader.value)

    def all_levels(self: Self) -> list[int]:
        return [self.prapor, self.therapist, self.skier, self.peacekeeper, self.mechanic, self.ragman, self.jaeger, self.ref]


@dataclass(frozen=True)
class UserSettings:
    flea: bool = True
    allow_quest_locked: bool = True
    allow_fir_only: bool = False
    meta_only: bool = False
    roll_thermals: bool = False
    trader_levels: TraderLevels = field(default_factory=TraderLevels)

    def to_dict(self: Self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "UserSettings":
        return cls(
            flea=data["flea"],
            allow_quest_locked=data["allow_quest_locked"],
            allow_fir_only=data["allow_fir_only"],
            meta_only=data["meta_only"],
            roll_thermals=data["roll_thermals"],
            trader_levels=TraderLevels(**data["trader_levels"]),
        )
