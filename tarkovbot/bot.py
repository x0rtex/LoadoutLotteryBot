import hikari
import lightbulb
import miru

from tarkovbot import lists

from typing import Optional
import os
import asyncio
import time
import datetime
import platform
import psutil
import random
import copy


def random_key(category):
    return random.choice(tuple(category.keys()))


class FIROnly(miru.View):
    def __init__(
            self,
            ctx
    ) -> None:
        super().__init__()
        self.ctx = ctx
        self.value = None

    @miru.button(label="Exclude FIR only items", style=hikari.ButtonStyle.SUCCESS)
    async def button_exclude(self, button: miru.Button, ctx: miru.Context) -> None:
        self.value = True
        await ctx.edit_response(components=None)
        self.stop()

    @miru.button(label="Include FIR only items", style=hikari.ButtonStyle.SECONDARY)
    async def button_include(self, button: miru.Button, ctx: miru.Context) -> None:
        self.value = False
        await ctx.edit_response(components=None)
        self.stop()

    async def on_timeout(self) -> None:
        await self.ctx.edit_response(components=None)
        self.stop()

    async def on_error(self, error: Exception, item: Optional[miru.Item] = None,
                       ctx: Optional[miru.Context] = None) -> None:
        if ctx is not None:  # ctx is only passed if the error is raised in an item callback
            await ctx.respond(f"Oh no! This error occurred: {error}")


class Bonus(miru.View):
    def __init__(
            self,
            ctx
    ) -> None:
        super().__init__()
        self.ctx = ctx
        self.value = None

    @miru.button(label="Roll optional bonus modifier", style=hikari.ButtonStyle.SUCCESS)
    async def button_roll_bonus(self, button: miru.Button, ctx: miru.Context) -> None:
        self.value = True
        await ctx.edit_response(components=None)
        self.stop()

    @miru.button(label="Cancel", style=hikari.ButtonStyle.SECONDARY)
    async def button_no_bonus(self, button: miru.Button, ctx: miru.Context) -> None:
        self.value = False
        await ctx.edit_response(components=None)
        self.stop()

    async def on_timeout(self) -> None:
        await self.ctx.edit_response(components=None)
        self.stop()

    async def on_error(self, error: Exception, item: Optional[miru.Item] = None,
                       ctx: Optional[miru.Context] = None) -> None:
        if ctx is not None:  # ctx is only passed if the error is raised in an item callback
            await ctx.respond(f"Oh no! This error occurred: {error}")


class Reroll1(miru.View):
    def __init__(
            self,
            ctx
    ) -> None:
        super().__init__()
        self.ctx = ctx
        self.value = None

    @miru.select(
        placeholder="Choose one option.",
        options=[
            miru.SelectOption(label="Weapon", emoji="🔫"),
            miru.SelectOption(label="Armor Vest", emoji="🦺"),
            miru.SelectOption(label="Armored Rig", emoji="🦺"),
            miru.SelectOption(label="Rig", emoji="🦺"),
            miru.SelectOption(label="Helmet", emoji="🪖"),
            miru.SelectOption(label="Backpack", emoji="👜"),
            miru.SelectOption(label="Gun mods", emoji="⚙️"),
            miru.SelectOption(label="Ammo", emoji="🇦"),
            miru.SelectOption(label="Map", emoji="🗺️"),
        ]
    )
    async def basic_select(self, select: miru.Select, ctx: miru.Context) -> None:
        self.value = select.values
        await ctx.edit_response(components=None)
        self.stop()

    async def on_timeout(self) -> None:
        await self.ctx.edit_response(components=None)
        self.stop()

    async def on_error(self, error: Exception, item: Optional[miru.Item] = None,
                       ctx: Optional[miru.Context] = None) -> None:
        if ctx is not None:
            await ctx.respond(f"Oh no! This error occurred: {error}")


