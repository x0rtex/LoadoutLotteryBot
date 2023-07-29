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

import EFT

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

example_settings = {
    'trader_levels': {
        EFT.Trader.PRAPOR: 1,
        EFT.Trader.THERAPIST: 1,
        EFT.Trader.SKIER: 1,
        EFT.Trader.PEACEKEEPER: 1,
        EFT.Trader.MECHANIC: 1,
        EFT.Trader.RAGMAN: 1,
        EFT.Trader.JAEGER: 1,
    },
    'flea': False,
    'allow_quest_locked': False,
    'allow_mod_ammo_levels': False,
    'allow_thermals': False,
    'meta_only': True,
}


def check_item(weapon, user_settings):
    # Check if the weapon has the force flag set to True
    if weapon.force:
        # Check if the weapon is not meta and the user is using meta_only
        if not weapon.meta and user_settings['meta_only']:
            return False
        return True

    # Check if the weapon is obtainable from any trader or the flea market
    for trader, trader_info in weapon.trader_info.items():
        # Check if the user's trader level is equal or higher than the trader's level
        if user_settings['trader_levels'][trader] >= trader_info.level:
            # Check if the weapon is available via barter and the user has access to the flea market,
            # or if the weapon is not locked behind a quest or the user allows quest locked items
            if (trader_info.barter and user_settings['flea']) or (not trader_info.quest_locked or user_settings['allow_quest_locked']):
                # Check if the weapon is meta and the user allows meta-only items
                if weapon.meta and user_settings['meta_only']:
                    return True

    # Check if the weapon is obtainable from the flea market directly
    if weapon.flea and user_settings['flea']:
        # Check if the weapon is meta and the user allows meta-only items
        if weapon.meta and user_settings['meta_only']:
            return True

    return False

def roll_items(user_settings):

    filtered_weapons = [weapon for weapon in EFT.all_weapons if check_item(weapon, user_settings)]
    # filtered_armor = [armor for armor in EFT.all_armors if check_item(armor, user_settings)]
    # filtered_helmets = [helmet for helmet in EFT.all_helmets if check_item(helmet, user_settings)]
    # filtered_backpacks = [backpack for backpack in EFT.all_backpacks if check_item(backpack, user_settings)]

    rolled_weapon = random.choice(filtered_weapons)
    # rolled_armor = random.choice(filtered_armor)
    # rolled_helmet = random.choice(filtered_helmets)
    # rolled_backpack = random.choice(filtered_backpacks)
    # rolled_map = random.choice(EFT.all_maps)
    # rolled_random_modifier = random.choice(EFT.all_modifiers)

    # if rolled_armor.category == "Armor Vest":
    #     filtered_rigs = [rig for rig in EFT.all_rigs if check_item(rig, user_settings)]
    #     rolled_rig = random.choice(filtered_rigs)
    #     rolls = [rolled_weapon, rolled_armor, rolled_rig, rolled_helmet, rolled_backpack, rolled_map, rolled_random_modifier]
    # else:
    #     rolls = [rolled_weapon, rolled_armor, rolled_helmet, rolled_backpack, rolled_map, rolled_random_modifier]

    # For testing
    print([weapon.name for weapon in filtered_weapons])
    print(f"Rolled Weapon: {rolled_weapon.name}")
    return rolled_weapon

# For testing
roll_items(example_settings)

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
async def roll(ctx: discord.ApplicationContext):
    embed_msg = discord.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery",
    )

    embed_msg.set_author(
        name="Support & LFG Server",
        icon_url="https://i.imgur.com/ptkBfO2.png",
        url="https://discord.gg/mgXmtMZgfb"
    )

    # Not fixed yet

    rolls = roll_items(example_settings)

    await ctx.send(embed=embed_msg)
    for rolled_item in rolls:
        await asyncio.sleep(1.5)
        embed_msg.add_field(name=rolled_item.category, value=f"{rolled_item.name} at {rolled_item.trader}", inline=True)
        await ctx.edit(embed=embed_msg)

# Application command error handler
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(
            f":hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.")
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
