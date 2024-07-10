# main.py

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

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

# Dictionary of events and corresponding locations
events = {
    "village": [
        "You meet a friendly villager named Mordaci who gives you a health potion.",
        "You visit the marketplace and find interesting items for sale."
    ],
    "enchanted_forest": [
        "You encounter a magical deer named Thomas with glowing antlers.",
        "You find a hidden fairy ring surrounded by mushrooms.",
        "You get lost among the towering trees and magical plants."
    ],
    "ancient_ruins": [
        "You encounter a guardian statue named Golem that comes to life.",
        "You find an ancient scroll hidden in the rubble.",
        "You get trapped in a collapsing corridor."
    ],
    "fairy_glade": [
        "You meet a friendly fairy named Steve who offers you some fairy dust.",
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
        "You encounter a dragon sleeping on a pile of gold.",
        "You find a rare dragon egg hidden in the lair.",
        "You narrowly escape a dragon's fiery breath."
    ],
    "haunted_castle": [
        "You encounter a ghost haunting the halls.",
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
        "You meet an ice queen who offers you a gift.",
        "You find a hidden chamber filled with ice sculptures.",
        "You narrowly escape a freezing trap."
    ],
    "sunken_temple": [
        "You encounter a sea monster guarding the temple.",
        "You find a hidden treasure chest filled with gold.",
        "You narrowly escape a collapsing tunnel."
    ],
    "treasure_vault": [
        "You encounter a guardian spirit protecting the vault.",
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
        "You encounter a pirate named Jook who offers to share his treasure.",
        "You find a hidden cave filled with pirate loot.",
        "You narrowly escape a falling rock."
    ],
    "pirate_cove": [
        "You encounter a pirate captain named Blackballs guarding his treasure.",
        "You find a hidden stash of gold coins.",
        "You narrowly escape a pirate ambush."
    ],
    "burning_desert": [
        "You meet a merchant named Omar who offers you a cooling drink.",
        "You find a hidden oasis with clear water.",
        "You get caught in a sudden sandstorm."
    ],
    "secret_oasis": [
        "You encounter a guardian spirit named Riva protecting the oasis.",
        "You find a hidden chamber filled with ancient artifacts.",
        "You narrowly escape a collapsing tunnel."
    ],
    "whispering_woods": [
        "You meet a druid named Rowan who offers you a healing potion.",
        "You find a hidden grove with rare herbs.",
        "You get lost among the whispering trees."
    ],
    "ancient_tree": [
        "You encounter a tree spirit named Yiggy who offers you a gift.",
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
        "You encounter a guardian spirit protecting the spring.",
        "You find a hidden chamber filled with rare herbs.",
        "You narrowly escape a collapsing tunnel."
    ],
    "dragon_peak": [
        "You encounter a dragon named Draco guarding his nest.",
        "You find a rare dragon egg hidden in the nest.",
        "You narrowly escape a dragon's fiery breath."
    ],
    "dragon_nest": [
        "You meet a dragon rider who offers you a ride.",
        "You find a hidden stash of dragon scales.",
        "You narrowly escape a dragon's fiery breath."
    ]
}

# Define the descriptions for each location
locations = {
    "village": {
        "description": "A quaint village with friendly inhabitants and a bustling marketplace."
    },
    "enchanted_forest": {
        "description": "A mystical forest filled with magical creatures and ancient secrets."
    },
    "ancient_ruins": {
        "description": "Ruins of an ancient civilization, filled with hidden treasures and dangers."
    },
    "fairy_glade": {
        "description": "A beautiful glade where fairies live, filled with sparkling lights and flowers."
    },
    "forgotten_tomb": {
        "description": "A dark and eerie tomb filled with ancient traps and treasures."
    },
    "mystic_mountains": {
        "description": "A range of tall mountains with treacherous paths and rare herbs."
    },
    "dragon_lair": {
        "description": "A lair where dragons dwell, filled with gold and rare treasures."
    },
    "haunted_castle": {
        "description": "A spooky castle haunted by ghosts and filled with dark secrets."
    },
    "hidden_dungeon": {
        "description": "A hidden dungeon filled with traps, treasures, and a dungeon master."
    },
    "serene_lake": {
        "description": "A peaceful lake with clear water and abundant fish."
    },
    "mystic_island": {
        "description": "An island with mystical creatures and hidden treasures."
    },
    "desert_oasis": {
        "description": "A hidden oasis in the desert, with fresh water and shade."
    },
    "hidden_sanctuary": {
        "description": "A hidden sanctuary protected by a guardian spirit."
    },
    "frost_caverns": {
        "description": "Ice caverns with rare crystals and icy paths."
    },
    "ice_palace": {
        "description": "A palace made of ice, home to an ice queen and her secrets."
    },
    "sunken_temple": {
        "description": "A temple that has sunk into the sea, guarded by sea monsters."
    },
    "treasure_vault": {
        "description": "A vault filled with rare gems and guarded by a spirit."
    },
    "verdant_meadow": {
        "description": "A meadow with rare flowers and a friendly shepherd."
    },
    "underground_grotto": {
        "description": "An underground grotto with glowing crystals and hidden paths."
    },
    "stormy_cliffs": {
        "description": "Cliffs battered by storms, home to pirates and hidden loot."
    },
    "pirate_cove": {
        "description": "A cove where pirates hide their treasures and ambush strangers."
    },
    "burning_desert": {
        "description": "A scorching desert with hidden oases and merchant caravans."
    },
    "secret_oasis": {
        "description": "A secret oasis protected by a guardian spirit."
    },
    "whispering_woods": {
        "description": "Woods where trees whisper secrets and rare herbs grow."
    },
    "ancient_tree": {
        "description": "An ancient tree with a spirit that guards hidden chambers."
    },
    "crystal_caves": {
        "description": "Caves filled with rare crystals and hidden chambers."
    },
    "crystal_chamber": {
        "description": "A chamber filled with crystals and guarded by a spirit."
    },
    "emerald_grove": {
        "description": "A grove with healing waters and a friendly ranger."
    },
    "healing_spring": {
        "description": "A spring with healing properties, guarded by a spirit."
    },
    "dragon_peak": {
        "description": "A peak where dragons nest, guarded by a fierce dragon."
    },
    "dragon_nest": {
        "description": "A nest of dragons with hidden treasures and dangers."
    }
}

