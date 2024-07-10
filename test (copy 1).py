import random
import tkinter as tk

# Define a list of enemies with random names, health, strength, defense, and loot for Flufftopia.
enemies = [
    {"name": "Dire Wolf", "health": 50, "strength": 10, "defense": 5, "loot": ["wolf pelt", "fang"]},
    {"name": "Cave Bat", "health": 20, "strength": 5, "defense": 2, "loot": ["bat wing", "guano"]},
    {"name": "Phantom Ghost", "health": 40, "strength": 15, "defense": 5, "loot": ["ectoplasm", "ancient coin"]},
    {"name": "Forest Goblin", "health": 30, "strength": 8, "defense": 3, "loot": ["goblin ear", "rusty sword"]},
    {"name": "Mountain Troll", "health": 70, "strength": 12, "defense": 7, "loot": ["troll hide", "club"]},
    {"name": "Skeletal Warrior", "health": 35, "strength": 10, "defense": 4, "loot": ["bone", "ancient sword"]},
    {"name": "Orc Berserker", "health": 60, "strength": 14, "defense": 6, "loot": ["orc tusk", "battle axe"]},
    {"name": "Fire Dragon", "health": 100, "strength": 20, "defense": 10, "loot": ["dragon scale", "fire gem"]},
    {"name": "Zombie Minion", "health": 45, "strength": 7, "defense": 3, "loot": ["rotten flesh", "zombie heart"]},
    {"name": "Desert Bandit", "health": 40, "strength": 12, "defense": 5, "loot": ["coin pouch", "dagger"]},
    {"name": "Dark Witch", "health": 55, "strength": 13, "defense": 4, "loot": ["witch hat", "magic potion"]},
    {"name": "Giant Spider", "health": 25, "strength": 8, "defense": 3, "loot": ["spider silk", "venom sac"]},
    {"name": "Stone Golem", "health": 80, "strength": 18, "defense": 9, "loot": ["golem core", "rock shard"]},
    {"name": "Hell Demon", "health": 90, "strength": 19, "defense": 8, "loot": ["demon horn", "hellfire"]},
    {"name": "Blood Vampire", "health": 60, "strength": 15, "defense": 6, "loot": ["vampire fang", "blood vial"]},
    {"name": "Hydra", "health": 75, "strength": 17, "defense": 8, "loot": ["hydra scale", "hydra blood"]},
    {"name": "Sand Scorpion", "health": 30, "strength": 10, "defense": 4, "loot": ["scorpion claw", "venom sac"]},
    {"name": "Water Serpent", "health": 50, "strength": 12, "defense": 5, "loot": ["serpent skin", "water gem"]},
    {"name": "Lava Beast", "health": 90, "strength": 20, "defense": 10, "loot": ["lava core", "molten rock"]},
    {"name": "Thunder Eagle", "health": 35, "strength": 15, "defense": 6, "loot": ["eagle feather", "thunder gem"]}
]

# Define a list of NPCs with random names and dialogues for Flufftopia.
npcs = [
    {"name": "Arin the Wise", "dialogue": "Hello traveler!"},
    {"name": "Borok the Merchant", "dialogue": "Would you like to buy something?"},
    {"name": "Cynric the Blacksmith", "dialogue": "I can forge weapons for you."},
    {"name": "Dagna the Healer", "dialogue": "I can heal your wounds."},
    {"name": "Eldrin the Guard", "dialogue": "Stay out of trouble."},
    {"name": "Finn the Farmer", "dialogue": "It's a hard day's work."},
    {"name": "Gilda the Innkeeper", "dialogue": "Need a room for the night?"},
    {"name": "Haldor the Fisherman", "dialogue": "Caught any big ones lately?"},
    {"name": "Ivar the Bard", "dialogue": "Shall I sing you a song?"},
    {"name": "Jorvik the Alchemist", "dialogue": "I have potions for every need."},
    {"name": "Kael the Scholar", "dialogue": "Knowledge is power."},
    {"name": "Lorna the Thief", "dialogue": "Keep an eye on your belongings."},
    {"name": "Mara the Hunter", "dialogue": "The forest is my domain."},
    {"name": "Nissa the Wizard", "dialogue": "Magic is the key to all things."},
    {"name": "Orla the Priest", "dialogue": "May the gods watch over you."}
]

