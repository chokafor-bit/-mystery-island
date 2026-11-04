from colors import GREEN, RED, RESET


def use_energy(player):

    if player["energy"] > 0:

        player["energy"] -= 1
        return True

    print(RED + "You have no energy left!" + RESET)
    return False


def collect_crystal(player):

    if not player["crystal_collected"]:

        player["energy"] += 3
        player["crystal_collected"] = True

        print(GREEN + "You found an energy crystal! +3 energy." + RESET)

    else:

        print(RED + "You already collected the crystal." + RESET)