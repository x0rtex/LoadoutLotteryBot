import discord
from discord.ext import commands
from discord import option

import asyncio
import random
import os
from dotenv import load_dotenv
import logging
import time
import datetime
import platform
import psutil

import eft_items.weapons
import eft_items.armors
import eft_items.rigs
import eft_items.helmets
import eft_items.backpacks
import eft_items.maps

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

debug_guilds = [
    1052251792798404719,
    1052251792798404719,
    489547721846423562,
]

bot = commands.Bot(
    debug_guilds=debug_guilds,
)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")


# /ping
@bot.slash_command(name="ping", description="Check the bot's latency.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f":ping_pong: **Ping:** {round(bot.latency * 100, 2)} ms")


# /stats
@bot.slash_command(name="stats", description="Displays the bot's statistics")
@commands.cooldown(1, 5, commands.BucketType.user)
async def stats(ctx: discord.ApplicationContext) -> None:
    embed_msg = discord.Embed(title=":robot: Bot Statistics")
    embed_msg.set_thumbnail(url="https://i.imgur.com/vCdkZal.png")

    proc = psutil.Process()
    with proc.oneshot():
        uptime = datetime.timedelta(seconds=time.time() - proc.create_time())
        cpu = proc.cpu_times()
        cpu_time = datetime.timedelta(seconds=cpu.system + cpu.user)
        mem_total = psutil.virtual_memory().total / (1024 ** 2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
    fields = [
        ("Python version", platform.python_version(), True),
        ("Pycord version", discord.__version__, True),
        ("Uptime", uptime, True),
        ("CPU time", cpu_time, True),
        ("Memory usage", f"{mem_usage:,.0f} MiB / {mem_total:,.0f} MiB ({mem_of_total:,.0f}%)", True),
        ("Servers", len(bot.guilds), True)
    ]
    for name, value, inline in fields:
        embed_msg.add_field(name=name, value=value, inline=inline)
    await ctx.respond(embed=embed_msg)


# /roll
@bot.slash_command(name="roll", description="Loadout Lottery!")
@commands.cooldown(1, 20, commands.BucketType.user)
@option("user_trader_level", description="Choose your trader levels", choices=[1, 2, 3, 4])
@option("allow_quest_locked", description="Allow items that are quest locked?", choices=[True, False])
@option("allow_fir_only", description="Allow rare items that are ONLY obtainable in raid?", choices=[True, False])
@option("meta_only", description="Would you like to roll only meta items (True), or all items? (False)", choices=[True, False])
async def roll(
        ctx: discord.ApplicationContext,
        user_trader_level: int,
        allow_quest_locked: bool,
        allow_fir_only: bool,
        meta_only: bool,
):

    embed_msg = discord.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery",
    )

    embed_msg.set_author(
        name="Support & LFG Server",
        icon_url="https://i.imgur.com/ptkBfO2.png",
        url="https://discord.gg/mgXmtMZgfb"
    )

    weapon_roll_list = [item for item in eft_items.weapons.weapon_list]
    armor_roll_list = [item for item in eft_items.armors.armor_list]
    rig_roll_list = [item for item in eft_items.rigs.rig_list]
    helmet_roll_list = [item for item in eft_items.helmets.helmet_list]
    backpack_roll_list = [item for item in eft_items.backpacks.backpack_list]

    for item in weapon_roll_list.copy():
        if (not item.meta and meta_only) or (item.trader_level > user_trader_level) or (item.quest_locked and not allow_quest_locked) or (item.fir_only and not allow_fir_only):
            weapon_roll_list.remove(item)

    rolled_weapon = random.choice(weapon_roll_list)

    await ctx.respond(f"Rolled! Meta only = `{meta_only}`, trader levels = `{user_trader_level}`, quest locked items = `{allow_quest_locked}` and fir only items = `{allow_fir_only}`.\nYour rolled item is `{rolled_weapon.name}`")
    await ctx.send(f"{rolled_weapon.image_url}")


# Application command error handler
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f":hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.")
    else:
        raise error  # Raise other errors so they aren't ignored


def run_bot() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()
    load_dotenv()
    bot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    run_bot()