# Define a list of weapons with random names and damage values for Flufftopia.
weapons = [
    {"name": "Flame Sword", "damage": 15},
    {"name": "Ice Axe", "damage": 12},
    {"name": "Storm Bow", "damage": 10},
    {"name": "Shadow Dagger", "damage": 8},
    {"name": "Light Mace", "damage": 14},
    {"name": "Nature Staff", "damage": 9},
    {"name": "Thunder Crossbow", "damage": 11},
    {"name": "Wind Spear", "damage": 13},
    {"name": "Earth Halberd", "damage": 16},
    {"name": "Sun Warhammer", "damage": 18}
]

# Dictionary of events and corresponding locations
events = {
    "village": [
        "You meet a friendly villager named Bob who gives you a health potion.",
        "You visit the marketplace and find interesting items for sale."
    ],
    "enchanted_forest": [
        "You encounter a magical deer named Luna with glowing antlers.",
        "You find a hidden fairy ring surrounded by mushrooms.",
        "You get lost among the towering trees and magical plants."
    ],
    "ancient_ruins": [
        "You encounter a guardian statue named Golem that comes to life.",
        "You find an ancient scroll hidden in the rubble.",
        "You get trapped in a collapsing corridor."
    ],
    "fairy_glade": [
        "You meet a friendly fairy named Tinker who offers you some fairy dust.",
        "You find a hidden treasure chest filled with sparkling gems.",
        "You are surrounded by a group of curious fairies."
    ],
    "forgotten_tomb": [
        "You encounter a skeleton warrior named Skelly guarding a treasure chest.",
        "You find an ancient artifact buried in the tomb.",
        "You trigger a trap and barely escape with your life."
    ],
    "mystic_mountains": [
        "You encounter a mountain troll named Gronk blocking your path.",
        "You find a rare herb with healing properties.",
        "You get caught in a sudden avalanche."
    ],
    "dragon_lair": [
        "You encounter a dragon named Smaug sleeping on a pile of gold.",
        "You find a rare dragon egg hidden in the lair.",
        "You narrowly escape a dragon's fiery breath."
    ],
    "haunted_castle": [
        "You encounter a ghost named Casper haunting the halls.",
        "You find an old diary with secrets of the castle.",
        "You get trapped in a room with moving walls."
    ],
    "hidden_dungeon": [
        "You encounter a dungeon master named Zorg who challenges you.",
        "You find a hidden stash of potions.",
        "You barely escape a room filling with poisonous gas."
    ],
    "serene_lake": [
        "You meet a fisherman named Fin who offers to share his catch.",
        "You find a rare pearl in the lake.",
        "You get caught in a sudden storm while on a boat."
    ],
    "mystic_island": [
        "You encounter a mystical creature named Nessie in the lake.",
        "You find a hidden cave filled with treasures.",
        "You narrowly escape a rising tide."
    ],
    "desert_oasis": [
        "You meet a nomad named Ali who shares his water with you.",
        "You find a hidden spring with crystal clear water.",
        "You get caught in a sudden sandstorm."
    ],
    "hidden_sanctuary": [
        "You encounter a guardian spirit named Anubis protecting the oasis.",
        "You find a hidden chamber filled with ancient artifacts.",
        "You narrowly escape a collapsing tunnel."
    ],
    "frost_caverns": [
        "You encounter an ice golem named Frost blocking your path.",
        "You find a rare crystal with magical properties.",
        "You get caught in a sudden ice slide."
    ],
    "ice_palace": [
        "You meet an ice queen named Elsa who offers you a gift.",
        "You find a hidden chamber filled with ice sculptures.",
        "You narrowly escape a freezing trap."
    ],
    "sunken_temple": [
        "You encounter a sea monster named Kraken guarding the temple.",
        "You find a hidden treasure chest filled with gold.",
        "You narrowly escape a collapsing tunnel."
    ],
    "treasure_vault": [
        "You encounter a guardian spirit named Poseidon protecting the vault.",
        "You find a hidden stash of rare gems.",
        "You narrowly escape a trap filled with water."
    ],
    "verdant_meadow": [
        "You meet a friendly shepherd named Sam who offers you some wool.",
        "You find a hidden grove with rare flowers.",
        "You get caught in a sudden thunderstorm."
    ],
    "underground_grotto": [
        "You encounter a cave troll named Grumpy blocking your path.",
        "You find a hidden chamber filled with glowing crystals.",
        "You narrowly escape a cave-in."
    ],
    "stormy_cliffs": [
        "You encounter a pirate named Jack who offers to share his treasure.",
        "You find a hidden cave filled with pirate loot.",
        "You narrowly escape a falling rock."
    ],
    "pirate_cove": [
        "You encounter a pirate captain named Blackbeard guarding his treasure.",
        "You find a hidden stash of gold coins.",
        "You narrowly escape a pirate ambush."
    ],
    "burning_desert": [
        "You meet a merchant named Omar who offers you a cooling drink.",
        "You find a hidden oasis with clear water.",
        "You get caught in a sudden sandstorm."
    ],
    "secret_oasis": [
        "You encounter a guardian spirit named Ra protecting the oasis.",
        "You find a hidden chamber filled with ancient artifacts.",
        "You narrowly escape a collapsing tunnel."
    ],
    "whispering_woods": [
        "You meet a druid named Rowan who offers you a healing potion.",
        "You find a hidden grove with rare herbs.",
        "You get lost among the whispering trees."
    ],
    "ancient_tree": [
        "You encounter a tree spirit named Yggdrasil who offers you a gift.",
        "You find a hidden chamber filled with ancient scrolls.",
        "You narrowly escape a falling branch."
    ],
    "crystal_caves": [
        "You meet a miner named Rocky who offers you some gems.",
        "You find a hidden chamber filled with rare crystals.",
        "You get caught in a sudden cave-in."
    ],
    "crystal_chamber": [
        "You encounter a guardian spirit named Crystal protecting the chamber.",
        "You find a hidden stash of rare gems.",
        "You narrowly escape a trap filled with crystals."
    ],
    "emerald_grove": [
        "You meet a ranger named Robin who offers you some herbs.",
        "You find a hidden spring with healing waters.",
        "You get caught in a sudden thunderstorm."
    ],
    "healing_spring": [
        "You encounter a guardian spirit named Gaia protecting the spring.",
        "You find a hidden chamber filled with rare herbs.",
        "You narrowly escape a collapsing tunnel."
    ],
    "dragon_peak": [
        "You encounter a dragon named Draco guarding his nest.",
        "You find a rare dragon egg hidden in the nest.",
        "You narrowly escape a dragon's fiery breath."
    ],
    "dragon_nest": [
        "You meet a dragon rider named Aragon who offers you a ride.",
        "You find a hidden stash of dragon scales.",
        "You narrowly escape a dragon's fiery breath."
    ]
}

