from game_intro import game_intro
from player_setup import player_setup
from locations import locations
from events import random_event

def describe_location(location, locations):
    """Displays the description of the current location."""
    print(f"You are at the {location.replace('_', ' ').title()}.")
    print(locations[location]["description"])

def discover_secret_path(location, locations):
    """Checks for and handles the discovery of secret paths in the current location."""
    if "secret" in locations[location]:
        print(locations[location]["secret"])
        choice = input("Do you want to explore the secret path? (yes/no) > ")
        if choice.lower() == "yes":
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
