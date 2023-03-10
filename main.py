import discord
from discord.ext import commands
from discord import option

import asyncio
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

debug_guilds = [
    1052251792798404719,
    1052251792798404719
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


# /roll
@bot.slash_command(name="roll", description="Loadout Lottery!")
@commands.cooldown(1, 20, commands.BucketType.user)
@option("items", description="Would you like to roll between all items, or only meta items?", choices=["Standard", "Meta Only"])
async def roll(ctx: discord.ApplicationContext, items: str):
    await ctx.respond(f"Rolled! You chose {items} Loadout Lottery")


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