# Define locations with descriptions and secrets
locations = {
    "village": {
        "description": "A quaint village with friendly inhabitants and a bustling marketplace."
    },
    "enchanted_forest": {
        "description": "An enchanted forest filled with glowing plants and mystical creatures. The air is thick with magic.",
        "secret": "You notice a faint trail of sparkling dust leading deeper into the forest.",
        "secret_location": "fairy_glade"
    },
    "ancient_ruins": {
        "description": "Ruins of an ancient civilization. Crumbling structures and broken statues are all that remain.",
        "secret": "You find a hidden staircase beneath a collapsed archway.",
        "secret_location": "forgotten_tomb"
    },
    "mystic_mountains": {
        "description": "Tall mountains shrouded in mist. The peaks are said to hold great treasures and dangers.",
        "secret": "A narrow path leads to a cave entrance hidden by mist.",
        "secret_location": "dragon_lair"
    },
    "haunted_castle": {
        "description": "An old castle rumored to be haunted. Shadows move on their own and eerie sounds echo through the halls.",
        "secret": "You discover a secret passage behind a tattered tapestry.",
        "secret_location": "hidden_dungeon"
    },
    "serene_lake": {
        "description": "A peaceful lake surrounded by lush greenery. The water is crystal clear and teeming with fish.",
        "secret": "You see a small island in the middle of the lake with something glinting in the sunlight.",
        "secret_location": "mystic_island"
    },
    "desert_oasis": {
        "description": "A refreshing oasis in the middle of a vast desert. Palm trees and clear water provide a welcome respite.",
        "secret": "You notice a hidden cave behind a waterfall.",
        "secret_location": "hidden_sanctuary"
    },
    "frost_caverns": {
        "description": "Caverns filled with ice and snow. The air is freezing and the ground is slippery.",
        "secret": "A small crack in the ice leads to a hidden chamber.",
        "secret_location": "ice_palace"
    },
    "sunken_temple": {
        "description": "An ancient temple partially submerged in water. Fish swim through the halls and the walls are covered in algae.",
        "secret": "A loose stone reveals a hidden passage.",
        "secret_location": "treasure_vault"
    },
    "verdant_meadow": {
        "description": "A lush meadow filled with wildflowers and tall grass. Butterflies and bees flit about.",
        "secret": "A patch of unusually tall grass hides a trapdoor.",
        "secret_location": "underground_grotto"
    },
    "stormy_cliffs": {
        "description": "High cliffs overlooking a stormy sea. The wind howls and waves crash against the rocks.",
        "secret": "A narrow ledge leads to a cave entrance.",
        "secret_location": "pirate_cove"
    },
    "burning_desert": {
        "description": "A scorching desert with endless dunes and intense heat. Mirages play tricks on your eyes.",
        "secret": "You find an ancient well that leads to an underground chamber.",
        "secret_location": "secret_oasis"
    },
    "whispering_woods": {
        "description": "A forest where the trees seem to whisper secrets to those who listen.",
        "secret": "You find a hidden grove with a mysterious tree.",
        "secret_location": "ancient_tree"
    },
    "crystal_caves": {
        "description": "Caves filled with glowing crystals that illuminate the dark passages.",
        "secret": "A hidden tunnel leads to a cavern filled with rare crystals.",
        "secret_location": "crystal_chamber"
    },
    "emerald_grove": {
        "description": "A lush grove with emerald-green foliage and vibrant wildlife.",
        "secret": "A hidden spring with healing waters lies deep within the grove.",
        "secret_location": "healing_spring"
    },
    "dragon_peak": {
        "description": "A towering mountain peak said to be home to dragons.",
        "secret": "A narrow path leads to a hidden dragon's nest.",
        "secret_location": "dragon_nest"
    }
}

