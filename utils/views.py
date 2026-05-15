from typing import Self

import discord

from utils.eft import Category

# Reroll Slots Random Modifiers
REROLL_ONE: str = "Re-roll 1 slot"
REROLL_TWO: str = "Re-roll 2 slots"
REROLL_ONE_PLACEHOLDER: str = "Select slot to re-roll"
REROLL_TWO_PLACEHOLDER: str = "Select slots to re-roll"
REROLL_OPTIONS_NO_RIG: list[discord.SelectOption] = [
    discord.SelectOption(label=Category.WEAPON.value, emoji="🔫"),
    discord.SelectOption(label=Category.ARMORED_RIG.value, emoji="🛡️"),
    discord.SelectOption(label=Category.HELMET.value, emoji="🪖"),
    discord.SelectOption(label=Category.BACKPACK.value, emoji="🎒"),
    discord.SelectOption(label=Category.GUN_MOD.value, emoji="🔧"),
    discord.SelectOption(label=Category.AMMO.value, emoji="🔍"),
    discord.SelectOption(label=Category.MAP.value, emoji="🗺️"),
]
REROLL_OPTIONS_RIG: list[discord.SelectOption] = [
    discord.SelectOption(label=Category.WEAPON.value, emoji="🔫"),
    discord.SelectOption(label=Category.ARMOR_VEST.value, emoji="🛡️"),
    discord.SelectOption(label=Category.RIG.value, emoji="🦺"),
    discord.SelectOption(label=Category.HELMET.value, emoji="🪖"),
    discord.SelectOption(label=Category.BACKPACK.value, emoji="🎒"),
    discord.SelectOption(label=Category.GUN_MOD.value, emoji="🔧"),
    discord.SelectOption(label=Category.AMMO.value, emoji="🔍"),
    discord.SelectOption(label=Category.MAP.value, emoji="🗺️"),
]


class RandomModifierButton(discord.ui.View):
    def __init__(self: Self) -> None:
        super().__init__(timeout=None)
        self.value: bool = False

    @discord.ui.button(label="Roll Random Modifier", style=discord.ButtonStyle.green, custom_id="persistent_view:roll")
    async def button_callback_yes(self: Self, _, interaction: discord.Interaction) -> None:
        await interaction.response.edit_message(view=None)
        self.value: bool = True
        self.stop()

    @discord.ui.button(label="Finish", style=discord.ButtonStyle.grey, custom_id="persistent_view:no-roll")
    async def button_callback_no(self: Self, _, interaction: discord.Interaction) -> None:
        await interaction.response.edit_message(view=None)
        self.stop()


class RerollOneSlotWithRig(discord.ui.View):
    def __init__(self: Self) -> None:
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id="persistent_view:reroll-one-rig",
        placeholder=REROLL_ONE_PLACEHOLDER,
        min_values=1,
        max_values=1,
        options=REROLL_OPTIONS_RIG,
    )
    async def select_callback(self: Self, select: discord.ui.Select, _) -> None:
        self.value = [select.values[0]]
        self.stop()


class RerollOneSlotNoRig(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id="persistent_view:reroll-one-norig",
        placeholder=REROLL_ONE_PLACEHOLDER,
        min_values=1,
        max_values=1,
        options=REROLL_OPTIONS_NO_RIG,
    )
    async def select_callback(self: Self, select: discord.ui.Select, _) -> None:
        self.value = [select.values[0]]
        self.stop()


class RerollTwoSlotsWithRig(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id="persistent_view:reroll-two-rig",
        placeholder=REROLL_TWO_PLACEHOLDER,
        min_values=2,
        max_values=2,
        options=REROLL_OPTIONS_RIG,
    )
    async def select_callback(self: Self, select: discord.ui.Select, _) -> None:
        self.value = select.values
        self.stop()


class RerollTwoSlotsNoRig(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.select(
        custom_id="persistent_view:reroll-two-norig",
        placeholder=REROLL_TWO_PLACEHOLDER,
        min_values=2,
        max_values=2,
        options=REROLL_OPTIONS_NO_RIG,
    )
    async def select_callback(self: Self, select: discord.ui.Select, _) -> None:
        self.value = select.values
        self.stop()
