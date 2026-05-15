from pathlib import Path

from pydantic import BaseModel


class TraderDefaults(BaseModel):
    prapor: int = 4
    therapist: int = 4
    skier: int = 4
    peacekeeper: int = 4
    mechanic: int = 4
    ragman: int = 4
    jaeger: int = 4
    ref: int = 4


class Settings(BaseModel):
    # Paths
    data_dir: Path = Path(__file__).parent.parent / "data"
    db_path: str = str(Path(__file__).parent.parent / "user_settings.db")

    # Default user settings
    default_flea: bool = True
    default_allow_quest_locked: bool = True
    default_allow_fir_only: bool = False
    default_meta_only: bool = False
    default_roll_thermals: bool = False
    default_traders: TraderDefaults = TraderDefaults()

    # Cooldowns (seconds)
    cooldown_roll: float = 20.0
    cooldown_fastroll: float = 5.0
    cooldown_settings: float = 10.0
    cooldown_viewsettings: float = 10.0
    cooldown_resetsettings: float = 10.0
    cooldown_ping: float = 5.0
    cooldown_stats: float = 5.0

    # Animation timing (seconds)
    delay_before_reveal: float = 1.0
    delay_after_reveal: float = 1.5
    delay_before_random_modifier: float = 1.0
    delay_before_final: float = 5.0

    # Bot
    bot_activity: str = "/help"


settings: Settings = Settings()
