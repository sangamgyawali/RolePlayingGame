from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

print("\n\n")

# create black magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
quake = Spell("Quake", 14, 140, "Black")

# create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 99999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores party's HP/MP", 99999)
grenade = Item("Grenade", "attack", "Deals 500 Hp Damage to oponent", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]
enemy_spells = [fire, meteor, cure]

# instantiate people
player1 = Person("Valos", 3300, 132, 60, 34, player_spells, player_items)
player2 = Person("Nick ", 4602, 123, 60, 34, player_spells, player_items)
player3 = Person("Robot", 3201, 154, 60, 34, player_spells, player_items)

enemy3 = Person("Imp  ", 1250, 130, 560, 345, enemy_spells, [])
enemy1 = Person("Magus", 18000, 65, 700, 25, enemy_spells, [])
enemy2 = Person("Imp  ", 1250, 130, 560, 345, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy2, enemy1, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy Attacks" + bcolors.ENDC)

while running:
    print("*********************\n\n")
    print("Name                              HP                           MP")
    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:
        player.choose_action()
        choice = input("Choose Action: ")
        index = int(choice) - 1
        if index == -1:
            continue
        elif index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(bcolors.OKBLUE + player.name + " attacked " + enemies[enemy].name + " for " + str(
                dmg) + " points of damage. Enemy HP ", enemies[enemy].get_hp(), bcolors.ENDC)
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            choice_m = int(input("Choose Magic: ")) - 1
            if choice_m == -1:
                continue
            spell = player.magic[choice_m]

            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.Fail + "\nYou don't have enough magic points to use this magic!!" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "Your Hp increased to: " + str(player.get_hp), "points")
            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg),
                      "points of damage to " + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

        elif index == 2:
            player.choose_items()
            choice_i = int(input("Enter the item you want to use")) - 1
            if choice_i == -1:
                continue

            item = player.items[choice_i]["item"]
            player.items[choice_i]["quantity"] -= 1
            if player.items[choice_i]["quantity"] <= 0:
                player.items[choice_i]["quantity"] = 0

                print(bcolors.FAIL + "\nNone left..." + bcolors.ENDC)
                continue

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), " HP " + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " Fully restores HP/MP" + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop),
                      " HP of damage to " + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemies += 1
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You WIN!!" + bcolors.ENDC)
        running = False
    for player in players:
        if player.get_hp == 0:
            defeated_players += 1
    if defeated_players == 2:
        print(bcolors.FAIL + bcolors.BOLD + "You LOSE!!!!!" + "bcolors.ENDC")
        running = False

    # enemy_choice = 1

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace("    :", "") + "attacks " + players[target].name.replace("    :", "") + "for",
                  enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals" + enemy.name + "for " + str(magic_dmg),
                      "HP" + bcolors.ENDC)

            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + enemy.name.replace("    :", "") + "'s" + spell.name + " deals",
                      str(magic_dmg), "points of damage to " + players[target].name.replace("    :", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace("    :", "") + " has died.")
                    del players[player]
