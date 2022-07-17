import asyncio
import bot_token
import datetime
import nextcord
from nextcord.ext import commands
import platform
import psutil
import random
import time
import lists
import copy

client = commands.Bot(command_prefix="t!")
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game("t!help"))
    print("BOT ONLINE\n")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  # Checks if on cooldown
        await ctx.message.add_reaction("⌛")
        await asyncio.sleep(error.retry_after)
        await ctx.message.clear_reaction("⌛")


@client.command(description="Commands List")
async def help(ctx):
    print(f"{datetime.datetime.now()}, t!help - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}\n")
    embed = nextcord.Embed(title="Tarkov Loadout Lottery Help - Commands are case-sensitive", description="Commands List")
    for command in client.walk_commands():
        description = command.description
        embed.add_field(name=f"`t!{command.name}{command.signature if command.signature is not None else ''}`", value=description)
    await ctx.send(embed=embed)


@client.command(description="Pong!")
async def ping(ctx):
    print(f"{datetime.datetime.now()}, t!ping - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}\n")
    start = time.time()
    msg = await ctx.send(f"Pong! DWSP latency: {round(client.latency * 1000)} ms.")
    end = time.time()
    await msg.edit(f"Pong! DWSP latency: {round(client.latency * 1000)} ms. Response time: {round((end - start) * 1000)} ms.")


