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
has_silver_sword = False # Has Silver Sword
has_health_potion = False # Has Health Potion
used_health_potion = False # Has Health Potion been used
boss_revived = False # Whether boss has revived
stage = 1 # Current stage
game_over = False # Is the game over
turn = 1 # Turn number

print("Hello {}, your adventure begins now!".format(player_name))
difficulty = input("Choose your difficulty: easy / normal / hard: ").lower()

# Adjust settings by difficulty
if difficulty == "easy":
    monster_attack = 5
    crit_chance = 0 
    crit_damage = 0
elif difficulty == "hard":
    monster_attack = 10
    crit_chance = 20
    crit_damage = 20
else:
    difficulty = "normal"
    monster_attack = 15
    crit_chance = 0
    crit_damage = 0

print("You selected {} mode.".format(difficulty))
print("-" * 30)

# Main game loop
while not game_over:

    # Set monster name and HP
    if stage == 1:
        monster_name = "Goblin"
        monster_hp = 30
    elif stage == 2:
        monster_name = "Orc"
        monster_hp = 30
    elif stage == 3:
        monster_name = "Troll"
        monster_hp = 30
    elif stage == 4:
        monster_name = "Dragon"
        monster_hp = 50
        boss_revived = False # Reset boss revive flag
    else:
        monster_name = " "
        monster_hp = 0

    print("You encounter a {}! (HP: {})".format(monster_name , monster_hp))

    # Battle loop
    while monster_hp > 0 and player_hp > 0:
        print("{} Turn {} {}".format("-" * 15, turn, "-" * 15))
        turn += 1 
        print("Your HP: {} / {}".format(player_hp , max_hp))
        print("{} HP: {}".format(monster_name , monster_hp))
        print("-" * 30)
        print("Choose your action:")
        print("  attack - Deal damage to the enemy")
        print("  defend - Block attack, recover 5 HP")
        print("  evade  - Try to dodge, maybe counterattack!")
        action = input("Your action: ")
        print("-" * 30)

        if action == "attack":
            monster_hp -= player_damage
            if random.randint(1, 100) <= 10:  
                heal_amount = 20
                player_hp += heal_amount
                if player_hp > max_hp:
                    player_hp = max_hp
                print("A mysterious healing light restores {} HP!".format(heal_amount))
            print("You attack the {} dealing {} damage.".format(monster_name , monster_hp))
        elif action == "defend":
            print("You brace yourself to defend the next attack.")
        elif action == "evade":
            print("You attempt to dodge the enemy's attack...")    
        else:
            print("Invalid action. Please choose 'attack' or 'defend'.")
            continue

        # Monster attacks
        if monster_hp > 0:
            print("{} attacks!".format(monster_name))
            if action == "defend":
                print("You brace yourself and block the attack.")
                player_hp += 5
                if player_hp > max_hp:
                    player_hp = max_hp
                print("You regain 5 HP while defending!")
            elif action == "evade":
                 # Evasion chance events
                chance = random.randint(1, 100)
                if chance <= 50:
                    print("You successfully dodged the attack!")
                elif 50 < chance <= 70:
                    player_hp -= 10
                    print("You failed to dodge and took 10 damage!")
                else:
                    monster_hp -= 30
                    print("Perfect dodge! You counterattacked and dealt 30 damage!")   

                # Boss revive mechanic
                if monster_hp <= 0 and stage == 4 and not boss_revived:
                    boss_revived = True
                    monster_hp = 50
                    print("The Dragon Boss refuses to fall and rises again with 50 HP!")     
            else:
               if crit_chance > 0 and random.randint(1, 100) <= crit_chance:
                   player_hp -= crit_damage
                   print("Critical Hit! You got hit and lost {} HP!".format(crit_damage))
               else:
                   player_hp -= monster_attack
                   print("You got hit and lost {} HP.".format(monster_attack))

        # Auto revive using potion
        if player_hp <= 0 and has_health_potion and not used_health_potion:
            print("You fell... but the Health Potion activates!")
            player_hp = 50
            used_health_potion = True

    # Player wins
    if player_hp > 0:
        print("You defeated the {}!".format(monster_name))

        stage += 1

        # Gain Silver Sword after stage 1
        if stage == 2 and not has_silver_sword:
            has_silver_sword = True
            player_damage += 10
            print("You found a Silver Sword! Your attack increases by 10.")

        # Gain Health Potion after stage 2
        if stage == 3 and not has_health_potion:
            has_health_potion = True
            print("You found a Health Potion! It will revive you once if you fall.")   

        # Game completed
        if stage == 5:
            print("-" * 30)
            print("You defeated the Dragon!")
            print("Congratulations! You return to your original world.")
            print("Welcome back, {}!".format(player_name))
            print("-" * 30)
            game_over = True     
# Player dies, restart
    else:
        print("You died! Restarting from the first monster...")
        player_hp = max_hp
        stage = 1
        used_health_potion = False        
