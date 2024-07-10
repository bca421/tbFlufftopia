# quests.py
def start_quest(player, quest_name):
    """Starts a new quest for the player in Flufftopia."""
    print(f"You have started the quest: {quest_name}")
    player["quests"].append(quest_name)
    if quest_name == "Find the Ancient Artifact":
        print("You need to explore the ancient ruins to find the artifact.")
    elif quest_name == "Defeat the Dragon":
        print("You must find and defeat the dragon on Dragon Peak.")
    # Add more quests as needed