class Reroll2(miru.View):
    def __init__(
            self,
            ctx
    ) -> None:
        super().__init__()
        self.ctx = ctx
        self.value = None

    @miru.select(
        placeholder="Choose two options.",
        min_values=2,
        max_values=2,
        options=[
            miru.SelectOption(label="Weapon", emoji="🔫"),
            miru.SelectOption(label="Armor Vest", emoji="🦺"),
            miru.SelectOption(label="Armored Rig", emoji="🦺"),
            miru.SelectOption(label="Rig", emoji="🦺"),
            miru.SelectOption(label="Helmet", emoji="🪖"),
            miru.SelectOption(label="Backpack", emoji="👜"),
            miru.SelectOption(label="Gun mods", emoji="⚙️"),
            miru.SelectOption(label="Ammo", emoji="🇦"),
            miru.SelectOption(label="Map", emoji="🗺️")
        ]
    )
    async def basic_select(self, select: miru.Select, ctx: miru.Context) -> None:
        self.value = select.values
        await ctx.edit_response(components=None)
        self.stop()

    async def on_timeout(self) -> None:
        await self.ctx.edit_response(components=None)
        self.stop()

    async def on_error(self, error: Exception, item: Optional[miru.Item] = None,
                       ctx: Optional[miru.Context] = None) -> None:
        if ctx is not None:
            await ctx.respond(f"Oh no! This error occurred: {error}")


bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    # default_enabled_guilds=int(os.environ["DEFAULT_GUILD_ID"]),
    help_slash_command=True
)

miru.load(bot)