def game_intro():
    """Displays the game introduction for Flufftopia."""
    print("Welcome to Flufftopia!")
    print("In a land of mystery and magic, you will embark on a journey like no other.")
    print("Explore ancient ruins, enchanted forests, and hidden villages.")
    print("Uncover secrets long forgotten and treasures untold.")
    print("Your goal is to survive, grow stronger, and uncover the ultimate treasure.")
    print("Good luck, brave adventurer!\n")

def player_setup():
    """Sets up the player character with initial attributes for Flufftopia."""
    print("Creating your character...")
    player = {
        "name": input("Enter your character's name: "),
        "health": 100,
        "strength": random.randint(10, 20),
        "defense": random.randint(5, 15),
        "agility": random.randint(5, 15),
        "inventory": [],
        "quests": []
    }
    print(f"\nWelcome, {player['name']}! Your adventure begins now.")
    print(f"Stats: Health = {player['health']}, Strength = {player['strength']}, Defense = {player['defense']}, Agility = {player['agility']}")
    print("\nThe journey ahead is perilous, but you feel ready to face any challenge.\n")
    return player

def use_skill(player, skill, target):
    """Applies a skill used by the player on the target in Flufftopia."""
    if skill == "fireball":
        damage = player["strength"] * 2 - target["defense"]
        target["health"] -= max(0, damage)
        print(f"You cast a fireball at {target['name']} for {damage} damage!")
    elif skill == "heal":
        heal_amount = player["strength"] * 2
        player["health"] = min(100, player["health"] + heal_amount)
        print(f"You heal yourself for {heal_amount} health points!")
    # Add more skills as needed

