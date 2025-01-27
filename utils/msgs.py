import logging
import time

import discord
from utils import users

# Embed Strings
REROLLED_PREFIX: str = "Rerolled "
SUPPORT_SERVER: str = "Support Server"
DISCORD_SERVER: str = "https://discord.gg/mgXmtMZgfb"
LOADOUT_LOTTERY_ICON: str = "https://i.imgur.com/tqtPhBA.png"
GITHUB_URL: str = "https://github.com/x0rtex/LoadoutLotteryBot"
WELCOME_TEXT: str = "🎲 Welcome to Loadout Lottery! 🎰"
WELCOME_TEXT_META: str = "🎲 Welcome to META Loadout Lottery! 🎰"


def create_embed(ctx: discord.ApplicationContext, user_settings: users.UserSettings) -> discord.Embed:
    embed_msg = discord.Embed(title=WELCOME_TEXT_META if user_settings["meta_only"] else WELCOME_TEXT, url=GITHUB_URL)
    embed_msg.set_author(name=SUPPORT_SERVER, icon_url=LOADOUT_LOTTERY_ICON, url=DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.interaction.user.display_avatar.url)
    return embed_msg


def print_command_timestamp(ctx: discord.ApplicationContext) -> None:
    logging.info(f"*️⃣️ {time.ctime(time.time())} *️⃣️ /{ctx.command.name} *️⃣")


def show_user_settings(user_settings: users.UserSettings, ctx: discord.ApplicationContext) -> discord.Embed:
    embed_msg = discord.Embed()
    embed_msg.set_author(name=SUPPORT_SERVER, icon_url=LOADOUT_LOTTERY_ICON, url=DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.interaction.user.display_avatar.url)

    fields: list = [
                       (trader, "Locked" if level == 0 else f"LL{level}")
                       for trader, level in user_settings["trader_levels"].items()
                   ] + [
                       ("Flea Market", user_settings["flea"]),
                       ("Allow Quest Locked Items", user_settings["allow_quest_locked"]),
                       ("Allow FIR-Only Items", user_settings["allow_fir_only"]),
                       ("Allow thermals", user_settings["roll_thermals"]),
                       ("Meta Only", user_settings["meta_only"]),
                   ]

    for name, value in fields:
        embed_msg.add_field(name=name, value=value)

    return embed_msg