# skills.py
def use_skill(player, skill, target):
    """Applies a skill used by the player on the target in Flufftopia."""
    if skill == "fireball":
        damage = player["magic"] * 2 - target["defense"]
        target["health"] -= max(0, damage)
        print(f"You cast a fireball at {target['name']} for {damage} damage!")
    elif skill == "heal":
        heal_amount = player["magic"] * 2
        player["health"] = min(player["max_health"], player["health"] + heal_amount)
        print(f"You heal yourself for {heal_amount} health points!")
    # Add more skills as needed
