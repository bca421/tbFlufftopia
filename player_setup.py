import random

def player_setup():
    """Sets up the player character with initial attributes for Flufftopia."""
    print("Creating your character...")
    player = {
        "name": input("Enter your character's name: "),
        "health": 100,
        "strength": random.randint(10, 20),
        "defense": random.randint(5, 15),
        "agility": random.randint(5, 15),
        "inventory": []
    }
    print(f"\nWelcome, {player['name']}! Your adventure begins now.")
    print(f"Stats: Health = {player['health']}, Strength = {player['strength']}, Defense = {player['defense']}, Agility = {player['agility']}")
    print("\nThe journey ahead is perilous, but you feel ready to face any challenge.\n")
    return player
