# Soul Knight Tools

A collection of tools related to the Soul Knight mobile game by ChillyRoom.

## Installation

```sh
git clone https://github.com/TheCheese42/soul-knight-tools
cd soul-knight-tools
python -m venv .venv
source .venv/bin/activate  # Linux
# On Windows:
# .venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt
```

## Usage

### sk_weapons.py

Generate a CSV file of all weapons sorted by category with data from the [Soul Knight Fandom Wiki](https://soul-knight.fandom.com/wiki/Soul_Knight_Wiki). Can also generate a CSV file with links to images of the weapons, hosted on said Wiki.

```sh
python sktools/sk_weapons.py > weapons.csv
python sktools/sk_weapons.py --images > weapon_images.csv
```

### sk_weapon_renderer.py

Generate a Markdown file containing all weapons with their images sorted by categories.

```sh
python sktools/sk_weapons.py > weapons.csv
python sktools/sk_weapons.py --images > weapon_images.csv
python sktools/sk_weapon_renderer.py weapons.csv weapon_images.csv > weapons.md
```

For an example output see `example_sk_weapon_renderer.md`
