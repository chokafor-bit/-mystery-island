from colors import GREEN, RED, RESET


def collect_coins(player):

    if not player["coins_collected"]:

        player["coins"] += 5
        player["coins_collected"] = True

        print(GREEN + "You collected 5 coins!" + RESET)

    else:

        print(RED + "You already collected these coins." + RESET)