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


# Button to exclude FIR-only items from roll
class FIROnly(nextcord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.value = None
        self.ctx = ctx

    async def interaction_check(self, interaction):
        return self.ctx.author == interaction.user

    @nextcord.ui.button(label="Exclude FIR-only items", style=nextcord.ButtonStyle.green)
    async def confirm(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Include FIR-only items", style=nextcord.ButtonStyle.gray)
    async def cancel(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = False
        self.stop()


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

    embed = nextcord.Embed(title="🎲 Welcome to Tarkov Loadout Lottery! 🎲", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Support & LFG Server", icon_url="https://i.imgur.com/ptkBfO2.png", url="https://discord.gg/mgXmtMZgfb")
    embed.set_thumbnail(url=ctx.message.author.avatar.url)
    embed_msg = await ctx.send(embed=embed)

    embed.add_field(name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)",
                    value="p.s. Currently only includes various armors, and tagilla masks.", inline=False)
    view1 = FIROnly(ctx)
    await embed_msg.edit(embed=embed, view=view1)
    await view1.wait()
    embed.remove_field(0)
    await embed_msg.edit(embed=embed, view=None)
    if view1.value == "Exclude FIR-only items":
        del armor_vests[fir_only_armor_vests]
        del armor_rigs[fir_only_armor_rigs]
        del helmets[fir_only_helmets]

    # Dictionary containing all the randomized rolls
    rolls = {
        "Weapon": random.choice(tuple(lists.weapons.keys())),
    }
    rolled_armor = random.choice(tuple(lists.armors.keys()))
    if rolled_armor in lists.armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random.choice(tuple(lists.rigs.keys()))
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random.choice(tuple(lists.helmets.keys())),
        "Backpack": random.choice(tuple(lists.backpacks.keys())),
        "Gun mods": random.choice(tuple(lists.modifiers.keys())),
        "Ammo": random.choice(tuple(lists.modifiers.keys())),
        "Map": random.choice(tuple(lists.maps.keys())),
    })

    field_index = -1
    await asyncio.sleep(0.66)

    # Prints all rolls categories
    for key, value in rolls.items():
        embed.add_field(name=key, value=":grey_question:", inline=False)
        embed.set_image(url="")
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name=key, value=value, inline=False)
        for dict in lists.all.values():
            if value in dict:
                embed.set_image(url=dict[value])
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(1.5)

    # User given the option to roll an optional bonus modifier from list
    embed.set_footer(text="Would you like to roll an optional bonus modifier?")
    view2 = BonusButton(ctx)
    await embed_msg.edit(embed=embed, view=view2)
    await view2.wait()
    embed.set_footer(text="")
    embed.set_image(url="")
    await embed_msg.edit(embed=embed, view=None)
    if view2.value:
        rolled_bonus = random.choice(random.choice(lists.bonuses))
        embed.add_field(name="\nBonus modifier:", value=":grey_question:", inline=False)
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="\nBonus modifier:", value=rolled_bonus, inline=False)
        await embed_msg.edit(embed=embed)

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll anything":
            await asyncio.sleep(1)
            view3 = RerollAnythingButton()
            embed_msg = await ctx.send(embed=embed, view=view3)
            await view3.wait()

            embed.add_field(name=f"Rerolled {view3.value.lower()}:", value=":grey_question:", inline=False)
            rerolled = random.choice(tuple(lists.all[view3.value].keys()))
            await embed_msg.edit(embed=embed, view=None)
            await asyncio.sleep(0.66)
            field_index += 1
            embed.set_field_at(field_index, name=f"Rerolled {view3.value.lower()}:", value=rerolled, inline=False)
            for dict in lists.all.values():
                if rerolled in dict:
                    embed.set_image(url=dict[rerolled])
            await embed_msg.edit(embed=embed)
            await asyncio.sleep(5)
            embed.set_image(url="")
            await embed_msg.edit(embed=embed)
            await asyncio.sleep(3)
        await asyncio.sleep(0.66)
        embed.set_footer(text="Enjoy! :)")
        embed.set_image(url="")
        await embed_msg.edit(embed=embed, view=None)


@client.command(name="fastroll", description="Same as classic loadout lottery, but with less waiting around.")
@commands.cooldown(1, 5, commands.BucketType.channel)
async def fastroll(ctx):
    print(f"{datetime.datetime.now()}, t!fastroll - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}")

    embed = nextcord.Embed(title="🎲 Welcome to Tarkov Loadout Lottery! 🎲", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Support & LFG Server", icon_url="https://i.imgur.com/ptkBfO2.png", url="https://discord.gg/mgXmtMZgfb")
    embed.set_thumbnail(url=ctx.message.author.avatar.url)
    embed_msg = await ctx.send(embed=embed)

    embed.add_field(name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)",
                    value="p.s. Currently only includes various armors, and tagilla masks.", inline=False)
    view1 = FIROnly(ctx)
    await embed_msg.edit(embed=embed, view=view1)
    await view1.wait()
    embed.remove_field(0)
    await embed_msg.edit(embed=embed, view=None)
    if view1.value == "Exclude FIR-only items":
        del armor_vests[fir_only_armor_vests]
        del armor_rigs[fir_only_armor_rigs]
        del helmets[fir_only_helmets]

    # Dictionary containing all the randomized rolls
    rolls = {
        "Weapon": random.choice(tuple(lists.weapons.keys())),
    }
    rolled_armor = random.choice(tuple(lists.armors.keys()))
    if rolled_armor in lists.armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random.choice(tuple(lists.rigs.keys()))
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random.choice(tuple(lists.helmets.keys())),
        "Backpack": random.choice(tuple(lists.backpacks.keys())),
        "Gun mods": random.choice(tuple(lists.modifiers.keys())),
        "Ammo": random.choice(tuple(lists.modifiers.keys())),
        "Map": random.choice(tuple(lists.maps.keys())),
    })

    # Prints all rolls categories
    for key, value in rolls.items():
        embed.add_field(name=key, value=value, inline=False)
    await embed_msg.edit(embed=embed)

    # User given the option to roll an optional bonus modifier from list
    embed.set_footer(text="Would you like to roll an optional bonus modifier?")
    view2 = BonusButton(ctx)
    await embed_msg.edit(embed=embed, view=view2)
    await view2.wait()
    embed.set_footer(text="")
    await embed_msg.edit(embed=embed, view=None)
    if view2.value:
        rolled_bonus = random.choice(random.choice(lists.bonuses))
        embed.add_field(name="\nBonus modifier:", value=rolled_bonus, inline=False)
        await embed_msg.edit(embed=embed)

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll anything":

            view3 = RerollAnythingButton()
            await embed_msg.edit(embed=embed, view=view3)
            await view3.wait()
            rerolled = random.choice(tuple(lists.all[view3.value].keys()))
            embed.add_field(name=f"Rerolled {lists.view3.value.lower()}:", value=rerolled, inline=False)

        embed.set_footer(text="Enjoy! :)")
        await embed_msg.edit(embed=embed, view=None)

client.run(bot_token.token)
