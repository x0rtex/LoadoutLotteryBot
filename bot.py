import asyncio
import bot_token
import datetime
import lists
import nextcord
from nextcord.ext import commands
import platform
import psutil
import random
import time

client = commands.Bot(command_prefix="t!")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game("t!help"))
    print("BOT ONLINE")
    while True:
        print("List of guilds:", client.guilds)
        await asyncio.sleep(21600)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  # Checks if on cooldown
        await ctx.message.add_reaction("⌛")
        await asyncio.sleep(error.retry_after)
        await ctx.message.clear_reaction("⌛")


@client.command(description="Commands List")
async def help(ctx):
    print(f"{datetime.datetime.now()}, t!help - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}")
    embed = nextcord.Embed(title="Tarkov Loadout Lottery Help - Commands are case-sensitive", description="Commands List")
    for command in client.walk_commands():
        description = command.description
        embed.add_field(name=f"`t!{command.name}{command.signature if command.signature is not None else ''}`", value=description)
    await ctx.send(embed=embed)


@client.command(description="Pong!")
async def ping(ctx):
    print(f"{datetime.datetime.now()}, t!ping - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}")
    start = time.time()
    msg = await ctx.send(f"Pong! DWSP latency: {round (client.latency*1000)} ms.")
    end = time.time()
    await msg.edit(f"Pong! DWSP latency: {round(client.latency * 1000)} ms. Response time: {round((end-start)*1000)} ms.")


@client.command(description="Displays the bot's statistics")
async def stats(ctx):
    embed = nextcord.Embed(title="Bot Statistics", color=ctx.author.color)
    embed.set_thumbnail(url=client.user.avatar.url)

    proc = psutil.Process()
    with proc.oneshot():
        uptime = datetime.timedelta(seconds=time.time()-proc.create_time())
        cpu_time = datetime.timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
        mem_total = psutil.virtual_memory().total / (1024**2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
    fields = [
        ("Python version", platform.python_version(), True),
        ("Nextcord version", nextcord.__version__, True),
        ("Uptime", uptime, True),
        ("CPU time", cpu_time, True),
        ("Memory usage", f"{mem_usage:,.0f} MiB / {mem_total:,.0f} MiB ({mem_of_total:,.0f}%)", True),
        ("Servers", len(client.guilds), True)
    ]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)


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


