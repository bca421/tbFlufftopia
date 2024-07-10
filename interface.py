# interface.py
import tkinter as tk
from game_intro import game_intro
from player_setup import player_setup
from locations import locations
from events import random_event

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Flufftopia")
        
        self.player = None
        self.current_location = "village"
        
        self.text_area = tk.Text(root, height=15, width=50)
        self.text_area.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        self.entry.bind("<Return>", self.process_input)
        
        self.start_game()

    def start_game(self):
        """Starts the game by showing the intro and setting up the player."""
        game_intro()
        self.player = player_setup()
        self.show_message(f"Welcome, {self.player['name']}! Your adventure begins now.")
        self.game_loop()
    
    def show_message(self, message):
        """Displays a message in the text area."""
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)
        
    def process_input(self, event):
        """Processes user input from the entry widget."""
        user_input = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.handle_choice(user_input)
        
    def handle_choice(self, choice):
        """Handles the player's choice and updates the game state."""
        if choice == "1":
            self.current_location = "enchanted_forest"
        elif choice == "2":
            self.current_location = "village"
        elif choice == "3":
            self.current_location = "ancient_ruins"
        elif choice == "4":
            self.current_location = "haunted_castle"
        elif choice == "5":
            self.current_location = "serene_lake"
        elif choice == "6":
            self.show_message(f"Inventory: {self.player['inventory']}")
            self.show_message(f"Health: {self.player['health']}")
            return
        elif choice == "7":
            self.show_message("Thanks for playing!")
            self.root.quit()
            return
        else:
            self.show_message("Invalid choice. Try again.")
            return

        self.describe_location(self.current_location)
        self.current_location = self.discover_secret_path(self.current_location)
        random_event(self.current_location, self.player)

        if self.player["health"] <= 0:
            self.show_message("You have died. Game over.")
            self.root.quit()

    def describe_location(self, location):
        """Displays the description of the current location."""
        self.show_message(f"You are at the {location.replace('_', ' ').capitalize()}.")
        self.show_message(locations[location]["description"])

    def discover_secret_path(self, location):
        """Checks for and handles the discovery of secret paths in the current location."""
        if "secret" in locations[location]:
            self.show_message(locations[location]["secret"])
            choice = input("Do you want to explore the secret path? (yes/no) > ").lower()
            if choice == "yes":
                return locations[location]["secret_location"]
        return location

    def game_loop(self):
        """Main game loop handling player actions and events."""
        self.show_message("\nWhat do you want to do?")
        self.show_message("1. Explore the enchanted forest")
        self.show_message("2. Visit the village")
        self.show_message("3. Enter the ancient ruins")
        self.show_message("4. Explore the haunted castle")
        self.show_message("5. Go to the serene lake")
        self.show_message("6. Check inventory")
        self.show_message("7. Quit")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()
