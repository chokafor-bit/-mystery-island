from colors import GREEN, RED, RESET

def collect_coins(player):
       # pass
    if not player["coins_collected"]:
        player["coins"] += 5
        player["coins_collected"] = True
        player["level"] += 1
        print(GREEN + "You collected 5 coins!" + RESET)
    else:
        print(RED + "You already collected these coins." + RESET)