@client.command(name="roll", description="Classic Tarkov Loadout Lottery uses a super quantum algorithm to generate a random loadout and map for you to play with.")
@commands.cooldown(1, 20, commands.BucketType.channel)
async def roll(ctx):
    print(f"{datetime.datetime.now()}, t!roll - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}")

    rolled_weapon = random.choice(tuple(lists.weapons.keys()))
    rolled_armor = random.choice(tuple(lists.armors.keys()) + tuple(lists.armor_rigs.keys()))
    rolled_rig = random.choice(tuple(lists.rigs.keys()))
    rolled_helmet = random.choice(tuple(lists.helmets.keys()))
    rolled_backpack = random.choice(tuple(lists.backpacks.keys()))
    rolled_map = random.choice(tuple(lists.maps.keys()))

    embed = nextcord.Embed(title="Welcome to Tarkov Loadout Lottery!", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Made by x0rtex", icon_url="https://i.imgur.com/4q2U4QN.png")
    embed.set_thumbnail(url=ctx.message.author.avatar.url)
    embed_msg = await ctx.send(embed=embed)

    await asyncio.sleep(0.66)
    embed.add_field(name="Weapon:", value=":grey_question:", inline=False)
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index = 0
    embed.set_field_at(field_index, name="Weapon:", value=rolled_weapon, inline=False)
    embed.set_image(url=lists.weapons[rolled_weapon])
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(1.5)
    if rolled_armor in lists.armors:
        embed.add_field(name="Armor:", value=":grey_question:", inline=False)
        embed.set_image(url="")
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="Armor:", value=rolled_armor, inline=False)
        embed.set_image(url=lists.armors[rolled_armor])
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(1.5)

        embed.add_field(name="Rig:", value=":grey_question:", inline=False)
        embed.set_image(url="")
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="Rig:", value=rolled_rig, inline=False)
        embed.set_image(url=lists.rigs[rolled_rig])
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(1.5)
    else:
        embed.add_field(name="Armored Rig:", value=":grey_question:", inline=False)
        embed.set_image(url="")
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="Armored Rig:", value=rolled_armor, inline=False)
        embed.set_image(url=lists.armor_rigs[rolled_armor])
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(1.5)
    embed.add_field(name="Helmet:", value=":grey_question:", inline=False)
    embed.set_image(url="")
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index += 1
    embed.set_field_at(field_index, name="Helmet:", value=rolled_helmet, inline=False)
    embed.set_image(url=lists.helmets[rolled_helmet])
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(1.5)

    embed.add_field(name="Backpack:", value=":grey_question:", inline=False)
    embed.set_image(url="")
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index += 1
    embed.set_field_at(field_index, name="Backpack:", value=rolled_backpack, inline=False)
    embed.set_image(url=lists.backpacks[rolled_backpack])
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(1.5)

    embed.add_field(name="Gun Mods:", value=":grey_question:", inline=False)
    embed.set_image(url="")
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index += 1
    embed.set_field_at(field_index, name="Gun Mods:", value=random.choice(lists.modifiers), inline=False)
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)

    embed.add_field(name="Ammo:", value=":grey_question:", inline=False)
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index += 1
    embed.set_field_at(field_index, name="Ammo:", value=random.choice(lists.modifiers), inline=False)
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)

    embed.add_field(name="Map:", value=":grey_question:", inline=False)
    await embed_msg.edit(embed=embed)
    await asyncio.sleep(0.66)
    field_index += 1
    embed.set_field_at(field_index, name="Map:", value=rolled_map, inline=False)
    embed.set_image(url=lists.maps[rolled_map])
    await embed_msg.edit(embed=embed)

    embed.set_footer(text="Would you like to roll an optional bonus modifier?")
    view1 = BonusButton(ctx)
    await embed_msg.edit(embed=embed, view=view1)
    await view1.wait()
    embed.set_footer(text="")
    embed.set_image(url="")
    await embed_msg.edit(embed=embed, view=None)
    if view1.value:
        rolled_bonus = random.choice(random.choice(lists.bonuses))
        embed.add_field(name="\nBonus modifier:", value=":grey_question:", inline=False)
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="\nBonus modifier:", value=rolled_bonus, inline=False)
        await embed_msg.edit(embed=embed)
        if rolled_bonus == "Re-roll anything":

            rolled_weapon = random.choice(tuple(lists.weapons.keys()))
            rolled_armor = random.choice(tuple(lists.armors.keys()))
            rolled_armor_rig = random.choice(tuple(lists.armor_rigs.keys()))
            rolled_rig = random.choice(tuple(lists.rigs.keys()))
            rolled_helmet = random.choice(tuple(lists.helmets.keys()))
            rolled_backpack = random.choice(tuple(lists.backpacks.keys()))
            rolled_map = random.choice(tuple(lists.maps.keys()))

            view2 = RerollAnythingButton()
            embed_msg = await ctx.send(embed=embed, view=view2)
            await view2.wait()
            if view2.value == "Weapon":
                embed.add_field(name="Rerolled weapon:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled weapon:", value=rolled_weapon, inline=False)
                embed.set_image(url=lists.weapons[rolled_weapon])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Armor":
                embed.add_field(name="Rerolled armor:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled armor:", value=rolled_armor, inline=False)
                embed.set_image(url=lists.armors[rolled_armor])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Rig":
                embed.add_field(name="Rerolled rig:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled rig:", value=rolled_rig, inline=False)
                embed.set_image(url=lists.rigs[rolled_rig])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Armored Rig":
                embed.add_field(name="Rerolled armored rig:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled armored rig:", value=rolled_armor_rig, inline=False)
                embed.set_image(url=lists.armor_rigs[rolled_armor_rig])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Helmet":
                embed.add_field(name="Rerolled helmet:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled helmet:", value=rolled_helmet, inline=False)
                embed.set_image(url=lists.helmets[rolled_helmet])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Backpack":
                embed.add_field(name="Rerolled backpack:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled backpack:", value=rolled_backpack, inline=False)
                embed.set_image(url=lists.backpacks[rolled_backpack])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(5)
                embed.set_image(url="")
                await embed_msg.edit(embed=embed)
            if view2.value == "Gun mods":
                embed.add_field(name="Rerolled gun mods:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled gun mods:", value=random.choice(lists.modifiers), inline=False)
                await embed_msg.edit(embed=embed)
            if view2.value == "Ammo":
                embed.add_field(name="Rerolled ammo:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled ammo:", value=random.choice(lists.modifiers), inline=False)
                await embed_msg.edit(embed=embed)
            if view2.value == "Map":
                embed.add_field(name="Rerolled map:", value=":grey_question:", inline=False)
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name="Rerolled map:", value=rolled_map, inline=False)
                embed.set_image(url=lists.maps[rolled_map])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(4)
        await asyncio.sleep(0.66)
        embed.set_footer(text="Enjoy! :)")
        embed.set_image(url="")
        await embed_msg.edit(embed=embed, view=None)


