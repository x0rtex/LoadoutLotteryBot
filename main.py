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
import tomllib
import tomli_w

import eft  # contains all information about items from EFT

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


def check_item_traders(item, user_settings) -> bool:  # Check if one or more traders meets user requirements
    for trader, trader_info in item.trader_info.items():
        if user_settings["trader_levels"][trader] >= trader_info.level:
            if trader_info.barter and not user_settings["flea"]:
                break
            elif trader_info.quest_locked and not user_settings["allow_quest_locked"]:
                break
            else:
                return True
    return False


def check_item(item, user_settings) -> bool:  # Check if an item is obtainable based on user settings
    if not item.meta and user_settings["meta_only"]:
        return False

    if item.unlocked:
        return True

    if item.flea and user_settings["flea"]:
        return True

    if item.trader_info == {} and not item.flea:
        if user_settings["allow_fir_only"]:
            return True
        else:
            return False

    return check_item_traders(item, user_settings)


def check_random_modifier(random_modifier, user_settings) -> bool:
    if random_modifier.name == "Use thermal" and not user_settings["roll_thermals"]:
        return False
    return True


def roll_items(user_settings) -> list:
    filtered_weapons = [weapon for weapon in eft.ALL_WEAPONS if check_item(weapon, user_settings)]
    filtered_armor = [armor for armor in eft.ALL_ARMORS if check_item(armor, user_settings)]
    filtered_helmets = [helmet for helmet in eft.ALL_HELMETS if check_item(helmet, user_settings)]
    filtered_backpacks = [backpack for backpack in eft.ALL_BACKPACKS if check_item(backpack, user_settings)]

    rolled_weapon = random.choice(filtered_weapons)
    rolled_armor = random.choice(filtered_armor)
    rolled_helmet = random.choice(filtered_helmets)
    rolled_backpack = random.choice(filtered_backpacks)
    rolled_map = random.choice(eft.ALL_MAPS)

    filtered_good_modifiers = [good_modifier for good_modifier in eft.GOOD_MODIFIERS]
    filtered_ok_modifiers = [ok_modifier for ok_modifier in eft.OK_MODIFIERS]
    filtered_bad_modifiers = [bad_modifier for bad_modifier in eft.BAD_MODIFIERS]
    filtered_all_modifiers = (filtered_good_modifiers, filtered_ok_modifiers, filtered_bad_modifiers)

    rolled_random_modifier = random.choice(random.choice(filtered_all_modifiers))

    # If armored rig is rolled instead of an armor vest, the user does not need a rig
    if rolled_armor.category == "Armor Vest":
        filtered_rigs = [rig for rig in eft.ALL_RIGS if check_item(rig, user_settings)]
        rolled_rig = random.choice(filtered_rigs)
        rolls = [rolled_weapon, rolled_armor, rolled_rig, rolled_helmet, rolled_backpack, rolled_map, rolled_random_modifier]
    else:
        rolls = [rolled_weapon, rolled_armor, rolled_helmet, rolled_backpack, rolled_map, rolled_random_modifier]
    return rolls


def write_settings(user_settings, user_id):
    with open(f'userdata/{user_id}.toml', 'wb') as f:
        tomli_w.dump(user_settings, f)


def read_settings(user_id):
    with open(f'userdata/{user_id}.toml', 'rb') as f:
        return tomllib.load(f)


def view_settings(user_settings, ctx):
    embed_msg = discord.Embed()
    embed_msg.set_author(name=eft.SUPPORT_SERVER, icon_url=eft.LOADOUT_LOTTERY_ICON, url=eft.DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    fields = [
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
async def roll(ctx: discord.ApplicationContext,):
    embed_msg = discord.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery",
        color=ctx.bot.user.color
    )
    embed_msg.set_author(
        name=eft.SUPPORT_SERVER,
        icon_url=eft.LOADOUT_LOTTERY_ICON,
        url=eft.DISCORD_SERVER
    )
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    try:
        user_settings = read_settings(ctx.user.id)
    except FileNotFoundError:
        user_settings = eft.DEFAULT_SETTINGS

    # Roll a random selection of items for the user based on their settings
    rolls = roll_items(user_settings)

    # Message is finally sent
    await ctx.respond(embed=embed_msg)

    # Slowly edits the message to reveal each rolled item
    for rolled_item in rolls:
        embed_msg.set_image(url="")
        embed_msg.add_field(name=f"{rolled_item.category}:", value="?", inline=False)
        await ctx.edit(embed=embed_msg)
        await asyncio.sleep(1)
        embed_msg.set_field_at(index=-1, name=f"{rolled_item.category}:", value=f"{rolled_item.name}", inline=False)
        embed_msg.set_image(url=rolled_item.image_url)
        await ctx.edit(embed=embed_msg)
        await asyncio.sleep(1.5)

    # End of the command
    await asyncio.sleep(10)
    embed_msg.set_image(url="")
    await ctx.edit(embed=embed_msg)


# /settings
@bot.slash_command(name="settings", description="Customise your Loadout Lottery experience.")
@commands.cooldown(1, 10, commands.BucketType.user)
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
@option(name="roll_thermals", description="Be able to roll thermals in optional random modifier?", choices=[True, False])
async def settings(
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
        roll_thermals: bool,
):

    user_settings = {
        "trader_levels": {
            eft.PRAPOR: prapor,
            eft.THERAPIST: therapist,
            eft.SKIER: skier,
            eft.PEACEKEEPER: peacekeeper,
            eft.MECHANIC: mechanic,
            eft.RAGMAN: ragman,
            eft.JAEGER: jaeger,
        },
        "flea": flea,
        "allow_quest_locked": allow_quest_locked,
        "allow_fir_only": allow_fir_only,
        "meta_only": meta_only,
        "roll_thermals": roll_thermals,
    }

    # Cannot unlock Prapor, Skier, Mechanic, Ragman, or Jaeger LL2 without unlocking Flea market
    if (user_settings["flea"] is False
            and (user_settings["trader_levels"][eft.PRAPOR] >= 2
                 or user_settings["trader_levels"][eft.SKIER] >= 2
                 or user_settings["trader_levels"][eft.MECHANIC] >= 2
                 or user_settings["trader_levels"][eft.RAGMAN] >= 2
                 or user_settings["trader_levels"][eft.JAEGER] >= 2)):
        user_settings["flea"] = True

    write_settings(user_settings, ctx.user.id)

    embed_msg = view_settings(user_settings, ctx)
    embed_msg.title = "Your settings have been updated:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /viewsettings
@bot.slash_command(name="viewsettings", description="View your currently saved Loadout Lottery settings.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def viewsettings(ctx: discord.ApplicationContext):

    try:
        user_settings = read_settings(ctx.user.id)
    except FileNotFoundError:
        user_settings = eft.DEFAULT_SETTINGS

    embed_msg = view_settings(user_settings, ctx)
    embed_msg.title = "Your currently saved settings:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /resetsettings
@bot.slash_command(name="resetsettings", description="Reset your currently saved Loadout Lottery settings to default.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def resetsettings(ctx: discord.ApplicationContext):

    user_settings = eft.DEFAULT_SETTINGS

    write_settings(user_settings, ctx.user.id)

    embed_msg = view_settings(user_settings, ctx)
    embed_msg.title = "Your settings have been reset to default:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


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
    if os.name != "nt":  # Use uvloop if using linux
        import uvloop
        uvloop.install()
    load_dotenv()
    bot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    run_bot()
