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

import eft

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

debug_guilds = [
    1052251792798404719,  # bot dev
]

bot = commands.Bot(
    debug_guilds=debug_guilds,
    help_command=commands.DefaultHelpCommand()
)


class UserSettings:
    def __init__(self, trader_levels, flea, allow_quest_locked, allow_mod_ammo_levels, allow_thermals, meta_only):
        self.trader_levels = trader_levels
        self.flea = flea
        self.allow_quest_locked = allow_quest_locked
        self.allow_mod_ammo_levels = allow_mod_ammo_levels
        self.allow_thermals = allow_thermals
        self.meta_only = meta_only


def check_item_trader(item, user_settings):
    for trader, trader_info in item.trader_info.items():
        if user_settings.trader_levels[trader] >= trader_info.level:
            if trader_info.barter and not user_settings.flea:
                return False
            if trader_info.quest_locked and not user_settings.allow_quest_locked:
                return False
            return True


def check_item(item, user_settings):
    if not item.meta and user_settings.meta_only:
        return False
    if item.force:
        return True
    if item.flea and user_settings.flea:
        return True
    check_item_trader(item, user_settings)
    return False


def roll_items(user_settings):
    filtered_weapons = [weapon for weapon in eft.ALL_WEAPONS if check_item(weapon, user_settings)]
    print([i.name for i in filtered_weapons])
    filtered_armor = [armor for armor in eft.ALL_ARMORS if check_item(armor, user_settings)]
    print([i.name for i in filtered_armor])
    filtered_helmets = [helmet for helmet in eft.ALL_HELMETS if check_item(helmet, user_settings)]
    print([i.name for i in filtered_helmets])
    filtered_backpacks = [backpack for backpack in eft.ALL_BACKPACKS if check_item(backpack, user_settings)]
    print([i.name for i in filtered_backpacks])

    rolled_weapon = random.choice(filtered_weapons)
    rolled_armor = random.choice(filtered_armor)
    rolled_helmet = random.choice(filtered_helmets)
    rolled_backpack = random.choice(filtered_backpacks)
    rolled_map = random.choice(eft.ALL_MAPS)
    rolled_random_modifier = random.choice(random.choice(eft.ALL_MODIFIERS))

    if rolled_armor.category.value == "Armor Vest":
        filtered_rigs = [rig for rig in eft.ALL_RIGS if check_item(rig, user_settings)]
        rolled_rig = random.choice(filtered_rigs)
        rolls = [rolled_weapon, rolled_armor, rolled_rig, rolled_helmet, rolled_backpack, rolled_map,
                 rolled_random_modifier]
    else:
        rolls = [rolled_weapon, rolled_armor, rolled_helmet, rolled_backpack, rolled_map, rolled_random_modifier]

    # testing
    print([i.name for i in rolls])
    return rolls


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
@option("prapor", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("therapist", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("skier", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("peacekeeper", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("mechanic", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("ragman", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option("jaeger", description="Enter Prapor's trader level", choices=[0, 1, 2, 3, 4])
@option("flea", description="Do you have access to the flea market?", choices=[True, False])
@option("quest_locked", description="Allow quest locked items to be rolled?", choices=[True, False])
@option("meta_only", description="Only allow meta items to be rolled?", choices=[True, False])

async def roll(
        ctx: discord.ApplicationContext,
        prapor: int,
        therapist: int,
        skier: int,
        peacekeeper: int,
        mechanic: int,
        ragman: int,
        jaeger: int,
        flea: bool,
        quest_locked: bool,
        meta_only: bool,
):

    embed_msg = discord.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery",
        color=ctx.bot.user.color
    )

    user_settings = UserSettings(
        trader_levels={
            eft.Trader.PRAPOR: prapor,
            eft.Trader.THERAPIST: therapist,
            eft.Trader.SKIER: skier,
            eft.Trader.PEACEKEEPER: peacekeeper,
            eft.Trader.MECHANIC: mechanic,
            eft.Trader.RAGMAN: ragman,
            eft.Trader.JAEGER: jaeger,
        },
        flea=flea,
        allow_quest_locked=quest_locked,
        meta_only=meta_only,
        allow_mod_ammo_levels=False,
        allow_thermals=False,
    )

    embed_msg.set_author(
        name="Support & LFG Server",
        icon_url="https://i.imgur.com/ptkBfO2.png",
        url="https://discord.gg/mgXmtMZgfb"
    )
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    rolls = roll_items(user_settings)

    await ctx.respond(embed=embed_msg)
    for rolled_item in rolls:
        await asyncio.sleep(1.5)
        embed_msg.set_image(url="")
        embed_msg.add_field(name=f"{rolled_item.category.value}:", value="?", inline=True)
        await ctx.edit(embed=embed_msg)
        await asyncio.sleep(1)
        embed_msg.set_field_at(index=-1, name=f"{rolled_item.category.value}:", value=f"{rolled_item.name}")
        embed_msg.set_image(url=rolled_item.image_url)
        await ctx.edit(embed=embed_msg)
    await asyncio.sleep(3)
    embed_msg.set_image(url="")
    embed_msg.set_footer(text="https://trello.com/b/A2xmLoBw/tarkov-loadout-lottery-discord-bot")
    await ctx.edit(embed=embed_msg)


# Application command error handler
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f":hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.")
    if isinstance(error, discord.errors.NotFound) and "Unknown Webhook" in str(error):
        await ctx.respond("An error occurred while editing the interaction response. Please try again.")
    else:
        raise error


def run_bot() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()
    load_dotenv()
    bot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    run_bot()
