import sqlite3

from utils.users import TraderLevels, UserSettings

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
                        jaeger TINYINT,
                        ref TINYINT
                    )""")

        # Migration: Add ref column if it doesn't exist
        c.execute("PRAGMA table_info(user_settings)")
        columns = [row[1] for row in c.fetchall()]
        if "ref" not in columns:
            c.execute("ALTER TABLE user_settings ADD COLUMN ref TINYINT DEFAULT 4")

        con.commit()


def user_exists(cursor, user_id: int) -> bool:
    cursor.execute("SELECT COUNT(*) FROM user_settings WHERE user_id = ?", (user_id,))
    return cursor.fetchone()[0] > 0


def write_user_settings(user_id: int, user_settings: UserSettings) -> None:
    with sqlite3.connect(USER_SETTINGS_DB) as con:
        c = con.cursor()

        if user_exists(c, user_id):
            c.execute(
                """UPDATE user_settings SET
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
                            jaeger = ?,
                            ref = ?
                        WHERE user_id = ?""",
                (
                    user_settings.flea,
                    user_settings.allow_quest_locked,
                    user_settings.allow_fir_only,
                    user_settings.meta_only,
                    user_settings.roll_thermals,
                    user_settings.trader_levels.prapor,
                    user_settings.trader_levels.therapist,
                    user_settings.trader_levels.skier,
                    user_settings.trader_levels.peacekeeper,
                    user_settings.trader_levels.mechanic,
                    user_settings.trader_levels.ragman,
                    user_settings.trader_levels.jaeger,
                    user_settings.trader_levels.ref,
                    user_id,
                ),
            )

        else:
            c.execute(
                """INSERT INTO user_settings (
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
                            jaeger,
                            ref
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    user_id,
                    user_settings.flea,
                    user_settings.allow_quest_locked,
                    user_settings.allow_fir_only,
                    user_settings.meta_only,
                    user_settings.roll_thermals,
                    user_settings.trader_levels.prapor,
                    user_settings.trader_levels.therapist,
                    user_settings.trader_levels.skier,
                    user_settings.trader_levels.peacekeeper,
                    user_settings.trader_levels.mechanic,
                    user_settings.trader_levels.ragman,
                    user_settings.trader_levels.jaeger,
                    user_settings.trader_levels.ref,
                ),
            )

        con.commit()


def read_user_settings(user_id: int) -> UserSettings:
    with sqlite3.connect(USER_SETTINGS_DB) as con:
        c = con.cursor()
        c.execute("SELECT * FROM user_settings WHERE user_id = ?", (user_id,))
        row = c.fetchone()
        if row is None:
            return UserSettings()
        return UserSettings(
            flea=bool(row[1]),
            allow_quest_locked=bool(row[2]),
            allow_fir_only=bool(row[3]),
            meta_only=bool(row[4]),
            roll_thermals=bool(row[5]),
            trader_levels=TraderLevels(
                prapor=row[6],
                therapist=row[7],
                skier=row[8],
                peacekeeper=row[9],
                mechanic=row[10],
                ragman=row[11],
                jaeger=row[12],
                ref=row[13],
            ),
        )
