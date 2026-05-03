# Loadout Lottery Bot

This is a Discord bot for generating a completely random loadout, map, and optional random modifier for Escape from Tarkov.

Its advanced AI\* will ensure the best loadout for any given person, map, and time! You must believe in the system- whether you get a drum mag Makarov with a Slick on labs or a Mk47 with a PACA- and it will reward you. :)

- [Invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=917846908075139083&permissions=414464666688&scope=bot%20applications.commands)
- [Support server](https://discord.gg/mgXmtMZgfb)

## Commands

- **/roll** - Classic Tarkov Loadout Lottery uses a super quantum mega swag algorithm to generate a random loadout and map for you to play with.
- **/fastroll** - Same as classic loadout lottery, but with less waiting around.
- **/settings** - Customise your Loadout Lottery experience. (trader levels, flea market, etc...)
- **/viewsettings** - View your currently saved Loadout Lottery settings.
- **/resetsettings** - Reset your currently saved Loadout Lottery settings to default. (Max traders)
- **/help** - Command list
- **/stats** - Displays the bot's statistics
- **/ping** - Pong!

## Running The Bot

### Download

```sh
git clone https://github.com/x0rtex/LoadoutLotteryBot
cd LoadoutLotteryBot
```

### Installation

```sh
# With uv
uv sync

# With pip
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Configuration

```sh
cp .env.example .env  # Edit .env with your Discord bot token
```

### Running

```sh
# With uv
uv run main.py

# With pip
python main.py
```

## Images

|              Example 1               |               Example 2               |
| :----------------------------------: | :-----------------------------------: |
| ![](https://i.imgur.com/SMAeIKt.png) | ![](https://i.imgur.com/0FAye6t.pngg) |
|              Example 3               |               Example 4               |
| ![](https://i.imgur.com/DgPfPfF.png) | ![](https://i.imgur.com/TXThfe1.png)  |

\* It's random.

```

```
