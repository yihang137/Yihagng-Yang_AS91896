player_name = input("Welcome to the other world! What is your name? ")

max_hp = 100
player_hp = max_hp
player_base_damage = 10
player_damage = player_base_damage
has_silver_sword = False
has_health_potion = False
used_health_potion = False

stage = 1
game_over = False

print("Hello {}, your adventure begins now!".format(player_name))

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
    else:
        monster_name = " "
        monster_hp = 0

    print("You encounter a {}! (HP: {})".format(monster_name , monster_hp))

    while monster_hp > 0 and player_hp > 0:
        print("Your HP: {} / {}".format(player_hp , max_hp))
        print("{} HP: {}".format(monster_name , monster_hp))
        action = input("Choose your action: attack or defend? ")

        if action == "attack":
            monster_hp -= player_damage
            print("You attack the {} dealing {} damage.".format(monster_name , monster_hp))
        elif action == "defend":
            print("You brace yourself to defend the next attack.")
        else:
            print("Invalid action. Please choose 'attack' or 'defend'.")
            continue

        if monster_hp > 0:
            print("{} attacks!".format(monster_name))
            if action == "defend":
                monster_hp -= 10
                print("You blocked the attack! {} takes 10 damage.".format(monster_name))
            else:
                player_hp -= 10
                print("You got hit and lost 10 HP.")

        if player_hp <= 0 and has_health_potion and not used_health_potion:
            print("You fell... but the Health Potion activates!")
            player_hp = 50
            used_health_potion = True

    if player_hp > 0:
        print("You defeated the {}!".format(monster_name))
