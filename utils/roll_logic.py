import asyncio
import random

import discord

from utils import eft, users, views, msgs


def roll_items(user_settings: users.UserSettings) -> (list, bool):
    filtered_items = filter_items(user_settings)

    weapon = random.choice(filtered_items[eft.WEAPON])
    armor = random.choice(filtered_items[eft.ARMOR_VEST] + filtered_items[eft.ARMORED_RIG])
    helmet = random.choice(filtered_items[eft.HELMET])
    backpack = random.choice(filtered_items[eft.BACKPACK])
    gun_mods = random.choice(filtered_items[eft.GUN_MOD])
    ammo = random.choice(filtered_items[eft.AMMO])
    map_ = random.choice(filtered_items[eft.MAP])

    rolls: list = [weapon, armor, helmet, backpack, gun_mods, ammo, map_]

    need_rig: bool = armor.category == eft.ARMOR_VEST
    if need_rig:
        rolled_rig = random.choice(filtered_items[eft.RIG])
        rolls.insert(2, rolled_rig)

    return filtered_items, rolls, need_rig


def filter_items(user_settings: users.UserSettings) -> dict:
    return {
        eft.WEAPON: tuple(item for item in eft.ALL_WEAPONS if check_item(item, user_settings)),
        eft.ARMOR_VEST: tuple(item for item in eft.ALL_ARMOR_VESTS if check_item(item, user_settings)),
        eft.ARMORED_RIG: tuple(item for item in eft.ALL_ARMORED_RIGS if check_item(item, user_settings)),
        eft.HELMET: tuple(item for item in eft.ALL_HELMETS if check_item(item, user_settings)),
        eft.RIG: tuple(item for item in eft.ALL_RIGS if check_item(item, user_settings)),
        eft.BACKPACK: tuple(item for item in eft.ALL_BACKPACKS if check_item(item, user_settings)),
        eft.GUN_MOD: tuple(trader for trader in eft.ALL_GUN_MODS if check_trader_modifier(trader, user_settings)),
        eft.AMMO: tuple(trader for trader in eft.ALL_AMMO if check_trader_modifier(trader, user_settings)),
        eft.MAP: tuple(gamerule for gamerule in eft.ALL_MAPS if check_gamerule(gamerule, user_settings)),
    }


def check_item(item: eft.Item, user_settings: users.UserSettings) -> bool:
    if not item.meta and user_settings["meta_only"]:
        return False

    if item.always_obtainable or (user_settings["flea"] and item.flea):
        return True

    if not user_settings["flea"] and not item.trader_info:
        return user_settings["allow_fir_only"]

    return check_item_traders(item, user_settings)


def check_item_traders(item: eft.Item, user_settings: users.UserSettings) -> bool:
    for trader_name, obtains in item.trader_info.items():
        for obtain in obtains:
            trader_level = user_settings["trader_levels"].get(trader_name)
            if ((trader_level < obtain.level)
                    or (obtain.quest_locked and not user_settings["allow_quest_locked"])
                    or (obtain.barter and not user_settings["flea"])):
                return False
    return True


def roll_random_modifier(user_settings: users.UserSettings) -> eft.GameRule:
    filtered_good_modifiers = eft.GOOD_MODIFIERS  # May need to filter these later
    filtered_ok_modifiers = tuple(ok_mod for ok_mod in eft.OK_MODIFIERS if check_gamerule(ok_mod, user_settings))
    filtered_bad_modifiers = eft.BAD_MODIFIERS  # May need to filter these later

    modifiers = random.choice((filtered_good_modifiers, filtered_ok_modifiers, filtered_bad_modifiers))
    return random.choice(modifiers)


def check_trader_modifier(trader_modifier: eft.GameRule, user_settings: users.UserSettings) -> bool:
    if trader_modifier.name == eft.NO_RESTRICTIONS and not user_settings["flea"]:
        return False

    for level in range(2, 5):
        if trader_modifier.name == getattr(eft, f"LL{level}_TRADERS"):
            return all(trader_level >= level for trader_level in user_settings["trader_levels"].values())

    return True


def check_gamerule(gamerule: eft.GameRule, user_settings: users.UserSettings) -> bool:
    return not (user_settings["meta_only"] and not gamerule.meta
                or gamerule.name == "The Lab" and not user_settings["flea"]
                or gamerule.name == "Ground Zero" and user_settings["flea"]
                or gamerule.name == "Use thermal" and not user_settings["roll_thermals"])


async def reveal_roll(
        ctx: discord.ApplicationContext,
        embed_msg: discord.Embed,
        rolled_item: eft.Item | eft.GameRule,
        prefix: str,
) -> None:
    embed_msg.set_image(url="")
    embed_msg.add_field(name=f"{prefix}{rolled_item.category}:", value=":grey_question:", inline=False)

    if not ctx.response.is_done():
        await ctx.respond(embed=embed_msg)
    else:
        await ctx.edit(embed=embed_msg, view=None)

    await asyncio.sleep(1)
    embed_msg.set_field_at(
        index=-1,
        name=f"{prefix}{rolled_item.category}:",
        value=f"{rolled_item.name}",
        inline=False,
    )

    embed_msg.set_image(url=rolled_item.image_url)
    await ctx.edit(embed=embed_msg, view=None)
    await asyncio.sleep(1.5)


async def is_random_modifier_special(
        rolled_random_modifier: eft.GameRule,
        need_rig: bool,
        ctx: discord.ApplicationContext,
        embed_msg: discord.Embed,
        filtered_items: dict[str, list],
) -> None:
    if rolled_random_modifier.name == views.REROLL_ONE:
        select = views.RerollOneSlotWithRig() if need_rig else views.RerollOneSlotNoRig()
        await reroll(ctx, select, embed_msg, filtered_items)

    elif rolled_random_modifier.name == views.REROLL_TWO:
        select = views.RerollTwoSlotsWithRig() if need_rig else views.RerollTwoSlotsNoRig()
        await reroll(ctx, select, embed_msg, filtered_items)


async def reroll(
        ctx: discord.ApplicationContext,
        select: discord.ui.select,
        embed_msg: discord.Embed,
        filtered_items: dict[str, list],
) -> None:
    await ctx.edit(embed=embed_msg, view=select)
    await select.wait()

    for category in select.value:
        rerolled = random.choice(filtered_items[category])

        if ctx.command.name == "roll":
            await reveal_roll(ctx, embed_msg, rerolled, msgs.REROLLED_PREFIX)
        elif ctx.command.name == "fastroll":
            embed_msg.add_field(
                name=f"{msgs.REROLLED_PREFIX}{rerolled.category}:",
                value=f"{rerolled.name}",
                inline=False,
            )