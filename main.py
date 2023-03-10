import discord
from discord.ext import commands

import asyncio
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

debug_guilds = [1052251792798404719]

bot = commands.Bot(
    intents=discord.Intents.all(),
    debug_guilds=debug_guilds,
)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")


@bot.command(name="ping", description="Check the bot's latency.")
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx: commands.Context):
    await ctx.reply(f":hourglass: **Ping:** {round(bot.latency * 100, 2)} ms")


@bot.event
async def on_application_command_error(ctx: commands.Context, error):
    await ctx.reply(error, ephemeral=True)
    if isinstance(error, commands.CommandOnCooldown):
        await asyncio.sleep(error.retry_after)
        await ctx.message.delete()
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
