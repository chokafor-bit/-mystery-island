from colors import BLUE, GREEN, YELLOW, RED, RESET

from features.coins import collect_coins
from features.inventory import collect_item
from features.energy import use_energy, collect_crystal
from features.lighthouse import light_beacon


def explore(player):

    location = player["location"]

    # BEACH
    if location == "Beach":

        print(BLUE + "\nYou are at the Beach." + RESET)
        print("1. Collect coins")
        print("2. Travel to Jungle")

        action = input(YELLOW + "Choose an action: " + RESET)

        if action == "1":

            collect_coins(player)

        elif action == "2":

            if use_energy(player):
                player["location"] = "Jungle"
                print(GREEN + "You travelled to the Jungle!" + RESET)

        else:
            print(RED + "Invalid action!" + RESET)

    # JUNGLE
    elif location == "Jungle":

        print(BLUE + "\nYou are in the Jungle." + RESET)
        print("1. Collect rope")
        print("2. Travel to Beach")
        print("3. Travel to Cave")
        print("4. Travel to Old Bridge")

        action = input(YELLOW + "Choose an action: " + RESET)

        if action == "1":

            collect_item(player, "Rope")

        elif action == "2":

            if use_energy(player):
                player["location"] = "Beach"
                print(GREEN + "You returned to the Beach!" + RESET)

        elif action == "3":

            if use_energy(player):
                player["location"] = "Cave"
                print(GREEN + "You entered the Cave!" + RESET)

        elif action == "4":

            if "Rope" in player["inventory"]:

                if use_energy(player):
                    player["location"] = "Old Bridge"
                    print(GREEN + "You crossed the bridge safely!" + RESET)

            else:
                print(RED + "You need a rope to cross the bridge!" + RESET)

        else:
            print(RED + "Invalid action!" + RESET)

    # CAVE
    elif location == "Cave":

        print(BLUE + "\nYou are in the Cave." + RESET)
        print("1. Collect lantern")
        print("2. Collect energy crystal")
        print("3. Return to Jungle")

        action = input(YELLOW + "Choose an action: " + RESET)

        if action == "1":

            collect_item(player, "Lantern")

        elif action == "2":

            collect_crystal(player)

        elif action == "3":

            if use_energy(player):
                player["location"] = "Jungle"
                print(GREEN + "You returned to the Jungle!" + RESET)

        else:
            print(RED + "Invalid action!" + RESET)

    # OLD BRIDGE
    elif location == "Old Bridge":

        print(BLUE + "\nYou are at the Old Bridge." + RESET)
        print("1. Return to Jungle")
        print("2. Travel to Lighthouse")

        action = input(YELLOW + "Choose an action: " + RESET)

        if action == "1":

            if use_energy(player):
                player["location"] = "Jungle"
                print(GREEN + "You returned to the Jungle!" + RESET)

        elif action == "2":

            if use_energy(player):
                player["location"] = "Lighthouse"
                print(GREEN + "You reached the Lighthouse!" + RESET)

        else:
            print(RED + "Invalid action!" + RESET)

    # LIGHTHOUSE
    elif location == "Lighthouse":

        print(BLUE + "\nYou are inside the Lighthouse." + RESET)
        print("1. Light the lighthouse beacon")

        action = input(YELLOW + "Choose an action: " + RESET)

        if action == "1":

            return light_beacon(player)

        else:
            print(RED + "Invalid action!" + RESET)

    return False