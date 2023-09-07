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

# Bot logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(help_command=commands.DefaultHelpCommand())


# Bot startup message
@bot.event
async def on_ready() -> None:
    await bot.change_presence(activity=discord.Game('/help'))
    bot.add_view(RandomModifierButton())
    print(f'Logged in as {bot.user}')
    print(f'Guilds: {len(bot.guilds)}')
    print(f'Status: {str(bot.status).capitalize()}')


# Loadout Lottery related constants
REROLLED_PREFIX: str = 'Rerolled '
SUPPORT_SERVER: str = 'Support Server'
DISCORD_SERVER: str = 'https://discord.gg/mgXmtMZgfb'
LOADOUT_LOTTERY_ICON: str = 'https://i.imgur.com/tqtPhBA.png'
GITHUB_URL: str = 'https://github.com/x0rtex/LoadoutLotteryBot'
WELCOME_TEXT: str = '🎲 Welcome to Loadout Lottery! 🎰'
WELCOME_TEXT_META: str = '🎲 Welcome to META Loadout Lottery! 🎰'
REROLL_ONE: str = 'Re-roll 1 slot'
REROLL_TWO: str = 'Re-roll 2 slots'
DEFAULT_SETTINGS: dict = {
    'flea': True,
    'allow_quest_locked': True,
    'allow_fir_only': False,
    'meta_only': False,
    'roll_thermals': False,
    'trader_levels': {
        'Prapor': 4,
        'Therapist': 4,
        'Skier': 4,
        'Peacekeeper': 4,
        'Mechanic': 4,
        'Ragman': 4,
        'Jaeger': 4,
    },
}


class RandomModifierButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value: bool = False

    @discord.ui.button(label='Roll Random Modifier', style=discord.ButtonStyle.green, custom_id='persistent_view:roll')
    async def button_callback_yes(self, _, interaction: discord.Interaction):
        self.value: bool = True
        self.stop()
        await interaction.response.edit_message(view=None)

    @discord.ui.button(label='Finish', style=discord.ButtonStyle.grey, custom_id='persistent_view:no-roll')
    async def button_callback_no(self, _, interaction: discord.Interaction):
        self.stop()
        await interaction.response.edit_message(view=None)


class RerollOneSlotWithRig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id='persistent_view:reroll-one-rig',
        placeholder=REROLL_ONE,
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label=eft.WEAPON, emoji='🔫'),
            discord.SelectOption(label=eft.ARMOR_VEST, emoji='🛡️'),
            discord.SelectOption(label=eft.RIG, emoji='🦺'),
            discord.SelectOption(label=eft.HELMET, emoji='🪖'),
            discord.SelectOption(label=eft.BACKPACK, emoji='🎒'),
            discord.SelectOption(label=eft.GUN_MOD, emoji='🔧'),
            discord.SelectOption(label=eft.AMMO, emoji='🔍'),
            discord.SelectOption(label=eft.MAP, emoji='🗺️'),
        ]
    )
    async def select_callback(self, select, _):
        self.value = [select.values[0]]
        self.stop()


class RerollOneSlotNoRig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id='persistent_view:reroll-one-norig',
        placeholder=REROLL_ONE,
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label=eft.WEAPON, emoji='🔫'),
            discord.SelectOption(label=eft.ARMORED_RIG, emoji='🛡️'),
            discord.SelectOption(label=eft.HELMET, emoji='🪖'),
            discord.SelectOption(label=eft.BACKPACK, emoji='🎒'),
            discord.SelectOption(label=eft.GUN_MOD, emoji='🔧'),
            discord.SelectOption(label=eft.AMMO, emoji='🔍'),
            discord.SelectOption(label=eft.MAP, emoji='🗺️'),
        ]
    )
    async def select_callback(self, select, _):
        self.value = [select.values[0]]
        self.stop()


class RerollTwoSlotsWithRig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id='persistent_view:reroll-two-rig',
        placeholder=REROLL_TWO,
        min_values=2,
        max_values=2,
        options=[
            discord.SelectOption(label=eft.WEAPON, emoji='🔫'),
            discord.SelectOption(label=eft.ARMOR_VEST, emoji='🛡️'),
            discord.SelectOption(label=eft.RIG, emoji='🦺'),
            discord.SelectOption(label=eft.HELMET, emoji='🪖'),
            discord.SelectOption(label=eft.BACKPACK, emoji='🎒'),
            discord.SelectOption(label=eft.GUN_MOD, emoji='🔧'),
            discord.SelectOption(label=eft.AMMO, emoji='🔍'),
            discord.SelectOption(label=eft.MAP, emoji='🗺️'),
        ]
    )
    async def select_callback(self, select, _):
        self.value = select.values
        self.stop()


