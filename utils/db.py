import sqlite3

from utils import eft, users

# Database name
USER_SETTINGS_DB: str = "user_settings.db"


def initialize_database() -> None:
    with sqlite3.connect(USER_SETTINGS_DB) as con:
        c = con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS user_settings (
                        user_id INTEGER PRIMARY KEY,
                        flea BOOLEAN,
                        allow_quest_locked BOOLEAN,
                        allow_fir_only BOOLEAN,
                        meta_only BOOLEAN,
                        roll_thermals BOOLEAN,
                        prapor TINYINT,
                        therapist TINYINT,
                        skier TINYINT,
                        peacekeeper TINYINT,
                        mechanic TINYINT,
                        ragman TINYINT,
                        jaeger TINYINT
                    )""")
        con.commit()


def user_exists(cursor, user_id: int) -> bool:
    cursor.execute("SELECT COUNT(*) FROM user_settings WHERE user_id = ?", (user_id,))
    return cursor.fetchone()[0] > 0


def write_user_settings(user_id: int, user_settings: users.UserSettings) -> None:
    with sqlite3.connect(USER_SETTINGS_DB) as con:
        c = con.cursor()

        if user_exists(c, user_id):
            c.execute("""UPDATE user_settings SET
                            flea = ?,
                            allow_quest_locked = ?,
                            allow_fir_only = ?,
                            meta_only = ?,
                            roll_thermals = ?,
                            prapor = ?,
                            therapist = ?,
                            skier = ?,
                            peacekeeper = ?,
                            mechanic = ?,
                            ragman = ?,
                            jaeger = ?
                        WHERE user_id = ?""",
                      (user_settings["flea"],
                       user_settings["allow_quest_locked"],
                       user_settings["allow_fir_only"],
                       user_settings["meta_only"],
                       user_settings["roll_thermals"],
                       user_settings["trader_levels"][eft.PRAPOR],
                       user_settings["trader_levels"][eft.THERAPIST],
                       user_settings["trader_levels"][eft.SKIER],
                       user_settings["trader_levels"][eft.PEACEKEEPER],
                       user_settings["trader_levels"][eft.MECHANIC],
                       user_settings["trader_levels"][eft.RAGMAN],
                       user_settings["trader_levels"][eft.JAEGER],
                       user_id))

        else:
            c.execute("""INSERT INTO user_settings (
                            user_id,
                            flea,
                            allow_quest_locked,
                            allow_fir_only,
                            meta_only,
                            roll_thermals,
                            prapor,
                            therapist,
                            skier,
                            peacekeeper,
                            mechanic,
                            ragman,
                            jaeger
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (user_id,
                       user_settings["flea"],
                       user_settings["allow_quest_locked"],
                       user_settings["allow_fir_only"],
                       user_settings["meta_only"],
                       user_settings["roll_thermals"],
                       user_settings["trader_levels"][eft.PRAPOR],
                       user_settings["trader_levels"][eft.THERAPIST],
                       user_settings["trader_levels"][eft.SKIER],
                       user_settings["trader_levels"][eft.PEACEKEEPER],
                       user_settings["trader_levels"][eft.MECHANIC],
                       user_settings["trader_levels"][eft.RAGMAN],
                       user_settings["trader_levels"][eft.JAEGER]))

        con.commit()


def read_user_settings(user_id: int) -> dict:
    with sqlite3.connect(USER_SETTINGS_DB) as con:
        c = con.cursor()
        c.execute("SELECT * FROM user_settings WHERE user_id = ?", (user_id,))
        row = c.fetchone()
        if row is None:
            return users.DEFAULT_SETTINGS
        return {
            "flea": bool(row[1]),
            "allow_quest_locked": bool(row[2]),
            "allow_fir_only": bool(row[3]),
            "meta_only": bool(row[4]),
            "roll_thermals": bool(row[5]),
            "trader_levels": {
                eft.PRAPOR: row[6],
                eft.THERAPIST: row[7],
                eft.SKIER: row[8],
                eft.PEACEKEEPER: row[9],
                eft.MECHANIC: row[10],
                eft.RAGMAN: row[11],
                eft.JAEGER: row[12],
            },
        }