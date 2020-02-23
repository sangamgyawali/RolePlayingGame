from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

#create black magic
fire = Spell ("Fire", 10, 100, "Black")
thunder = Spell ("Thunder",10, 100, "Black")
meteor = Spell("Meteor", 20,200 , "black")
blizzard = Spell ("Blizzard", 10, 100, "Black")
quake = Spell ("Quake",14, 140, "Black")


#create white magic
cure = Spell ("Cure", 12, 120, "white")
cura = Spell ("Cura", 18, 200, "white")

#create some items
po


#instantiate people
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy Attacks" + bcolors.ENDC)

while running:
    print("*********************")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for ", dmg, " points of damage. Enemy HP", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        choice_m = int(input("Choose Magic: ")) - 1

        spell = player.magic[choice_m]

        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.Fail + "\nYou don't have enough magic points to use this magic!!" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if (spell.type=="white"):
            player.heal(magic_dmg)
            print(bcolors.OKBLUE+"Your Hp increased to: " + str(player.get_hp), "points")
        elif (spell.type=="black")
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("************************************")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your Magic Points: ", bcolors.OKBLUE + str(player.get_mp) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp == 0:
        print(bcolors.OKGREEN + "You WIN!!" + bcolors.ENDC)
        running = False
    elif player.get_hp == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You LOSE!!!!!" + "bcolors.ENDC")

    # running = False