class RerollTwoSlotsNoRig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id='persistent_view:reroll-two-norig',
        placeholder=REROLL_TWO,
        min_values=2,
        max_values=2,
        options=[
            discord.SelectOption(label=eft.WEAPON, emoji='🔫'),
            discord.SelectOption(label=eft.ARMORED_RIG, emoji='🛡️'),
            discord.SelectOption(label=eft.HELMET, emoji='🪖'),
            discord.SelectOption(label=eft.BACKPACK, emoji='🎒'),
            discord.SelectOption(label=eft.GUN_MOD, emoji='🔧'),
            discord.SelectOption(label=eft.AMMO, emoji='🔍'),
            discord.SelectOption(label=eft.MAP, emoji='🗺️'),
        ]
    )
    async def select_callback(self, select, _):
        self.value = select.values
        self.stop()


def write_user_settings(user_id: int, user_settings: dict) -> None:
    with open(f'userdata/{user_id}.toml', 'wb') as f:
        tomli_w.dump(user_settings, f)


def read_user_settings(user_id: int) -> dict[str, any]:
    try:
        with open(f'userdata/{user_id}.toml', 'rb') as f:
            return tomllib.load(f)
    except FileNotFoundError:
        return DEFAULT_SETTINGS


def show_user_settings(user_settings: dict, ctx) -> discord.Embed:
    embed_msg = discord.Embed()
    embed_msg.set_author(name=SUPPORT_SERVER, icon_url=LOADOUT_LOTTERY_ICON, url=DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.user.avatar.url)

    fields: list = (
            [
                (trader, 'Locked' if level == 0 else f'LL{level}')
                for trader, level in user_settings['trader_levels'].items()
            ] + [
                ('Flea Market', user_settings['flea']),
                ('Allow Quest Locked Items', user_settings['allow_quest_locked']),
                ('Allow FIR-Only Items', user_settings['allow_fir_only']),
                ('Allow thermals', user_settings['roll_thermals']), ('Meta Only', user_settings['meta_only'])
            ]
    )

    for name, value in fields:
        embed_msg.add_field(name=name, value=value)

    return embed_msg


def check_item_traders(item: eft.Item, user_settings: dict) -> bool:
    if item.trader_info == {} and not item.flea:
        if user_settings['allow_fir_only']:
            return True
        else:
            return False

    for trader, trader_info in item.trader_info.items():
        if user_settings['trader_levels'][trader] >= trader_info.level:
            if trader_info.barter and not user_settings['flea']:
                break
            elif trader_info.quest_locked and not user_settings['allow_quest_locked']:
                break
            else:
                return True
    return False


def check_item(item: eft.Item, user_settings: dict) -> bool:
    if not item.meta and user_settings['meta_only']:
        return False

    if item.category == eft.GUN_MOD or item.category == eft.AMMO:
        return True

    if item.category == eft.MAP:
        if item.name == 'The Lab' and not user_settings['flea']:
            return False
        else:
            return True

    if item.unlocked or (item.flea and user_settings['flea']):
        return True

    return check_item_traders(item, user_settings)


def filter_items(user_settings: dict) -> dict[str, list]:

    filtered_items = {}

    for category, items in {
        eft.WEAPON: eft.ALL_WEAPONS,
        eft.ARMOR_VEST: eft.ALL_ARMOR_VESTS,
        eft.ARMORED_RIG: eft.ALL_ARMORED_RIGS,
        eft.RIG: eft.ALL_RIGS,
        eft.HELMET: eft.ALL_HELMETS,
        eft.BACKPACK: eft.ALL_BACKPACKS,
        eft.GUN_MOD: eft.ALL_GUN_MODS,
        eft.AMMO: eft.ALL_AMMO,
        eft.MAP: eft.ALL_MAPS
    }.items():
        filtered_items[category] = [item for item in items if check_item(item, user_settings)]

    return filtered_items


