from __future__ import annotations

import asyncio
import datetime
import logging
import os
import platform
import time

import discord
import psutil
from discord import option
from discord.ext import commands
from dotenv import load_dotenv

from utils import eft, roll_logic, users, db, msgs, views

# Bot logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

bot = commands.Bot(help_command=commands.DefaultHelpCommand())


# Bot startup message
@bot.event
async def on_ready() -> None:
    await bot.change_presence(activity=discord.Game("/help"))
    bot.add_view(views.RandomModifierButton())
    logging.info(f"Logged in as {bot.user}")
    logging.info(f"Guilds: {len(bot.guilds)}")


# /roll
@bot.slash_command(name="roll", description="Loadout Lottery!")
@commands.cooldown(1, 20, commands.BucketType.channel)
async def roll(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)
    db.initialize_database()
    user_settings = db.read_user_settings(ctx.user.id)

    embed_msg = msgs.create_embed(ctx, user_settings)
    filtered_items, rolls, need_rig = roll_logic.roll_items(user_settings)

    for rolled_item in rolls:
        await roll_logic.reveal_roll(ctx, embed_msg, rolled_item, "")

    button = views.RandomModifierButton()
    embed_msg.set_image(url="")
    await ctx.edit(embed=embed_msg, view=button)
    await button.wait()
    if button.value:
        rolled_random_modifier = roll_logic.roll_random_modifier(user_settings)
        await asyncio.sleep(1)
        await roll_logic.reveal_roll(ctx, embed_msg, rolled_random_modifier, "")

        # Check if random modifier requires further action
        await roll_logic.is_random_modifier_special(rolled_random_modifier, need_rig, ctx, embed_msg, filtered_items)

    await asyncio.sleep(5)
    embed_msg.set_image(url="")
    embed_msg.set_footer(text="Enjoy!")
    await ctx.edit(embed=embed_msg, view=None)


# /fastroll
@bot.slash_command(name="fastroll", description="Loadout Lottery! (Without the waiting around)")
@commands.cooldown(1, 5, commands.BucketType.user)
async def fastroll(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)
    db.initialize_database()
    user_settings = db.read_user_settings(ctx.user.id)

    embed_msg = msgs.create_embed(ctx, user_settings)
    filtered_items, rolls, need_rig = roll_logic.roll_items(user_settings)

    for rolled_item in rolls:
        embed_msg.add_field(name=f"{rolled_item.category}:", value=f"{rolled_item.name}", inline=False)

    button = views.RandomModifierButton()
    await ctx.respond(embed=embed_msg, view=button)
    await button.wait()
    if button.value:
        rolled_random_modifier = roll_logic.roll_random_modifier(user_settings)
        embed_msg.add_field(
            name=f"{rolled_random_modifier.category}:",
            value=f"{rolled_random_modifier.name}",
            inline=False,
        )

        await roll_logic.is_random_modifier_special(rolled_random_modifier, need_rig, ctx, embed_msg, filtered_items)

    embed_msg.set_footer(text="Enjoy!")
    await ctx.edit(embed=embed_msg, view=None)


# /settings
@bot.slash_command(name="settings", description="Customise your Loadout Lottery experience.")
@commands.cooldown(1, 10, commands.BucketType.user)
@option(name="prapor", description="Enter Prapor's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="therapist", description="Enter Therapist's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="skier", description="Enter Skier's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="peacekeeper", description="Enter Peacekeeper's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="mechanic", description="Enter Mechanic's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="ragman", description="Enter Ragman's trader level", type=int, choices=[1, 2, 3, 4])
@option(name="jaeger", description="Enter Jaeger's trader level", type=int, choices=[0, 1, 2, 3, 4])
@option(name="flea", description="Do you have access to the flea market?", type=bool, choices=[True, False])
@option(name="allow_quest_locked", description="Allow quest locked items to be rolled?", type=bool, choices=[True, False])
@option(name="allow_fir_only", description="Allow non-trader flea-banned items to be rolled?", type=bool, choices=[True, False])
@option(name="meta_only", description="Only allow meta items to be rolled?", type=bool, choices=[True, False])
@option(name="roll_thermals", description="Be able to roll thermal as a random modifier?", type=bool, choices=[True, False])
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
) -> None:
    msgs.print_command_timestamp(ctx)

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
    ll2: int = 2
    if user_settings["flea"] is False and (
            user_settings["trader_levels"][eft.PRAPOR] >= ll2
            or user_settings["trader_levels"][eft.SKIER] >= ll2
            or user_settings["trader_levels"][eft.MECHANIC] >= ll2
            or user_settings["trader_levels"][eft.RAGMAN] >= ll2
            or user_settings["trader_levels"][eft.JAEGER] >= ll2
    ):
        user_settings["flea"] = True

    db.initialize_database()
    db.write_user_settings(ctx.user.id, user_settings)

    embed_msg = msgs.show_user_settings(user_settings, ctx)
    embed_msg.title = "Your settings have been updated:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /viewsettings
@bot.slash_command(name="viewsettings", description="View your currently saved Loadout Lottery settings.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def viewsettings(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)

    try:
        db.initialize_database()
        user_settings = db.read_user_settings(ctx.user.id)
    except FileNotFoundError:
        user_settings = users.DEFAULT_SETTINGS

    embed_msg = msgs.show_user_settings(user_settings, ctx)
    embed_msg.title = "Your currently saved settings:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /resetsettings
@bot.slash_command(name="resetsettings", description="Reset your currently saved Loadout Lottery settings to default.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def resetsettings(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)

    db.initialize_database()
    db.write_user_settings(ctx.user.id, users.DEFAULT_SETTINGS)
    embed_msg = msgs.show_user_settings(users.DEFAULT_SETTINGS, ctx)
    embed_msg.title = "Your settings have been reset to default:"
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /ping
@bot.slash_command(name="ping", description="Check the bot's latency.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)

    await ctx.respond(f":ping_pong: **Ping:** {round(bot.latency * 100, 2)} ms")


# /stats
@bot.slash_command(name="stats", description="Displays the bot's statistics")
@commands.cooldown(1, 5, commands.BucketType.user)
async def stats(ctx: discord.ApplicationContext) -> None:
    msgs.print_command_timestamp(ctx)

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
        ("Servers", len(bot.guilds), True),
    ]

    for name, value, inline in fields:
        embed_msg.add_field(name=name, value=value, inline=inline)

    await ctx.respond(embed=embed_msg)


@bot.event  # Application command error handler
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException) -> None:
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(
            f":hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.",
            ephemeral=True,
        )

    elif isinstance(error, commands.DisabledCommand):
        await ctx.respond(
            f"{ctx.command} has been disabled.",
            ephemeral=True,
        )

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.respond(
            f":warning: **Bot is missing permissions:** {error.missing_permissions}. ",
            ephemeral=True,
        )

    elif isinstance(error, commands.BotMissingAnyRole):
        await ctx.respond(
            f":warning: **Bot is missing roles:** {error.missing_roles}.",
            ephemeral=True,
        )

    elif isinstance(error, commands.TooManyArguments):
        await ctx.respond(
            f"::warning: **Too many arguments:** {error.args}.",
            ephemeral=True,
        )

    elif isinstance(error, commands.BadArgument):
        await ctx.respond(
            f"::warning: **Invalid argument:** {error.args}.",
            ephemeral=True,
        )

    else:
        raise error


def run_bot() -> None:
    if os.name != "nt":  # Use uvloop if using linux
        import uvloop
        uvloop.install()
    load_dotenv()
    bot.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    run_bot()