@bot.command()
@lightbulb.add_cooldown(3.0, 1, lightbulb.GuildBucket)
@lightbulb.command("ping", "Pong!")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_ping(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(f"Pong! {bot.heartbeat_latency * 1000:0.0f}ms")


@bot.command()
@lightbulb.add_cooldown(5.0, 1, lightbulb.GuildBucket)
@lightbulb.command("stats", "Displays the bot's statistics")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_stats(ctx: lightbulb.SlashContext) -> None:
    embed_msg = hikari.Embed(title="Bot Statistics")
    embed_msg.set_thumbnail(ctx.author.avatar_url)

    proc = psutil.Process()
    with proc.oneshot():
        uptime = datetime.timedelta(seconds=time.time() - proc.create_time())
        cpu_time = datetime.timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
        mem_total = psutil.virtual_memory().total / (1024 ** 2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
    fields = [
        ("Python version", platform.python_version(), True),
        ("Hikari-py version", hikari.__version__, True),
        ("Uptime", uptime, True),
        ("CPU time", cpu_time, True),
        ("Memory usage", f"{mem_usage:,.0f} MiB / {mem_total:,.0f} MiB ({mem_of_total:,.0f}%)", True),
        ("Servers", len(bot.cache.get_guilds_view()), True)
    ]
    for name, value, inline in fields:
        embed_msg.add_field(name=name, value=value, inline=inline)
    await ctx.respond(embed=embed_msg)


@bot.command()
@lightbulb.add_cooldown(15.0, 1, lightbulb.GuildBucket)
@lightbulb.command("roll", "Loadout Lottery uses a super mega quantum algorithm to generate a random loadout for you!")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_roll(ctx: lightbulb.SlashContext) -> None:
    view_fironly = FIROnly(300.0)
    view_bonus = Bonus(300.0)
    view_reroll1 = Reroll1(300.0)
    view_reroll2 = Reroll2(300.0)

    question_mark_emoji = ":grey_question:"
    bonus_text = "\nBonus:"

    # Take all variables from lists.py to save a few hundred lines + fresh lists every command run
    weapons = copy.deepcopy(lists.weapons)
    armor_vests = copy.deepcopy(lists.armor_vests)
    armor_rigs = copy.deepcopy(lists.armor_rigs)
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
    fir_only_rigs = copy.deepcopy(lists.fir_only_rigs)
    fir_only_helmets = copy.deepcopy(lists.fir_only_helmets)
    fir_only_backpacks = copy.deepcopy(lists.fir_only_backpacks)
    all_rolls = copy.deepcopy(lists.all_rolls)

    embed_msg = hikari.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery"
    )
    embed_msg.set_author(
        name="Support & LFG Server",
        icon="https://i.imgur.com/ptkBfO2.png",
        url="https://discord.gg/mgXmtMZgfb"
    )
    embed_msg.set_thumbnail(
        ctx.author.avatar_url
    )
    embed_msg.add_field(
        name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)",
        value="This currently includes various armor vests, goons armors/rig/backpack, and tagilla armor/masks.",
        inline=False
    )

    message1 = await ctx.respond(embed_msg, components=view_fironly.build())
    message1 = await message1
    view_fironly.start(message1)
    await view_fironly.wait()
    embed_msg.remove_field(0)

    if view_fironly:
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
        "Weapon": random_key(weapons),
    }
    armors = {**armor_vests, **armor_rigs}
    rolled_armor = random_key(armors)
    if rolled_armor in armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random_key(rigs)
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random_key(helmets),
        "Backpack": random_key(backpacks),
        "Gun mods": random_key(modifiers),
        "Ammo": random_key(modifiers),
        "Map": random_key(maps),
    })

    # Prints all rolls categories
    for category, item in rolls.items():
        embed_msg.add_field(f"{category}:", question_mark_emoji, inline=False)
        embed_msg.set_image(None)
        await ctx.edit_last_response(embed_msg)
        await asyncio.sleep(0.66)
        embed_msg.edit_field(-1, f"{category}:", item, inline=False)
        for category_dict in all_rolls.values():
            if item in category_dict:
                embed_msg.set_image(category_dict[item])
        await ctx.edit_last_response(embed_msg)
        await asyncio.sleep(1.5)

    # User given the option to roll an optional bonus modifier from list
    embed_msg.set_footer(text="Would you like to roll an optional bonus modifier?")
    message2 = await ctx.edit_last_response(embed_msg, components=view_bonus.build())
    view_bonus.start(message2)
    await view_bonus.wait()
    embed_msg.set_footer(text=None)
    embed_msg.set_image(None)
    if view_bonus.value:
        rolled_bonus = random_key(random.choice(bonuses))
        embed_msg.add_field(name=bonus_text, value=question_mark_emoji, inline=False)
        await ctx.edit_last_response(embed_msg)
        await asyncio.sleep(0.66)
        embed_msg.edit_field(-1, bonus_text, rolled_bonus, inline=False)
        for dictionary in bonuses:
            if rolled_bonus in dictionary:
                embed_msg.set_image(dictionary[rolled_bonus])

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll one slot":
            await asyncio.sleep(1)
            embed_msg.set_image(None)
            message3 = await ctx.edit_last_response(embed_msg, components=view_reroll1.build())
            view_reroll1.start(message3)
            await view_reroll1.wait()
            for i in view_reroll1.value:
                embed_msg.add_field(name=f"Rerolled {i.lower()}:", value=question_mark_emoji, inline=False)
                rerolled = random_key(all_rolls[i])
                await ctx.edit_last_response(embed_msg)
                await asyncio.sleep(0.66)
                embed_msg.edit_field(-1, f"Rerolled {i.lower()}:", rerolled, inline=False)
                for dictionary in all_rolls.values():
                    if rerolled in dictionary:
                        embed_msg.set_image(dictionary[rerolled])
                await ctx.edit_last_response(embed_msg)

        elif rolled_bonus == "Re-roll two slots":
            await asyncio.sleep(1)
            embed_msg.set_image(None)
            message4 = await ctx.edit_last_response(embed_msg, components=view_reroll2.build())
            view_reroll2.start(message4)
            await view_reroll2.wait()
            for i in view_reroll2.value:
                embed_msg.add_field(name=f"Rerolled {i.lower()}:", value=question_mark_emoji,
                                    inline=False)
                rerolled = random_key(all_rolls[i])
                embed_msg.set_image(None)
                await ctx.edit_last_response(embed_msg)
                await asyncio.sleep(0.66)
                embed_msg.edit_field(-1, f"Rerolled {i.lower()}:", rerolled, inline=False)
                for dictionary in all_rolls.values():
                    if rerolled in dictionary:
                        embed_msg.set_image(dictionary[rerolled])
                await ctx.edit_last_response(embed_msg)
            await asyncio.sleep(2)
        else:
            await ctx.edit_last_response(embed_msg)

        await asyncio.sleep(3)
        embed_msg.set_image(None)
        embed_msg.set_footer(text="Enjoy! :)")
        await ctx.edit_last_response(embed_msg)