def roll_items(filtered_items: dict[str, list]) -> (list, bool):
    rolls: list = [
        random.choice(filtered_items[eft.WEAPON]),
        random.choice((filtered_items[eft.ARMOR_VEST] + filtered_items[eft.ARMORED_RIG])),
        random.choice(filtered_items[eft.HELMET]),
        random.choice(filtered_items[eft.BACKPACK]),
        random.choice(filtered_items[eft.GUN_MOD]),
        random.choice(filtered_items[eft.AMMO]),
        random.choice(filtered_items[eft.MAP]),
    ]

    need_rig: bool = rolls[1].category == 'Armor Vest'
    if need_rig:
        rolled_rig = random.choice(filtered_items[eft.RIG])
        rolls.insert(2, rolled_rig)

    return rolls, need_rig


def roll_random_modifier(user_settings: dict) -> eft.GameRule:

    filtered_ok_modifiers = [ok_modifier for ok_modifier in eft.OK_MODIFIERS
                             if check_random_modifier(ok_modifier, user_settings)]

    filtered_modifiers = (eft.GOOD_MODIFIERS, filtered_ok_modifiers, eft.BAD_MODIFIERS)

    return random.choice(random.choice(filtered_modifiers))


def check_random_modifier(random_modifier: eft.GameRule, user_settings: dict) -> bool:
    if random_modifier.name == 'Use thermal' and not user_settings['roll_thermals']:
        return False
    return True


async def reveal_roll(ctx, embed_msg: discord.Embed, rolled_item, prefix: str) -> None:
    embed_msg.set_image(url='')
    embed_msg.add_field(name=f'{prefix}{rolled_item.category}:', value=':grey_question:', inline=False)
    await ctx.edit(embed=embed_msg, view=None)
    await asyncio.sleep(1)
    embed_msg.set_field_at(index=-1, name=f'{prefix}{rolled_item.category}:', value=f'{rolled_item.name}', inline=False)
    embed_msg.set_image(url=rolled_item.image_url)
    await ctx.edit(embed=embed_msg, view=None)
    await asyncio.sleep(1.5)


async def is_random_modifier_special(
        rolled_random_modifier: eft.GameRule,
        need_rig: bool,
        ctx,
        embed_msg,
        filtered_items: dict[str, list]
) -> None:
    if rolled_random_modifier.name == REROLL_ONE:
        select = RerollOneSlotWithRig() if need_rig else RerollOneSlotNoRig()
        await reroll(ctx, select, embed_msg, filtered_items)

    elif rolled_random_modifier.name == REROLL_TWO:
        select = RerollTwoSlotsWithRig() if need_rig else RerollTwoSlotsNoRig()
        await reroll(ctx, select, embed_msg, filtered_items)


async def reroll(ctx, select, embed_msg: discord.Embed, filtered_items: dict[str, list]) -> None:
    await ctx.edit(embed=embed_msg, view=select)
    await select.wait()
    rerolled = None

    for category in select.value:
        if category == eft.WEAPON:
            rerolled = random.choice(filtered_items[eft.WEAPON])
        elif category == eft.ARMOR_VEST:
            rerolled = random.choice(filtered_items[eft.ARMOR_VEST])
        elif category == eft.ARMORED_RIG:
            rerolled = random.choice(filtered_items[eft.ARMORED_RIG])
        elif category == eft.RIG:
            rerolled = random.choice(filtered_items[eft.RIG])
        elif category == eft.HELMET:
            rerolled = random.choice(filtered_items[eft.HELMET])
        elif category == eft.BACKPACK:
            rerolled = random.choice(filtered_items[eft.BACKPACK])
        elif category == eft.GUN_MOD:
            rerolled = random.choice(filtered_items[eft.GUN_MOD])
        elif category == eft.AMMO:
            rerolled = random.choice(filtered_items[eft.AMMO])
        elif category == eft.MAP:
            rerolled = random.choice(filtered_items[eft.MAP])

        if ctx.command.name == 'roll':
            await reveal_roll(ctx, embed_msg, rerolled, REROLLED_PREFIX)
        elif ctx.command.name == 'fastroll':
            embed_msg.add_field(name=f'{REROLLED_PREFIX}{rerolled.category}:', value=f'{rerolled.name}', inline=False)