@client.command(description="Displays the bot's statistics")
async def stats(ctx):
    print(f"{datetime.datetime.now()}, t!stats - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}\n")
    embed = nextcord.Embed(title="Bot Statistics", color=ctx.author.color)
    embed.set_thumbnail(url=ctx.message.author.display_avatar)

    proc = psutil.Process()
    with proc.oneshot():
        uptime = datetime.timedelta(seconds=time.time() - proc.create_time())
        cpu_time = datetime.timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
        mem_total = psutil.virtual_memory().total / (1024 ** 2)
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
class RerollButton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = "None"

    @nextcord.ui.button(label="Weapon", style=nextcord.ButtonStyle.primary)
    async def weapon(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Weapon"
        self.stop()

    @nextcord.ui.button(label="Armor Vest", style=nextcord.ButtonStyle.primary)
    async def armor_vest(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Armor Vest"
        self.stop()

    @nextcord.ui.button(label="Armored Rig", style=nextcord.ButtonStyle.primary)
    async def armored_rig(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Armored Rig"
        self.stop()

    @nextcord.ui.button(label="Rig", style=nextcord.ButtonStyle.primary)
    async def rig(self, _: nextcord.ui.Button, __: nextcord.Interaction):
        self.value = "Rig"
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
    print(f"{datetime.datetime.now()}, t!roll - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}\n")

    # Take all variables from lists.py to save a few hundred lines + fresh lists every command run
    weapons = copy.deepcopy(lists.weapons)
    armor_vests = copy.deepcopy(lists.armor_vests)
    armor_rigs = copy.deepcopy(lists.armor_rigs)
    armors = {**armor_vests, **armor_rigs}
    rigs = copy.deepcopy(lists.rigs)
    helmets = copy.deepcopy(lists.helmets)
    backpacks = copy.deepcopy(lists.backpacks)
    modifiers = copy.deepcopy(lists.modifiers)
    maps = copy.deepcopy(lists.maps)
    good_bonuses = copy.deepcopy(lists.good_bonuses)
    mid_bonuses = copy.deepcopy(lists.mid_bonuses)
    bad_bonuses = copy.deepcopy(lists.bad_bonuses)
    bonuses = good_bonuses, mid_bonuses, bad_bonuses
    fir_only_armor_vests = copy.deepcopy(lists.fir_only_armor_vests)
    fir_only_armor_rigs = copy.deepcopy(lists.fir_only_armor_rigs)
    fir_only_rigs = "LBT-1961A Load Bearing chest rig (Goons Edition)"
    fir_only_helmets = copy.deepcopy(lists.fir_only_helmets)
    fir_only_backpacks = "Mystery Ranch NICE COMM 3 BVS frame system"
    all_rolls = copy.deepcopy(lists.all_rolls)

    embed = nextcord.Embed(title="🎲 Welcome to Tarkov Loadout Lottery! 🎰", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Support & LFG Server", icon_url="https://i.imgur.com/ptkBfO2.png", url="https://discord.gg/mgXmtMZgfb")
    embed.set_thumbnail(url=ctx.message.author.display_avatar)

    embed.add_field(name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)", value="p.s. Currently only includes various armors, and tagilla masks.", inline=False)
    view1 = FIROnly(ctx)
    embed_msg = await ctx.send(embed=embed, view=view1)
    await view1.wait()
    embed.remove_field(0)
    await embed_msg.edit(embed=embed, view=None)
    if view1.value:
        for i in fir_only_armor_vests:
            del armor_vests[i]
        for i in fir_only_armor_rigs:
            del armor_rigs[i]
        for i in fir_only_helmets:
            del helmets[i]
        del rigs[fir_only_rigs]
        del backpacks[fir_only_backpacks]

    # Dictionary containing all the randomized rolls
    rolls = {
        "Weapon": random.choice(tuple(weapons.keys())),
    }
    rolled_armor = random.choice(tuple(armors.keys()))
    if rolled_armor in armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random.choice(tuple(rigs.keys()))
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random.choice(tuple(helmets.keys())),
        "Backpack": random.choice(tuple(backpacks.keys())),
        "Gun mods": random.choice(tuple(modifiers.keys())),
        "Ammo": random.choice(tuple(modifiers.keys())),
        "Map": random.choice(tuple(maps.keys())),
    })

    field_index = -1
    await asyncio.sleep(0.66)

    # Prints all rolls categories
    for category, item in rolls.items():
        embed.add_field(name=f"{category}:", value=":grey_question:", inline=False)
        embed.set_image(url="")
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name=f"{category}:", value=item, inline=False)
        for category_dict in all_rolls.values():
            if item in category_dict:
                embed.set_image(url=category_dict[item])
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
        rolled_bonus = random.choice(tuple(random.choice(bonuses).keys()))
        embed.add_field(name="\nBonus:", value=":grey_question:", inline=False)
        await embed_msg.edit(embed=embed)
        await asyncio.sleep(0.66)
        field_index += 1
        embed.set_field_at(field_index, name="\nBonus:", value=rolled_bonus, inline=False)
        for dictionary in bonuses:
            if rolled_bonus in dictionary:
                embed.set_image(url=dictionary[rolled_bonus])

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll one slot":
            await asyncio.sleep(1)
            view3 = RerollButton()
            await embed_msg.edit(embed=embed, view=view3)
            await view3.wait()
            embed.add_field(name=f"Rerolled {view3.value.lower()}:", value=":grey_question:", inline=False)
            rerolled = random.choice(tuple(all_rolls[view3.value].keys()))
            await embed_msg.edit(embed=embed, view=None)
            await asyncio.sleep(0.66)
            field_index += 1
            embed.set_field_at(field_index, name=f"Rerolled {view3.value.lower()}:", value=rerolled, inline=False)
            for dictionary in all_rolls.values():
                if rerolled in dictionary:
                    embed.set_image(url=dictionary[rerolled])
            await embed_msg.edit(embed=embed)
        else:
            await embed_msg.edit(embed=embed)

        if rolled_bonus == "Re-roll two slots":
            for _ in range(2):
                await asyncio.sleep(1)
                view3 = RerollButton()
                embed.set_image(url="")
                await embed_msg.edit(embed=embed, view=view3)
                await view3.wait()
                embed.add_field(name=f"Rerolled {view3.value.lower()}:", value=":grey_question:", inline=False)
                rerolled = random.choice(tuple(all_rolls[view3.value].keys()))
                await embed_msg.edit(embed=embed, view=None)
                await asyncio.sleep(0.66)
                field_index += 1
                embed.set_field_at(field_index, name=f"Rerolled {view3.value.lower()}:", value=rerolled, inline=False)
                for dictionary in all_rolls.values():
                    if rerolled in dictionary:
                        embed.set_image(url=dictionary[rerolled])
                await embed_msg.edit(embed=embed)
                await asyncio.sleep(2)
            else:
                await embed_msg.edit(embed=embed)

        await asyncio.sleep(3)
        embed.set_image(url="")
        embed.set_footer(text="Enjoy! :)")
        await embed_msg.edit(embed=embed, view=None)


@client.command(name="fastroll", description="Same as classic loadout lottery, but with less waiting around.")
@commands.cooldown(1, 5, commands.BucketType.channel)
async def fastroll(ctx):
    print(f"{datetime.datetime.now()}, t!fastroll - {ctx.message.author.name} - #{ctx.message.channel.name} - {ctx.message.guild.name}\n")

    # Take all variables from lists.py to save a few hundred lines + fresh lists every command run
    weapons = copy.deepcopy(lists.weapons)
    armor_vests = copy.deepcopy(lists.armor_vests)
    armor_rigs = copy.deepcopy(lists.armor_rigs)
    armors = {**armor_vests, **armor_rigs}
    rigs = copy.deepcopy(lists.rigs)
    helmets = copy.deepcopy(lists.helmets)
    backpacks = copy.deepcopy(lists.backpacks)
    modifiers = copy.deepcopy(lists.modifiers)
    maps = copy.deepcopy(lists.maps)
    good_bonuses = copy.deepcopy(lists.good_bonuses)
    mid_bonuses = copy.deepcopy(lists.mid_bonuses)
    bad_bonuses = copy.deepcopy(lists.bad_bonuses)
    bonuses = good_bonuses, mid_bonuses, bad_bonuses
    fir_only_armor_vests = copy.deepcopy(lists.fir_only_armor_vests)
    fir_only_armor_rigs = copy.deepcopy(lists.fir_only_armor_rigs)
    fir_only_rigs = "LBT-1961A Load Bearing chest rig (Goons Edition)"
    fir_only_helmets = copy.deepcopy(lists.fir_only_helmets)
    fir_only_backpacks = "Mystery Ranch NICE COMM 3 BVS frame system"
    all_rolls = copy.deepcopy(lists.all_rolls)

    embed = nextcord.Embed(title="🎲 Welcome to Tarkov Loadout Lottery! 🎰", url="https://github.com/x0rtex/TarkovLoadoutLottery", color=ctx.author.color)
    embed.set_author(name="Support & LFG Server", icon_url="https://i.imgur.com/ptkBfO2.png", url="https://discord.gg/mgXmtMZgfb")
    embed.set_thumbnail(url=ctx.message.author.display_avatar)

    embed.add_field(name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)", value="p.s. Currently only includes various armors, and tagilla masks.", inline=False)
    view1 = FIROnly(ctx)
    embed_msg = await ctx.send(embed=embed, view=view1)
    await view1.wait()
    embed.remove_field(0)
    await embed_msg.edit(embed=embed, view=None)
    if view1.value:
        for i in fir_only_armor_vests:
            del armor_vests[i]
        for i in fir_only_armor_rigs:
            del armor_rigs[i]
        for i in fir_only_helmets:
            del helmets[i]
        del rigs[fir_only_rigs]
        del backpacks[fir_only_backpacks]

    # Dictionary containing all the randomized rolls
    rolls = {
        "Weapon": random.choice(tuple(weapons.keys())),
    }
    rolled_armor = random.choice(tuple(armors.keys()))
    if rolled_armor in armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random.choice(tuple(rigs.keys()))
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random.choice(tuple(helmets.keys())),
        "Backpack": random.choice(tuple(backpacks.keys())),
        "Gun mods": random.choice(tuple(modifiers.keys())),
        "Ammo": random.choice(tuple(modifiers.keys())),
        "Map": random.choice(tuple(maps.keys())),
    })

    # Prints all rolls categories
    for category, item in rolls.items():
        embed.add_field(name=category, value=item, inline=False)
    await embed_msg.edit(embed=embed)

    # User given the option to roll an optional bonus modifier from list
    embed.set_footer(text="Would you like to roll an optional bonus modifier?")
    view2 = BonusButton(ctx)
    await embed_msg.edit(embed=embed, view=view2)
    await view2.wait()
    embed.set_footer(text="")
    await embed_msg.edit(embed=embed, view=None)
    if view2.value:
        rolled_bonus = random.choice(tuple(random.choice(bonuses).keys()))
        embed.add_field(name="\nBonus modifier:", value=rolled_bonus, inline=False)

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll one slot":
            view3 = RerollButton()
            await embed_msg.edit(embed=embed, view=view3)
            await view3.wait()
            rerolled = random.choice(tuple(all_rolls[view3.value].keys()))
            embed.add_field(name=f"Rerolled {view3.value.lower()}:", value=rerolled, inline=False)

        if rolled_bonus == "Re-roll two slots":
            for _ in range(2):
                view3 = RerollButton()
                await embed_msg.edit(embed=embed, view=view3)
                await view3.wait()
                rerolled = random.choice(tuple(all_rolls[view3.value].keys()))
                embed.add_field(name=f"Rerolled {view3.value.lower()}:", value=rerolled, inline=False)

        embed.set_footer(text="Enjoy! :)")
        await embed_msg.edit(embed=embed, view=None)


client.run(bot_token.token)
