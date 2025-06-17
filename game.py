import random
print("-" * 30)
player_name = input("Welcome to the other world! What is your name? ")
print("-" * 30)

max_hp = 100
player_hp = max_hp
player_base_damage = 15
player_damage = player_base_damage
has_silver_sword = False
has_health_potion = False
used_health_potion = False
boss_revived = False
stage = 1
game_over = False
turn = 1

print("Hello {}, your adventure begins now!".format(player_name))
print("-" * 30)

while not game_over:
    
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
        boss_revived = False
    else:
        monster_name = " "
        monster_hp = 0

    print("You encounter a {}! (HP: {})".format(monster_name , monster_hp))

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
            if random.randint(1, 100) <= 20:  
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

        if monster_hp > 0:
            print("{} attacks!".format(monster_name))
            if action == "defend":
                print("You brace yourself and block the attack.")
                player_hp += 5
                if player_hp > max_hp:
                    player_hp = max_hp
                print("You regain 5 HP while defending!")
            elif action == "evade":
                chance = random.randint(1, 100)
                if chance <= 50:
                    print("You successfully dodged the attack!")
                elif chance <= 70:
                    player_hp -= 10
                    print("You failed to dodge and took 10 damage!")
                else:
                    monster_hp -= 30
                    print("Perfect dodge! You counterattacked and dealt 30 damage!")   
                if monster_hp <= 0 and stage == 4 and not boss_revived:
                    boss_revived = True
                    monster_hp = 50
                    print("The Dragon Boss refuses to fall and rises again with 50 HP!")     
            else:
                player_hp -= 10
                print("You got hit and lost 10 HP.")

        if player_hp <= 0 and has_health_potion and not used_health_potion:
            print("You fell... but the Health Potion activates!")
            player_hp = 50
            used_health_potion = True

    if player_hp > 0:
        print("You defeated the {}!".format(monster_name))

        stage += 1

        if stage == 2 and not has_silver_sword:
            has_silver_sword = True
            player_damage += 10
            print("You found a Silver Sword! Your attack increases by 10.")

        if stage == 3 and not has_health_potion:
            has_health_potion = True
            print("You found a Health Potion! It will revive you once if you fall.")   

        if stage == 5:
            print("-" * 30)
            print("You defeated the Dragon!")
            print("Congratulations! You return to your original world.")
            print("Welcome back, {}!".format(player_name))
            print("-" * 30)
            game_over = True     

    else:
        print("You died! Restarting from the first monster...")
        player_hp = max_hp
        stage = 1
        used_health_potion = False        
