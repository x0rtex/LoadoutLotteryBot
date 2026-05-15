from dataclasses import asdict, dataclass, field
from typing import Self

from config.config import settings as cfg
from utils.eft import Trader


@dataclass(frozen=True)
class TraderLevels:
    prapor: int = cfg.default_traders.prapor
    therapist: int = cfg.default_traders.therapist
    skier: int = cfg.default_traders.skier
    peacekeeper: int = cfg.default_traders.peacekeeper
    mechanic: int = cfg.default_traders.mechanic
    ragman: int = cfg.default_traders.ragman
    jaeger: int = cfg.default_traders.jaeger
    ref: int = cfg.default_traders.ref

    def get_level(self: Self, trader: Trader) -> int:
        return getattr(self, trader.value)

    def all_levels(self: Self) -> list[int]:
        return [self.prapor, self.therapist, self.skier, self.peacekeeper, self.mechanic, self.ragman, self.jaeger, self.ref]


@dataclass(frozen=True)
class UserSettings:
    flea: bool = cfg.default_flea
    allow_quest_locked: bool = cfg.default_allow_quest_locked
    allow_fir_only: bool = cfg.default_allow_fir_only
    meta_only: bool = cfg.default_meta_only
    roll_thermals: bool = cfg.default_roll_thermals
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
