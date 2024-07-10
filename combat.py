# combat.py
import random
from skills import use_skill

def combat(player, enemy):
    """Handles combat between the player and an enemy."""
    print(f"A wild {enemy['name']} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n{player['name']}'s Health: {player['health']}")
        print(f"{enemy['name']}'s Health: {enemy['health']}")
        action = input("Do you want to [A]ttack or [R]un? > ").lower()
        
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
