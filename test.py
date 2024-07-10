import pygame
import pytmx
import os
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
CHARACTER_SIZE = 64
FPS = 60

# Load the map
tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flufftopia")

# Load the sprites
player_image = pygame.image.load('img/player.png').convert_alpha()
npc_image = pygame.image.load('img/npc.png').convert_alpha()
enemies_image = pygame.image.load('img/enemies.png').convert_alpha()
monsters_image = pygame.image.load('img/monsters.png').convert_alpha()
boss_image = pygame.image.load('img/boss.png').convert_alpha()

# Player setup
player = {
    "name": "Hero",
    "health": 100,
    "strength": random.randint(10, 20),
    "defense": random.randint(5, 15),
    "agility": random.randint(5, 15),
    "inventory": [],
    "quests": [],
    "x": 5,
    "y": 5
}

# NPC setup (example)
npcs = [
    {"name": "Arin the Wise", "dialogue": "Hello traveler!", "x": 10, "y": 10}
]

# Enemy setup (example)
enemies = [
    {"name": "Goblin", "health": 30, "strength": 10, "defense": 5, "loot": ["goblin ear", "rusty sword"], "x": 15, "y": 15}
]

# Game loop
running = True
clock = pygame.time.Clock()

def draw_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

def draw_player():
    screen.blit(player_image, (player['x'] * TILE_SIZE, player['y'] * TILE_SIZE), (0, 0, CHARACTER_SIZE, CHARACTER_SIZE))

def draw_npcs():
    for npc in npcs:
        screen.blit(npc_image, (npc['x'] * TILE_SIZE, npc['y'] * TILE_SIZE), (0, 0, CHARACTER_SIZE, CHARACTER_SIZE))

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemies_image, (enemy['x'] * TILE_SIZE, enemy['y'] * TILE_SIZE), (0, 0, CHARACTER_SIZE, CHARACTER_SIZE))

def handle_movement(keys):
    if keys[pygame.K_UP]:
        player['y'] -= 1
    if keys[pygame.K_DOWN]:
        player['y'] += 1
    if keys[pygame.K_LEFT]:
        player['x'] -= 1
    if keys[pygame.K_RIGHT]:
        player['x'] += 1

def combat(player, enemy):
    """Handles combat between the player and an enemy."""
    print(f"A wild {enemy['name']} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n{player['name']}'s Health: {player['health']}")
        print(f"{enemy['name']}'s Health: {enemy['health']}")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_attack(player, enemy)
                    if enemy["health"] > 0:
                        enemy_attack(player, enemy)
                elif event.key == pygame.K_r:
                    if random.choice([True, False]):
                        print(f"You managed to escape from the {enemy['name']}!")
                        return
                    else:
                        print(f"You failed to escape. The {enemy['name']} attacks!")
                        enemy_attack(player, enemy)
                elif event.key == pygame.K_s:
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

def use_skill(player, skill, target):
    """Applies a skill used by the player in Flufftopia."""
    if skill == "fireball":
        damage = player["strength"] * 2 - target["defense"]
        target["health"] -= damage
        print(f"You use fireball on the {target['name']} for {damage} damage!")

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    handle_movement(keys)

    screen.fill((0, 0, 0))
    draw_map()
    draw_player()
    draw_npcs()
    draw_enemies()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
