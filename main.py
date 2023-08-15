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


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")


class UserSettings:
    def __init__(self, trader_levels, flea, allow_quest_locked, allow_fir_only, allow_mod_ammo_levels, allow_thermals,
                 meta_only):
        self.trader_levels = trader_levels
        self.flea = flea
        self.allow_quest_locked = allow_quest_locked
        self.allow_fir_only = allow_fir_only
        self.allow_mod_ammo_levels = allow_mod_ammo_levels
        self.allow_thermals = allow_thermals
        self.meta_only = meta_only


def check_traders(item, user_settings) -> bool:
    for trader, trader_info in item.trader_info.items():
        print(f"Checking if {item.name}'s traders are equal or less than the user's trader levels")

        if user_settings.trader_levels[trader] >= trader_info.level:
            if trader_info.barter and not user_settings.flea:
                print(f"{item.name} is at {trader_info} with a barter while user does not have Flea, breaking out")
                break

            elif trader_info.quest_locked and not user_settings.allow_quest_locked:
                print(
                    f"{item.name} is at {trader_info} but is quest-locked and user does not allow quest-locked items, breaking out")
                break

            else:
                print(f"{item.name} is at {trader_info} and user has {user_settings.trader_levels}, returned True")
                return True

    print(f"{item.name} met no conditions while user has {user_settings.trader_levels}, returned False")
    return False


def check_item(item, user_settings) -> bool:
    # print(f"------ CHECKING ITEM {item.name} ------")
    # print(f"Checking if {item.name} is not meta while user settings are meta only")

    if not item.meta and user_settings.meta_only:
        # print(
        # f"{item.name} is not meta ({item.meta}) while user settings are meta only ({user_settings.meta_only}), returned False")
        return False

    # print(f"Checking if {item.name} is unlocked")
    if item.unlocked:
        # print(f"{item.name} is unlocked ({item.unlocked}), returned True")
        return True

    # print(f"Checking if {item.name} is on flea and user has flea.")
    if item.flea and user_settings.flea:
        # print(f"{item.name} is available on flea {item.flea}, and user flea is {user_settings.flea}, returned True")
        return True

    # print(f"Checking if {item.name} is a non-trader flea-banned item.")
    # print(f"not item.flea ({item.flea}) and item.trader_info ({item.trader_info} is None) ")
    # print(f"{not item.flea and item.trader_info is None}")
    if not item.flea and item.trader_info == {}:
        # print(f"{item.name} is a non-trader ({item.trader_info == {} }) flea-banned ({item.flea}) item")
        # print("Checking if user allows fir-only items")
        if user_settings.allow_fir_only:
            # print(f"{item.name} returned true as user has set allow fir-only items to {user_settings.allow_fir_only}")
            return True
        else:
            # print(f"{item.name} returned false as user has set allow fir-only items to {user_settings.allow_fir_only}")
            return False

    return check_traders(item, user_settings)


def roll_items(user_settings) -> list:
    filtered_weapons = [weapon for weapon in eft.ALL_WEAPONS if check_item(weapon, user_settings)]
    # print([i.name for i in filtered_weapons])
    filtered_armor = [armor for armor in eft.ALL_ARMORS if check_item(armor, user_settings)]
    # print([i.name for i in filtered_armor])
    filtered_helmets = [helmet for helmet in eft.ALL_HELMETS if check_item(helmet, user_settings)]
    # print([i.name for i in filtered_helmets])
    filtered_backpacks = [backpack for backpack in eft.ALL_BACKPACKS if check_item(backpack, user_settings)]
    # print([i.name for i in filtered_backpacks])

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

    return rolls


# /roll
@bot.slash_command(name="roll", description="Loadout Lottery!")
@commands.cooldown(1, 20, commands.BucketType.user)
@option(name="prapor", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="therapist", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="skier", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="peacekeeper", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="mechanic", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="ragman", description="Enter Prapor's trader level", choices=[1, 2, 3, 4])
@option(name="jaeger", description="Enter Prapor's trader level", choices=[0, 1, 2, 3, 4])
@option(name="flea", description="Do you have access to the flea market?", choices=[True, False])
@option(name="allow_quest_locked", description="Allow quest locked items to be rolled?", choices=[True, False])
@option(name="allow_fir_only", description="Allow non-trader flea-banned items to be rolled?", choices=[True, False])
@option(name="meta_only", description="Only allow meta items to be rolled?", choices=[True, False])
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
        allow_quest_locked: bool,
        allow_fir_only: bool,
        meta_only: bool,
):
    # Making the embed look nice
    embed_msg = discord.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery",
        color=ctx.bot.user.color.value
    )
    embed_msg.set_author(
        name="Support Server",
        icon_url="https://i.imgur.com/tqtPhBA.png",
        url="https://discord.gg/mgXmtMZgfb"
    )
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    # Defining user settings based on command arguments (temporarily)
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
        allow_quest_locked=allow_quest_locked,
        allow_fir_only=allow_fir_only,
        meta_only=meta_only,
        allow_mod_ammo_levels=False,
        allow_thermals=False,
    )

    # Cannot unlock Prapor, Skier, Mechanic, Ragman, or Jaeger LL2 without unlocking Flea market
    # Could integrate this logic into the /settings command once its made
    if (user_settings.trader_levels[eft.Trader.PRAPOR] >= 2
            or user_settings.trader_levels[eft.Trader.SKIER].value >= 2
            or user_settings.trader_levels[eft.Trader.MECHANIC].value >= 2
            or user_settings.trader_levels[eft.Trader.RAGMAN].value >= 2
            or user_settings.trader_levels[eft.Trader.JAEGER].value >= 2):
        user_settings.flea = True

    # Roll a random selection of items for the user based on their settings
    rolls = roll_items(user_settings)

    # Message is finally sent
    await ctx.respond(embed=embed_msg)

    # Slowly edits the message to reveal each rolled item
    for rolled_item in rolls:
        embed_msg.set_image(url="")
        embed_msg.add_field(name=f"{rolled_item.category.value}:", value="?", inline=False)
        await ctx.edit(embed=embed_msg)
        await asyncio.sleep(1)
        embed_msg.set_field_at(index=-1, name=f"{rolled_item.category.value}:", value=f"{rolled_item.name}")
        embed_msg.set_image(url=rolled_item.image_url)
        await ctx.edit(embed=embed_msg)
        await asyncio.sleep(1.5)

    # End of the command
    await asyncio.sleep(6)
    embed_msg.set_image(url="")
    embed_msg.set_footer(text="https://trello.com/b/A2xmLoBw/tarkov-loadout-lottery-discord-bot")
    await ctx.edit(embed=embed_msg)


# /settings
@bot.slash_command(name="settings", description="Customise your Loadout Lottery experience.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def settings(ctx: discord.ApplicationContext) -> None:
    await ctx.respond("This command has yet to do anything.")


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


# Application command error handler
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(
            f":hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.")
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