# /roll
@bot.slash_command(name='roll', description='Loadout Lottery!')
@commands.cooldown(1, 20, commands.BucketType.user)
async def roll(ctx: discord.ApplicationContext) -> None:

    user_settings = read_user_settings(ctx.user.id)

    embed_msg = discord.Embed(title=WELCOME_TEXT_META if user_settings["meta_only"] else WELCOME_TEXT, url=GITHUB_URL)
    embed_msg.set_author(name=SUPPORT_SERVER, icon_url=LOADOUT_LOTTERY_ICON, url=DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    # Roll a random selection of items for the user based on their settings
    await ctx.respond(embed=embed_msg)
    filtered_items = filter_items(user_settings)
    rolls, need_rig = roll_items(filtered_items)

    for rolled_item in rolls:
        await reveal_roll(ctx, embed_msg, rolled_item, '')

    # Asks user if they want to roll an optional random modifier
    embed_msg.set_image(url='')
    button = RandomModifierButton()
    await ctx.edit(embed=embed_msg, view=button)
    await button.wait()

    # If they click yes, show their random modifier
    if button.value:
        rolled_random_modifier = roll_random_modifier(user_settings)
        await asyncio.sleep(1)
        await reveal_roll(ctx, embed_msg, rolled_random_modifier, '')

        # Check if random modifier requires further action
        await is_random_modifier_special(rolled_random_modifier, need_rig, ctx, embed_msg, filtered_items)

    # End of the command
    await asyncio.sleep(5)
    embed_msg.set_image(url='')
    embed_msg.set_footer(text='Enjoy!')
    await ctx.edit(embed=embed_msg)


# /fastroll
@bot.slash_command(name='fastroll', description='Loadout Lottery! (Without the waiting around)')
@commands.cooldown(1, 5, commands.BucketType.user)
async def roll(ctx: discord.ApplicationContext) -> None:

    user_settings = read_user_settings(ctx.user.id)

    embed_msg = discord.Embed(title=WELCOME_TEXT_META if user_settings["meta_only"] else WELCOME_TEXT, url=GITHUB_URL)
    embed_msg.set_author(name=SUPPORT_SERVER, icon_url=LOADOUT_LOTTERY_ICON, url=DISCORD_SERVER)
    embed_msg.set_thumbnail(url=ctx.interaction.user.avatar.url)

    # Roll a random selection of items for the user based on their settings
    filtered_items = filter_items(user_settings)
    rolls, need_rig = roll_items(filtered_items)

    for rolled_item in rolls:
        embed_msg.add_field(name=f'{rolled_item.category}:', value=f'{rolled_item.name}', inline=False)

    # Asks user if they want to roll an optional random modifier
    button = RandomModifierButton()
    await ctx.respond(embed=embed_msg, view=button)
    await button.wait()

    if button.value:
        rolled_random_modifier = roll_random_modifier(user_settings)
        embed_msg.add_field(
            name=f'{rolled_random_modifier.category}:',
            value=f'{rolled_random_modifier.name}',
            inline=False
        )
        await asyncio.sleep(1)
        await ctx.edit(embed=embed_msg)

        # Check if random modifier requires further action
        await is_random_modifier_special(rolled_random_modifier, need_rig, ctx, embed_msg, filtered_items)

    # End of the command
    embed_msg.set_footer(text='Enjoy!')
    await ctx.edit(embed=embed_msg, view=None)


# /settings
@bot.slash_command(name='settings', description='Customise your Loadout Lottery experience.')
@commands.cooldown(1, 10, commands.BucketType.user)
@option(name='prapor', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='therapist', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='skier', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='peacekeeper', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='mechanic', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='ragman', description='Enter Prapor\'s trader level', choices=[1, 2, 3, 4])
@option(name='jaeger', description='Enter Prapor\'s trader level', choices=[0, 1, 2, 3, 4])
@option(name='flea', description='Do you have access to the flea market?', choices=[True, False])
@option(name='allow_quest_locked', description='Allow quest locked items to be rolled?', choices=[True, False])
@option(name='allow_fir_only', description='Allow non-trader flea-banned items to be rolled?', choices=[True, False])
@option(name='meta_only', description='Only allow meta items to be rolled?', choices=[True, False])
@option(name='roll_thermals', description='Be able to roll thermal as a random modifier?', choices=[True, False])
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
    user_settings = {
        'trader_levels': {
            eft.PRAPOR: prapor,
            eft.THERAPIST: therapist,
            eft.SKIER: skier,
            eft.PEACEKEEPER: peacekeeper,
            eft.MECHANIC: mechanic,
            eft.RAGMAN: ragman,
            eft.JAEGER: jaeger,
        },
        'flea': flea,
        'allow_quest_locked': allow_quest_locked,
        'allow_fir_only': allow_fir_only,
        'meta_only': meta_only,
        'roll_thermals': roll_thermals,
    }

    # Cannot unlock Prapor, Skier, Mechanic, Ragman, or Jaeger LL2 without unlocking Flea market
    if (user_settings['flea'] is False
            and (user_settings['trader_levels'][eft.PRAPOR] >= 2
                 or user_settings['trader_levels'][eft.SKIER] >= 2
                 or user_settings['trader_levels'][eft.MECHANIC] >= 2
                 or user_settings['trader_levels'][eft.RAGMAN] >= 2
                 or user_settings['trader_levels'][eft.JAEGER] >= 2)):
        user_settings['flea'] = True

    write_user_settings(ctx.user.id, user_settings)

    embed_msg = show_user_settings(user_settings, ctx)
    embed_msg.title = 'Your settings have been updated:'
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /viewsettings
@bot.slash_command(name='viewsettings', description='View your currently saved Loadout Lottery settings.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def viewsettings(ctx: discord.ApplicationContext) -> None:
    try:
        user_settings = read_user_settings(ctx.user.id)
    except FileNotFoundError:
        user_settings = DEFAULT_SETTINGS
    embed_msg = show_user_settings(user_settings, ctx)
    embed_msg.title = 'Your currently saved settings:'
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /resetsettings
@bot.slash_command(name='resetsettings', description='Reset your currently saved Loadout Lottery settings to default.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def resetsettings(ctx: discord.ApplicationContext) -> None:
    write_user_settings(ctx.user.id, DEFAULT_SETTINGS)
    embed_msg = show_user_settings(DEFAULT_SETTINGS, ctx)
    embed_msg.title = 'Your settings have been reset to default:'
    await ctx.respond(embed=embed_msg, ephemeral=True)


# /ping
@bot.slash_command(name='ping', description='Check the bot\'s latency.')
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx: discord.ApplicationContext) -> None:
    await ctx.respond(f':ping_pong: **Ping:** {round(bot.latency * 100, 2)} ms')


# /stats
@bot.slash_command(name='stats', description='Displays the bot\'s statistics')
@commands.cooldown(1, 5, commands.BucketType.user)
async def stats(ctx: discord.ApplicationContext) -> None:
    embed_msg = discord.Embed(title=':robot: Bot Statistics')
    embed_msg.set_thumbnail(url='https://i.imgur.com/vCdkZal.png')
    proc = psutil.Process()
    with proc.oneshot():
        uptime = datetime.timedelta(seconds=time.time() - proc.create_time())
        cpu = proc.cpu_times()
        cpu_time = datetime.timedelta(seconds=cpu.system + cpu.user)
        mem_total = psutil.virtual_memory().total / (1024 ** 2)
        mem_of_total = proc.memory_percent()
        mem_usage = mem_total * (mem_of_total / 100)
    fields = [
        ('Python version', platform.python_version(), True),
        ('Pycord version', discord.__version__, True),
        ('Uptime', uptime, True),
        ('CPU time', cpu_time, True),
        ('Memory usage', f'{mem_usage:,.0f} MiB / {mem_total:,.0f} MiB ({mem_of_total:,.0f}%)', True),
        ('Servers', len(bot.guilds), True)
    ]
    for name, value, inline in fields:
        embed_msg.add_field(name=name, value=value, inline=inline)
    await ctx.respond(embed=embed_msg)


# Application command error handler
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException) -> None:
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(
            f':hourglass: **This command is currently on cooldown.** Try again in {round(error.retry_after, 1)}s.',
            ephemeral=True
        )
    else:
        raise error


def run_bot() -> None:
    if os.name != 'nt':  # Use uvloop if using linux
        import uvloop
        uvloop.install()
    load_dotenv()
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    run_bot()
