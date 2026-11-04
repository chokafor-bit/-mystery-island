from colors import GREEN, RED, PURPLE, RESET


def collect_item(player, item):

    if item == "Rope":
        if not player["rope_collected"]:
            player["inventory"].append("Rope")
            player["rope_collected"] = True
            print(GREEN + "You collected a rope!" + RESET)
        else:
            print(RED + "You already have a rope." + RESET)
    elif item == "Lantern":
        if not player["lantern_collected"]:
            player["inventory"].append("Lantern")
            player["lantern_collected"] = True
            print(GREEN + "You collected a lantern!" + RESET)
        else:
            print(RED + "You already have a lantern." + RESET)


def show_inventory(player):
    print(PURPLE + "\n========== INVENTORY ==========" + RESET)
    print(f"Coins: {player['coins']}")
    print(f"Items: {player['inventory']}")
    print(f"Energy: {player['energy']}")
    print(PURPLE + "================================" + RESET)