@bot.command()
@lightbulb.add_cooldown(15.0, 1, lightbulb.GuildBucket)
@lightbulb.command("fastroll", "In a rush? This will generate a loadout without any waiting around.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_fastroll(ctx: lightbulb.SlashContext) -> None:
    view_fironly = FIROnly(300)
    view_bonus = Bonus(300)
    view_reroll1 = Reroll1(300)
    view_reroll2 = Reroll2(300)

    bonus_text = "\nBonus:"

    # Take all variables from lists.py to save a few hundred lines + fresh lists every command run
    weapons = copy.deepcopy(lists.weapons)
    armor_vests = copy.deepcopy(lists.armor_vests)
    armor_rigs = copy.deepcopy(lists.armor_rigs)
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
    fir_only_rigs = copy.deepcopy(lists.fir_only_rigs)
    fir_only_helmets = copy.deepcopy(lists.fir_only_helmets)
    fir_only_backpacks = copy.deepcopy(lists.fir_only_backpacks)
    all_rolls = copy.deepcopy(lists.all_rolls)

    embed_msg = hikari.Embed(
        title="🎲 Welcome to Tarkov Loadout Lottery! 🎰",
        url="https://github.com/x0rtex/TarkovLoadoutLottery"
    )
    embed_msg.set_author(
        name="Support & LFG Server",
        icon="https://i.imgur.com/ptkBfO2.png",
        url="https://discord.gg/mgXmtMZgfb"
    )
    embed_msg.set_thumbnail(
        ctx.author.avatar_url
    )
    embed_msg.add_field(
        name="Would you like to include or exclude FIR-only items? (i.e. Unobtainable via purchase or barter from traders or flea)",
        value="This currently includes various armor vests, goons armors/rig/backpack, and tagilla armor/masks.",
        inline=False
    )

    message5 = await ctx.respond(embed_msg, components=view_fironly.build())
    message5 = await message5
    view_fironly.start(message5)
    await view_fironly.wait()
    embed_msg.remove_field(0)

    if view_fironly:
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
        "Weapon": random_key(weapons),
    }
    armors = {**armor_vests, **armor_rigs}
    rolled_armor = random_key(armors)
    if rolled_armor in armor_vests:
        rolls["Armor Vest"] = rolled_armor
        rolls["Rig"] = random_key(rigs)
    else:
        rolls["Armored Rig"] = rolled_armor
    rolls.update({
        "Helmet": random_key(helmets),
        "Backpack": random_key(backpacks),
        "Gun mods": random_key(modifiers),
        "Ammo": random_key(modifiers),
        "Map": random_key(maps),
    })

    # Prints all rolls categories
    for category, item in rolls.items():
        embed_msg.add_field(f"{category}:", item, inline=False)

    # User given the option to roll an optional bonus modifier from list
    embed_msg.set_footer(text="Would you like to roll an optional bonus modifier?")
    message6 = await ctx.edit_last_response(embed_msg, components=view_bonus.build())
    view_bonus.start(message6)
    await view_bonus.wait()
    embed_msg.set_footer(text=None)
    if view_bonus.value:
        rolled_bonus = random_key(random.choice(bonuses))
        embed_msg.add_field(bonus_text, rolled_bonus, inline=False)

        # Re-roll and print a new category of the user's choice
        if rolled_bonus == "Re-roll one slot":
            message7 = await ctx.edit_last_response(embed_msg, components=view_reroll1.build())
            view_reroll1.start(message7)
            await view_reroll1.wait()
            for i in view_reroll1.value:
                rerolled = random_key(all_rolls[i])
                embed_msg.add_field(f"Rerolled {i.lower()}:", rerolled, inline=False)

        elif rolled_bonus == "Re-roll two slots":
            message8 = await ctx.edit_last_response(embed_msg, components=view_reroll2.build())
            view_reroll2.start(message8)
            await view_reroll2.wait()
            for i in view_reroll2.value:
                rerolled = random_key(all_rolls[i])
                embed_msg.add_field(f"Rerolled {i.lower()}:", rerolled, inline=False)

    embed_msg.set_footer(text="Enjoy! :)")
    await ctx.edit_last_response(embed_msg)


def run() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run(
        asyncio_debug=True,  # enable asyncio debug to detect blocking and slow code.
        coroutine_tracking_depth=20,  # enable tracking of coroutines, makes some asyncio errors clearer.
        propagate_interrupts=True,  # Any OS interrupts get rethrown as errors.
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="/help",
            type=hikari.ActivityType.LISTENING
        )
    )