@client.command(name="fastroll", description="Same as classic loadout lottery, but with less waiting around.")
@commands.cooldown(1, 5, commands.BucketType.channel)
async def fastroll(ctx):
    print(f"{datetime.datetime.now()}, t!fastroll - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}")

    rolled_weapon = random.choice(tuple(lists.weapons.keys()))
    rolled_armor = random.choice(tuple(lists.armors.keys()) + tuple(lists.armor_rigs.keys()))
    rolled_rig = random.choice(tuple(lists.rigs.keys()))
    rolled_helmet = random.choice(tuple(lists.helmets.keys()))
    rolled_backpack = random.choice(tuple(lists.backpacks.keys()))
    rolled_map = random.choice(tuple(lists.maps.keys()))

    embed = nextcord.Embed(title="Welcome to Tarkov Loadout Lottery!", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Made by x0rtex", icon_url="https://i.imgur.com/4q2U4QN.png")
    embed.set_thumbnail(url=ctx.message.author.avatar.url)
    embed.add_field(name="Weapon:", value=rolled_weapon, inline=False)
    if rolled_armor in lists.armors:
        embed.add_field(name="Armor:", value=rolled_armor, inline=False)
        embed.add_field(name="Rig:", value=rolled_rig, inline=False)
    else:
        embed.add_field(name="Armored Rig:", value=rolled_armor, inline=False)
    embed.add_field(name="Helmet:", value=rolled_helmet, inline=False)
    embed.add_field(name="Backpack:", value=rolled_backpack, inline=False)
    embed.add_field(name="Gun Mods:", value=random.choice(lists.modifiers), inline=False)
    embed.add_field(name="Ammo:", value=random.choice(lists.modifiers), inline=False)
    embed.add_field(name="Map:", value=rolled_map, inline=False)
    embed.set_footer(text="Would you like to roll an optional bonus modifier?")
    view1 = BonusButton(ctx)
    embed_msg = await ctx.send(embed=embed, view=view1)
    await view1.wait()
    embed.set_footer(text="")
    await embed_msg.edit(embed=embed, view=None)
    if view1.value:
        rolled_bonus = random.choice(random.choice(lists.bonuses))
        embed.add_field(name="\nBonus modifier:", value=rolled_bonus, inline=False)
        if rolled_bonus == "Re-roll anything":
            view2 = RerollAnythingButton()
            embed_msg = await ctx.send(embed=embed, view=view2)
            await view2.wait()
            if view2.value == "Weapon":
                embed.add_field(name="Rerolled weapon:", value=random.choice(tuple(lists.weapons.keys())), inline=False)
            if view2.value == "Armor":
                embed.add_field(name="Rerolled armor:", value=random.choice(tuple(lists.armors.keys())), inline=False)
            if view2.value == "Rig":
                embed.add_field(name="Rerolled rig:", value=random.choice(tuple(lists.rigs.keys())), inline=False)
            if view2.value == "Armored Rig":
                embed.add_field(name="Rerolled armored rig:", value=random.choice(tuple(lists.armor_rigs.keys())), inline=False)
            if view2.value == "Helmet":
                embed.add_field(name="Rerolled helmet:", value=random.choice(tuple(lists.helmets.keys())), inline=False)
            if view2.value == "Backpack":
                embed.add_field(name="Rerolled backpack:", value=random.choice(tuple(lists.backpacks.keys())), inline=False)
            if view2.value == "Gun mods":
                embed.add_field(name="Rerolled gun mods:", value=random.choice(lists.modifiers), inline=False)
            if view2.value == "Ammo":
                embed.add_field(name="Rerolled ammo:", value=random.choice(lists.modifiers), inline=False)
            if view2.value == "Map":
                embed.add_field(name="Rerolled map:", value=random.choice(tuple(lists.maps.keys())), inline=False)
        embed.set_footer(text="Enjoy! :)")
        await embed_msg.edit(embed=embed, view=None)

client.run(bot_token.token)