class FlufftopiaApp(App):
    def build(self):
        self.player = self.player_setup()
        self.location_index = 0
        self.current_enemy = None

        main_layout = BoxLayout(orientation='vertical')

        self.health_bar = ProgressBar(max=100, value=self.player['health'])
        main_layout.add_widget(self.health_bar)

        self.info_label = Label(text="Welcome to Flufftopia!", size_hint_y=None, height=400)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
        self.scroll_view.add_widget(self.info_label)
        main_layout.add_widget(self.scroll_view)

        self.inventory_label = Label(text="Inventory: " + ', '.join(self.player['inventory']))
        main_layout.add_widget(self.inventory_label)

        button_layout = GridLayout(cols=5, size_hint_y=None, height=50)
        main_layout.add_widget(button_layout)

        self.next_button = Button(text="Next")
        self.next_button.bind(on_press=self.next_location)
        button_layout.add_widget(self.next_button)

        self.skill_button = Button(text="Use Skill")
        self.skill_button.bind(on_press=self.show_skill_popup)
        button_layout.add_widget(self.skill_button)

        self.attack_button = Button(text="Attack")
        self.attack_button.bind(on_press=self.attack_enemy)
        button_layout.add_widget(self.attack_button)

        self.defend_button = Button(text="Defend")
        self.defend_button.bind(on_press=self.defend)
        button_layout.add_widget(self.defend_button)

        self.run_button = Button(text="Run")
        self.run_button.bind(on_press=self.run_from_combat)
        button_layout.add_widget(self.run_button)

        self.enable_combat_buttons(False)  # Disable combat buttons initially

        return main_layout

    def game_intro(self):
        intro_text = (
            "Welcome to Flufftopia!\n"
            "In a land of mystery and magic, you will embark on a journey like no other.\n"
            "Explore ancient ruins, enchanted forests, and hidden villages.\n"
            "Uncover secrets long forgotten and treasures untold.\n"
            "Your goal is to survive, grow stronger, and uncover the ultimate treasure.\n"
            "Good luck, brave adventurer!\n"
        )
        self.info_label.text = intro_text

    def player_setup(self):
        player = {
            "name": "Hero",
            "health": 100,
            "strength": random.randint(10, 20),
            "defense": random.randint(5, 15),
            "agility": random.randint(5, 15),
            "inventory": ["health potion"],
            "quests": []
        }
        return player

    def clear_screen(self):
        self.info_label.text = ""

    def describe_location(self, location):
        self.info_label.text += f"\nYou are at the {location.replace('_', ' ').title()}.\n{locations[location]['description']}"

    def random_event(self, location):
        self.clear_screen()
        if location in events:
            event = random.choice(events[location])
            self.info_label.text += f"\n{event}"
            if "guardian" in event or "encounter" in event:
                self.current_enemy = random.choice(enemies)
                self.info_label.text += f"\nA wild {self.current_enemy['name']} appears!"
                self.enable_combat_buttons(True)
            elif "trap" in event or "escape" in event:
                self.player["health"] -= 10
                self.health_bar.value = self.player["health"]
                self.info_label.text += f"\nYou lose 10 health. Current health: {self.player['health']}"
            elif "potion" in event or "healing" in event:
                self.player["health"] = min(100, self.player["health"] + 10)
                self.health_bar.value = self.player["health"]
                self.info_label.text += f"\nYou gain 10 health. Current health: {self.player['health']}"
        self.check_player_health()

    def combat(self, enemy):
        self.clear_screen()
        self.info_label.text += f"\n{self.player['name']}'s Health: {self.player['health']}"
        self.info_label.text += f"\n{enemy['name']}'s Health: {enemy['health']}"

        damage = max(0, self.player["strength"] - enemy["defense"] + random.randint(-5, 5))
        enemy["health"] -= damage
        self.info_label.text += f"\nYou attack the {enemy['name']} for {damage} damage!"

        if enemy["health"] <= 0:
            self.info_label.text += f"\nYou have defeated the {enemy['name']}!"
            loot = random.choice(enemy["loot"])
            self.player["inventory"].append(loot)
            self.inventory_label.text = "Inventory: " + ', '.join(self.player["inventory"])
            self.info_label.text += f"\nYou found a {loot} on the {enemy['name']}!"
            self.enable_combat_buttons(False)
            self.proceed_if_enemy_defeated()
            return

        damage = max(0, enemy["strength"] - self.player["defense"] + random.randint(-5, 5))
        self.player["health"] -= damage
        self.health_bar.value = self.player["health"]
        self.info_label.text += f"\nThe {enemy['name']} attacks you for {damage} damage!"

        self.check_player_health()

    def defend(self, instance):
        self.clear_screen()
        self.info_label.text += f"\n{self.player['name']} is defending!"
        self.player["defense"] *= 2
        self.enemy_attack(self.current_enemy)

    def enemy_attack(self, enemy):
        damage = max(0, enemy["strength"] - self.player["defense"] + random.randint(-5, 5))
        self.player["health"] -= damage
        self.health_bar.value = self.player["health"]
        self.info_label.text += f"\nThe {enemy['name']} attacks you for {damage} damage!"
        self.player["defense"] = int(self.player["defense"] / 2)
        self.check_player_health()

    def check_player_health(self):
        if self.player["health"] <= 0:
            self.info_label.text += "\nYou have been defeated. Game over."
            self.next_button.disabled = True
            self.enable_combat_buttons(False)

    def proceed_if_enemy_defeated(self):
        if self.current_enemy and self.current_enemy["health"] <= 0:
            self.current_enemy = None
            self.next_location(None)

    def next_location(self, instance):
        if self.player["health"] <= 0:
            return

        if self.current_enemy:
            self.info_label.text += f"\nYou must defeat the {self.current_enemy['name']} to proceed!"
            return

        if self.location_index < len(locations):
            location = list(locations.keys())[self.location_index]
            self.describe_location(location)
            self.random_event(location)
            self.location_index += 1
        else:
            self.info_label.text += "\nCongratulations! You have completed the journey through Flufftopia!"
            self.next_button.disabled = True

    def use_skill(self, skill, target, popup):
        self.clear_screen()
        if skill == "fireball" or skill == "f":
            damage = self.player["strength"] * 2 - target["defense"]
            target["health"] -= max(0, damage)
            self.info_label.text += f"\nYou cast a fireball at {target['name']} for {damage} damage!"
        elif skill == "heal" or skill == "h":
            heal_amount = self.player["strength"] * 2
            self.player["health"] = min(100, self.player["health"] + heal_amount)
            self.health_bar.value = self.player["health"]
            self.info_label.text += f"\nYou heal yourself for {heal_amount} health points!"
        popup.dismiss()
        self.check_player_health()
        self.proceed_if_enemy_defeated()

    def show_skill_popup(self, instance):
        layout = BoxLayout(orientation='vertical')
        fireball_button = Button(text="Fireball", size_hint=(1, 0.5))
        heal_button = Button(text="Heal", size_hint=(1, 0.5))

        popup = Popup(title="Choose a Skill", content=layout, size_hint=(0.5, 0.3))
        fireball_button.bind(on_press=lambda x: self.use_skill("fireball", self.current_enemy, popup))
        heal_button.bind(on_press=lambda x: self.use_skill("heal", self.player, popup))
        layout.add_widget(fireball_button)
        layout.add_widget(heal_button)

        popup.open()

    def attack_enemy(self, instance):
        if self.current_enemy:
            self.combat(self.current_enemy)
        else:
            self.info_label.text += "\nNo enemy to attack."

    def run_from_combat(self, instance):
        if self.current_enemy:
            self.info_label.text += f"\nYou must defeat the {self.current_enemy['name']} to proceed!"
        else:
            self.info_label.text += "\nNo enemy to run from."

    def enable_combat_buttons(self, enable):
        self.attack_button.disabled = not enable
        self.defend_button.disabled = not enable
        self.skill_button.disabled = not enable
        self.run_button.disabled = not enable

if __name__ == "__main__":
    FlufftopiaApp().run()
