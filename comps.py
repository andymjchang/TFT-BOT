"""
Team composition used by the bot
Items are in camel case and a-Z
The "headliner" tag represents a trait from bottom to top.
Set to True if you want it in your team.
Only final comp champion will become headliner and need to set the corresponding 'headliner' tag to True.
e.g. Only want "Sentinel" Ekko, set it to "headliner": [True, False, False]
e.g.2 want either "Sentinel" or "True Damage" Ekko, set it to "headliner": [True, False, True]
"""

COMP = {
    "Diana": {
        "board_position": 24,
        "items": ["SunfireCape", "GargoyleStoneplate", "GargoyleStoneplate"],
        "level": 3,
        "final_comp": True
    },
    "Zyra": {
        "board_position": 1,
        "items": ["SpearofShojin", "NashorsTooth", "SpearofShojin"],
        "level": 2,
        "final_comp": True
    },
    "Janna": {
        "board_position": 2,
        "items": ["GuinsoosRageblade", "StatikkShiv", "RabadonsDeathcap"],
        "level": 2,
        "final_comp": True
    },
    "Neeko": {
        "board_position": 22,
        "items": ["WarmogsArmor", "DragonsClaw", "Crownguard"],
        "level": 2,
        "final_comp": True
    },
    "Riven": {
        "board_position": 26,
        "items": ["ThiefsGloves"],
        "level": 2,
        "final_comp": True
    },
    "Soraka": {
        "board_position": 5,
        "items": ["BlueBuff", "RedBuff"],
        "level": 2,
        "final_comp": True
    },
    "Zoe": {
        "board_position": 4,
        "items": ["HeavenlyEmblem"],
        "level": 2,
        "final_comp": True
    },
    "Wukong": {
        "board_position": 23,
        "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "level": 3,
        "final_comp": True
    },
    "Garen": {
        "board_position": 25,
        "items": ["SunfireCape", "GargoyleStoneplate", "GargoyleStoneplate"],
        "level": 2,
        "final_comp": False
    },
    "Sivir": {
        "board_position": 3,
        "items": ["StatikkShiv"],
        "level": 2,
        "final_comp": False
    },
    "Irelia": {
        "board_position": 0,
        "items": [],
        "level": 3,
        "final_comp": False
    },
    "XayahRakan": {
        "board_position": 25,
        "items": [],
        "level": 3,
        "final_comp": True
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
# The ones on the top will be prioritized for selection.
# For those augments names with suffixes like I, II, III, such as 'Cybernetic Uplink II',
# You only need to add 'Cybernetic Uplink' in the list to cover all three levels.

# Lots of subpar prismatic augments are added to avoid taking an augment that the bot doesn't know how to use,
# or that might confuse the bots positioning logic.
AUGMENTS: list[str] = [
    "Two Healthy",
    "Combat Caster",
    "Enter the Dragon",
    "Heavy Hitters",
    "Featherweights",
    "Pumping Up",
    "Stand United",
    "Drop Blossom!",
    "Inspiring Epitaph",
    "Stimpack",
    "Healing Orbs",
    "Sharing is Caring",
    "Long Shot",
    "Magic Wand",
    "Dragon's Spirit",
    "Harmacist",
    "Shock Treatment",
    "Ascension",
    "Final Ascension",
    "Partial Ascension",
    "Tiny Titans",
    "Tiny, but Deadly",
    "Jeweled Lotus",
    "That's Jazz Baby!",
    "You Have My Bow",
    "Blistering Strikes",
    "Buried Treasures",
    "Switching Gears",
    "Caretaker's Favor",
    "Gotta Go Fast",
    "Tiny Power",
    "Marytr",
    "Shurima's Legacy",
    "Reconnaissance Team",
    "Electrocharge",
    "Quickdraw Soul",
    "InfiniTeam",
    "Big Friend",
    "First Aid Kit",
    "Stand United",
    "Grab Bag",
    "Component Grab Bag",
    "Thrill of the Hunt",
    "Better Together",
    "Cybernetic Uplink",
    "Cybernetic Implants",
    "Celestial Blessing",
    "Raining Gold",
    "Cybernetic Bulk",
    "Unified Resistance",
    "Cybernetic Shell",
    "Weakspot",
    "Tri Force",
    "Gadget Expert",
    "Metabolic Accelerator",
    "Second Wind",
    "Luden's Echo",
    "Last Stand",
    "Ascension",
    "Tiny Titans",
    "Sunfire Board",
    "Wise Spending",
    "Component Grab Bag+",
    "Preparation",
    "Blue Battery",
    "Hustler",
    "Windfall++",
    "Verdant Veil",
    "Rich Get Richer+",
    "Combat Training",
    "Meditation",
    "Axiom Arc",
    "Tiniest Titan",
    "Impenetrable Bulwark", 
    "Unleashed Arcana",
    "Invoker Crown",
    "Dragonlord Crown",
    "Sage Crown",
    "Sage Crest",
    "Dragonlord Crest",
    "Invoker Crest",
    "Shopping Spree",
    "Ba-BOOM!",
    "Tons of Stats!",
    "Epoch",
    "Patient Study",
    "Silver Spoon",
    "Martyr",
    "Balanced Budget",
    "Heroic Grab Bag",
    "Mana Shield",
    "Level Up",
    "New Recruit",
    "Pumping Up",
    "Buried Treasures",
    "Altruist Crown",
    "Altruist Crest",
    "Prismatic Ticket",
    "Hedge Fund",
]

AVOID_AUGMENTS: list[str] = [
    "March of Progress",
    "Stationary Support",
    "Component Buffet",
    "Call to Chaos",
    "Escort Quest",
    "Mind Over Matter",
    "Scapegoat",
    "Wandering Trainer",
    "Recombobulator",
    "Forge",
    "Exiles",
    "Lucky Streak",
    "It's Going to be Epic"
]


def champions_to_buy() -> dict:
    """Creates a list of champions to buy during the game"""
    champs_to_buy: dict = {}
    for champion, champion_data in COMP.items():
        if champion_data["level"] == 1:
            champs_to_buy[champion] = 1
        elif champion_data["level"] == 2:
            champs_to_buy[champion] = 3
        elif champion_data["level"] == 3:
            champs_to_buy[champion] = 10 # Helps when bot makes counting/combine mistakes
        else:
            raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container: list = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
