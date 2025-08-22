import random
print("-" * 30)

# Get player name
player_name = input("Welcome to the other world! What is your name? ")
print("-" * 30)

# Initialize player stats
max_hp = 100
player_hp = max_hp
player_base_damage = 15
player_damage = player_base_damage
has_silver_sword = False  # Has Silver Sword
has_health_potion = False  # Has Health Potion
used_health_potion = False  # Has Health Potion been used
boss_revived = False  # Whether boss has revived
stage = 1  # Current stage
game_over = False  # Is the game over
turn = 1  # Turn number

print(f"Hello {player_name}, your adventure begins now!")
# difficulty input with validation
while True:
    difficulty = input("Choose your difficulty: easy / normal / hard: ").lower()
    if difficulty in ["easy", "normal", "hard"]:
        break
    else:
        print("Invalid difficulty! Please enter easy, normal, or hard.")

# Adjust settings by difficulty
if difficulty == "easy":
    monster_attack = 5
    crit_chance = 0
    crit_damage = 0
elif difficulty == "hard":
    monster_attack = 10
    crit_chance = 20
    crit_damage = 25
else:  # normal
    monster_attack = 10
    crit_chance = 10
    crit_damage = 15

print(f"You selected {difficulty} mode.")
print("-" * 30)

# Set monster name and HP
monsters = [
    {"name": "Goblin", "hp": 30},
    {"name": "Orc",    "hp": 40},
    {"name": "Troll",  "hp": 50},
    {"name": "Dragon", "hp": 80}
]

# Player actions

def player_attack(monster_hp, monster_name):
    global player_hp
    monster_hp -= player_damage
    print(f"You attack the {monster_name}, dealing {player_damage} damage.")
    # 10% chance of health recovery
    if random.randint(1, 100) <= 10:
        heal_amount = 20
        player_hp += heal_amount
        if player_hp > max_hp:
            player_hp = max_hp
        print(f"A mysterious healing light restores {heal_amount} HP!")
    return monster_hp

def player_defend():
    global player_hp
    print("You brace yourself and block the next attack.")
    player_hp += 5
    if player_hp > max_hp:
        player_hp = max_hp
    print("You regain 5 HP while defending!")

def player_evade(monster_hp, monster_name):
    """Resolve the enemy's attack when the player chose to evade."""
    global player_hp
    chance = random.randint(1, 100)
    if chance <= 50:
        print("You successfully dodged the attack!")
    elif chance <= 70:
        player_hp -= 10
        print("You failed to dodge and took 10 damage!")
    else:
        monster_hp -= 30
        print(f"Perfect dodge! You counterattacked the {monster_name} for 30 damage!")
    return monster_hp

# Monster turn

def monster_turn(action, monster_hp, monster_name):
    global player_hp, boss_revived

    if monster_hp <= 0:  # if the monster is already dead, it can't attack
        return monster_hp

    print(f"{monster_name} attacks!")

    if action == "defend":
        print("You blocked the attack!")
    elif action == "evade":
        monster_hp = player_evade(monster_hp, monster_name)
    else:
        if random.randint(1, 100) <= crit_chance:
            player_hp -= crit_damage
            print(f"Critical Hit! You took {crit_damage} damage!")
        else:
            player_hp -= monster_attack
            print(f"You got hit and lost {monster_attack} HP.")

    # Boss resurgence
    if monster_hp <= 0 and monster_name == "Dragon" and not boss_revived:
        boss_revived = True
        monster_hp = 50
        print("The Dragon refuses to fall and rises again with 50 HP!")

    return monster_hp

# Main game loop

while not game_over:
    monster = monsters[stage - 1]
    monster_name = monster["name"]
    monster_hp = monster["hp"]
    boss_revived = False

    print(f"You encounter a {monster_name}! (HP: {monster_hp})")

    # Battle loop
    while monster_hp > 0 and player_hp > 0:
        print(f"{'-'*15} Turn {turn} {'-'*15}")
        print(f"Your HP: {player_hp}/{max_hp}")
        print(f"{monster_name} HP: {monster_hp}")
        print("-" * 30)

        action = input("Choose your action (attack/defend/evade): ").lower()
        print("-" * 30)

        if action == "attack":
            monster_hp = player_attack(monster_hp, monster_name)
        elif action == "defend":
            player_defend()
        elif action == "evade":
            print("You attempt to dodge the enemy's attack...")
        else:
            print("Invalid action!")
            continue

        monster_hp = monster_turn(action, monster_hp, monster_name)

        # Auto revive using potion
        if player_hp <= 0 and has_health_potion and not used_health_potion:
            print("The Health Potion activates! You revive with 50 HP!")
            player_hp = 50
            used_health_potion = True

        if monster_hp > 0 and player_hp > 0:
            turn += 1

    # After the battle ends
    if player_hp > 0:
        print(f"You defeated the {monster_name}!")
        stage += 1

        if stage == 2 and not has_silver_sword:
            has_silver_sword = True
            player_damage += 10
            print("You found a Silver Sword! Attack +10!")
        elif stage == 3 and not has_health_potion:
            has_health_potion = True
            print("You found a Health Potion! It will revive you once.")

        if stage > len(monsters):
            print("-" * 30)
            print("You defeated the Dragon! Congratulations!")
            print(f"Welcome back, {player_name}!")
            print("-" * 30)
            game_over = True
    else:
        print("You died! Restarting from the first monster...")
        player_hp = max_hp
        stage = 1
        used_health_potion = False
        turn = 1