def start_quest(player, quest_name):
    """Starts a new quest for the player in Flufftopia."""
    print(f"You have started the quest: {quest_name}")
    player["quests"].append(quest_name)
    if quest_name == "Find the Ancient Artifact":
        print("You need to explore the ancient ruins to find the artifact.")
    elif quest_name == "Defeat the Dragon":
        print("You must find and defeat the dragon on Dragon Peak.")
    # Add more quests as needed

def combat(player, enemy):
    """Handles combat between the player and an enemy."""
    print(f"A wild {enemy['name']} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n{player['name']}'s Health: {player['health']}")
        print(f"{enemy['name']}'s Health: {enemy['health']}")
        action = input("Do you want to [A]ttack, [R]un, or use a [S]kill? > ").lower()
        
        if action == 'a':
            player_attack(player, enemy)
            if enemy["health"] > 0:
                enemy_attack(player, enemy)
        elif action == 'r':
            if random.choice([True, False]):
                print(f"You managed to escape from the {enemy['name']}!")
                return
            else:
                print(f"You failed to escape. The {enemy['name']} attacks!")
                enemy_attack(player, enemy)
        elif action == 's':
            skill = input("Choose a skill (fireball/heal): ").lower()
            use_skill(player, skill, enemy)
            if enemy["health"] > 0:
                enemy_attack(player, enemy)
        else:
            print("Invalid action. Try again.")
        
    if player["health"] <= 0:
        print("You have been defeated. Game over.")
    elif enemy["health"] <= 0:
        print(f"You have defeated the {enemy['name']}!")
        loot = random.choice(enemy["loot"])
        player["inventory"].append(loot)
        print(f"You found a {loot} on the {enemy['name']}!")

def player_attack(player, enemy):
    """Calculates and applies damage dealt by the player to the enemy."""
    damage = max(0, player["strength"] - enemy["defense"] + random.randint(-5, 5))
    enemy["health"] -= damage
    print(f"You attack the {enemy['name']} for {damage} damage!")

def enemy_attack(player, enemy):
    """Calculates and applies damage dealt by the enemy to the player."""
    damage = max(0, enemy["strength"] - player["defense"] + random.randint(-5, 5))
    player["health"] -= damage
    print(f"The {enemy['name']} attacks you for {damage} damage!")

def random_event(location, player):
    """Triggers a random event based on the current location."""
    if location in events:
        event = random.choice(events[location])
        print(event)
        if "guardian" in event or "encounter" in event:
            combat(player, random.choice(enemies))
        elif "trap" in event or "escape" in event:
            player["health"] -= 10
            print(f"You lose 10 health. Current health: {player['health']}")
        elif "potion" in event or "healing" in event:
            player["health"] += 10
            print(f"You gain 10 health. Current health: {player['health']}")

def describe_location(location, locations):
    """Displays the description of the current location."""
    print(f"You are at the {location.replace('_', ' ').title()}.")
    print(locations[location]["description"])

def discover_secret_path(location, locations):
    """Checks for and handles the discovery of secret paths in the current location."""
    if "secret" in locations[location]:
        print(locations[location]["secret"])
        choice = input("Do you want to explore the secret path? (y/no) > ")
        if choice.lower() == "y":
            return locations[location]["secret_location"]
    return location

def game_loop(player, locations):
    """Main game loop handling player actions and events."""
    current_location = "village"
    while True:
        print("\nWhat do you want to do?")
        for idx, loc in enumerate(locations.keys(), start=1):
            print(f"{idx}. Explore the {loc.replace('_', ' ').title()}")
        print(f"{len(locations) + 1}. Check inventory")
        print(f"{len(locations) + 2}. Quit")

        choice = input("> ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(locations):
                current_location = list(locations.keys())[choice - 1]
            elif choice == len(locations) + 1:
                print(f"Inventory: {player['inventory']}")
                print(f"Health: {player['health']}")
                continue
            elif choice == len(locations) + 2:
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Try again.")
                continue
        else:
            print("Invalid choice. Try again.")
            continue

        describe_location(current_location, locations)
        current_location = discover_secret_path(current_location, locations)
        random_event(current_location, player)

        if player["health"] <= 0:
            print("You have died. Game over.")
            break

# Start the game
if __name__ == "__main__":
    game_intro()
    player = player_setup()
    game_loop(player, locations)
