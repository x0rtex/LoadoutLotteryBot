from utils import eft

# User Settings Type
UserSettings = dict[
               str: bool,
               str: bool,
               str: bool,
               str: bool,
               str: bool,
               str: {
                   eft.PRAPOR: 1 | 2 | 3 | 4,
                   eft.THERAPIST: 1 | 2 | 3 | 4,
                   eft.SKIER: 1 | 2 | 3 | 4,
                   eft.PEACEKEEPER: 1 | 2 | 3 | 4,
                   eft.MECHANIC: 1 | 2 | 3 | 4,
                   eft.RAGMAN: 1 | 2 | 3 | 4,
                   eft.JAEGER: 0 | 1 | 2 | 3 | 4,
               },
            ]

DEFAULT_SETTINGS: UserSettings = {
    "flea": True,
    "allow_quest_locked": True,
    "allow_fir_only": False,
    "meta_only": False,
    "roll_thermals": False,
    "trader_levels": {
        eft.PRAPOR: 4,
        eft.THERAPIST: 4,
        eft.SKIER: 4,
        eft.PEACEKEEPER: 4,
        eft.MECHANIC: 4,
        eft.RAGMAN: 4,
        eft.JAEGER: 4,
    },
}