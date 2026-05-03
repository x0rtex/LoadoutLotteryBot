import asyncio
import random

import discord

from utils import eft, msgs, views
from utils.eft import GameRule, GameRules, Item, Items
from utils.users import UserSettings


def roll_items(user_settings: UserSettings) -> tuple[dict, list, bool]:
    filtered_items: dict = filter_items(user_settings)

    weapon: Item = random.choice(filtered_items[eft.WEAPON])
    armor: Item = random.choice(filtered_items[eft.ARMOR_VEST] + filtered_items[eft.ARMORED_RIG])
    helmet: Item = random.choice(filtered_items[eft.HELMET])
    backpack: Item = random.choice(filtered_items[eft.BACKPACK])
    gun_mods: GameRule = random.choice(filtered_items[eft.GUN_MOD])
    ammo: GameRule = random.choice(filtered_items[eft.AMMO])
    map: GameRule = random.choice(filtered_items[eft.MAP])

    rolls: list[Item | GameRule] = [weapon, armor, helmet, backpack, gun_mods, ammo, map]

    need_rig: bool = armor.category == eft.ARMOR_VEST
    if need_rig:
        rolled_rig = random.choice(filtered_items[eft.RIG])
        rolls.insert(2, rolled_rig)

    return filtered_items, rolls, need_rig


def filter_items(user_settings: UserSettings) -> dict:
    return {
        eft.WEAPON: tuple(item for item in Items.Weapons if check_item(item, user_settings)),
        eft.ARMOR_VEST: tuple(item for item in Items.ArmorVests if check_item(item, user_settings)),
        eft.ARMORED_RIG: tuple(item for item in Items.ArmoredRigs if check_item(item, user_settings)),
        eft.HELMET: tuple(item for item in Items.Helmets if check_item(item, user_settings)),
        eft.RIG: tuple(item for item in Items.Rigs if check_item(item, user_settings)),
        eft.BACKPACK: tuple(item for item in Items.Backpacks if check_item(item, user_settings)),
        eft.GUN_MOD: tuple(trader for trader in GameRules.GunMods if check_trader_modifier(trader, user_settings)),
        eft.AMMO: tuple(trader for trader in GameRules.Ammo if check_trader_modifier(trader, user_settings)),
        eft.MAP: tuple(gamerule for gamerule in GameRules.Maps if check_gamerule(gamerule, user_settings)),
    }


def check_item(item: Item, user_settings: UserSettings) -> bool:
    if not item.meta and user_settings.meta_only:
        return False

    if item.always_obtainable or (user_settings.flea and item.flea):
        return True

    if not user_settings.flea and not item.trader_info:
        return user_settings.allow_fir_only

    return check_item_traders(item, user_settings)


def check_item_traders(item: Item, user_settings: UserSettings) -> bool:
    for trader_name, obtains in item.trader_info.items():
        for obtain in obtains:
            trader_level = user_settings.trader_levels.get_level(trader_name)
            if trader_level is None:
                continue
            if (
                (trader_level >= obtain.level)
                and not (obtain.quest_locked and not user_settings.allow_quest_locked)
                and not (obtain.barter and not user_settings.flea)
            ):
                return True
    return False


def roll_random_modifier(user_settings: UserSettings) -> eft.GameRule:
    filtered_good_modifiers = GameRules.GoodModifiers  # TODO: May need to filter these later
    filtered_ok_modifiers = tuple(ok_mod for ok_mod in GameRules.OkModifiers if check_gamerule(ok_mod, user_settings))
    filtered_bad_modifiers = GameRules.BadModifiers  # TODO: May need to filter these later

    modifiers = random.choice((filtered_good_modifiers, filtered_ok_modifiers, filtered_bad_modifiers))
    return random.choice(modifiers)


def check_trader_modifier(trader_modifier: GameRule, user_settings: UserSettings) -> bool:
    if trader_modifier.name == eft.NO_RESTRICTIONS and not user_settings.flea:
        return False

    for level in range(2, 5):
        if trader_modifier.name == getattr(eft, f"LL{level}_TRADERS"):
            return all(trader_level >= level for trader_level in user_settings.trader_levels.all_levels())

    return True


def check_gamerule(gamerule: GameRule, user_settings: UserSettings) -> bool:
    return not (
        user_settings.meta_only
        and not gamerule.meta
        or gamerule.name == "The Lab"
        and not user_settings.flea
        or gamerule.name == "Ground Zero"
        and user_settings.flea
        or gamerule.name == "Use thermal"
        and not user_settings.roll_thermals
    )


async def reveal_roll(
    ctx: discord.ApplicationContext,
    embed_msg: discord.Embed,
    rolled_item: Item | GameRule,
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
    rolled_random_modifier: GameRule,
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
    view: discord.ui.View,
    embed_msg: discord.Embed,
    filtered_items: dict,
) -> None:
    await ctx.edit(embed=embed_msg, view=view)
    await view.wait()

    for category in view.value:
        rerolled = random.choice(filtered_items[category])

        if ctx.command.name == "roll":
            await reveal_roll(ctx, embed_msg, rerolled, msgs.REROLLED_PREFIX)
        elif ctx.command.name == "fastroll":
            embed_msg.add_field(
                name=f"{msgs.REROLLED_PREFIX}{rerolled.category}:",
                value=f"{rerolled.name}",
                inline=False,
            )
