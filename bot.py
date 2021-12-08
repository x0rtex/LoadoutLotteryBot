import asyncio
import nextcord
import random
import time
from nextcord.ext import commands

import bot_token
from lists import *

ts = time.gmtime()
user_reroll = ""

client = commands.Bot(command_prefix="!")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game("!help"))
    print("BOT ONLINE")
    while True:
        print("List of guilds as of:", time.strftime("%x %X", ts), client.guilds)
        await asyncio.sleep(7200)


# Button to roll a bonus modifier
class BonusButton(nextcord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.value = None
        self.ctx = ctx

    async def interaction_check(self, interaction):
        return self.ctx.author == interaction.user

    @nextcord.ui.button(label="Roll Optional Bonus Modifier", style=nextcord.ButtonStyle.green)
    async def confirm(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.gray)
    async def cancel(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = False
        self.stop()


# Buttons for every re-rollable category
class RerollAnythingButton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = "None"

    @nextcord.ui.button(label="Weapon", style=nextcord.ButtonStyle.primary)
    async def weapon(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Weapon"
        self.stop()

    @nextcord.ui.button(label="Armor", style=nextcord.ButtonStyle.primary)
    async def armor(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Armor"
        self.stop()

    @nextcord.ui.button(label="Rig", style=nextcord.ButtonStyle.primary)
    async def rig(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Rig"
        self.stop()

    @nextcord.ui.button(label="Armored Rig", style=nextcord.ButtonStyle.primary)
    async def armored_rig(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Armored Rig"
        self.stop()

    @nextcord.ui.button(label="Helmet", style=nextcord.ButtonStyle.primary)
    async def helmet(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Helmet"
        self.stop()

    @nextcord.ui.button(label="Backpack", style=nextcord.ButtonStyle.primary)
    async def backpack(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Backpack"
        self.stop()

    @nextcord.ui.button(label="Gun mods", style=nextcord.ButtonStyle.primary)
    async def gun_mods(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Gun mods"
        self.stop()

    @nextcord.ui.button(label="Ammo", style=nextcord.ButtonStyle.primary)
    async def ammo(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Ammo"
        self.stop()

    @nextcord.ui.button(label="Map", style=nextcord.ButtonStyle.primary)
    async def map(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Map"
        self.stop()


@client.command(name="roll", description="Classic Tarkov Loadout Lottery uses a super quantum algorithm to generate a "
                                         "random loadout and map for you to play with.")
async def roll(ctx):
    print("!roll", ctx.message)
    rollmsg = await ctx.reply("Welcome to Tarkov Loadout Lottery!")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Weapon:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(weapon_list)}")
    await asyncio.sleep(1)

    rolled_armor = random.choice(armor_list + armor_rig_list)

    if rolled_armor in armor_list:
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Armor:**")
        await asyncio.sleep(1)
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(armor_list)}")
        await asyncio.sleep(1)
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rig:**")
        await asyncio.sleep(1)
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(rig_list)}")
    else:
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Armored Rig:**")
        await asyncio.sleep(1)
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(armor_rig_list)}")

    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Helmet:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(helmet_list)}")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Backpack:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(backpack_list)}")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Gun Mods:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(modifier_list)}")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Ammo:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(modifier_list)}")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Map:**")
    await asyncio.sleep(1)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(map_list)}")
    await asyncio.sleep(1)

    view1 = BonusButton(ctx)
    rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", view=view1)
    await view1.wait()
    rollmsg = await rollmsg.edit(view=None)

    if view1.value:
        rolled_bonus = random.choice(random.choice(bonus_list))
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Bonus modifier:**")
        await asyncio.sleep(1)
        rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {rolled_bonus}")
        await asyncio.sleep(1)

        if rolled_bonus == "Re-roll anything":
            view2 = RerollAnythingButton()
            rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
                                         view=view2)
            await view2.wait()
            rollmsg = await rollmsg.edit(view=None)

            if view2.value == "Weapon":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled weapon:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(weapon_list)}")
            if view2.value == "Armor":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled armor:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(armor_list)}")
            if view2.value == "Rig":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled rig:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(rig_list)}")
            if view2.value == "Armored Rig":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled armored rig:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(armor_rig_list)}")
            if view2.value == "Helmet":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled helmet:** ")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(helmet_list)}")
            if view2.value == "Backpack":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled backpack:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(backpack_list)}")
            if view2.value == "Gun mods":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled gun mods:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(modifier_list)}")
            if view2.value == "Ammo":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled ammo:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(modifier_list)}")
            if view2.value == "Map":
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content}\n**Rerolled map:**")
                await asyncio.sleep(1)
                rollmsg = await rollmsg.edit(content=f"{rollmsg.content} {random.choice(map_list)}")
    await asyncio.sleep(1)
    await rollmsg.edit(content=f"{rollmsg.content}\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


@client.command(description="Commands List")
async def help(ctx):
    print("!help", ctx.message)
    embed = nextcord.Embed(
        title="Tarkov Loadout Lottery Help - Commands are case-sensitive", description="Commands ""List")
    for command in client.walk_commands():
        description = command.description
        if not description or description is None or description == "":
            description = "No Description Provided"
        embed.add_field(name=f"`!{command.name}{command.signature if command.signature is not None else ''}`",
                        value=description)
    await ctx.send(embed=embed)


@client.command(description="Pong!")
async def ping(ctx):
    print("!ping", ctx.message)
    await ctx.reply("pong")


client.run(bot_token.TOKEN)
