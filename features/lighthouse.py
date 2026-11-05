from colors import GREEN, RED, BOLD, RESET


def light_beacon(player):
     # pass
    if "Lantern" not in player["inventory"]:
        print(RED + "You need a lantern to light the beacon!" + RESET)
        return False
    if player["energy"] <= 0:
        print(RED + "You do not have enough energy!" + RESET)
        return False

    print(GREEN + BOLD)
    print("================================")
    print("      THE LIGHTHOUSE IS LIT!")
    print("          YOU WIN!")
    print("================================")
    print(RESET)
    print(f"Congratulations, {player['name']}!")
    print(f"You finished with {player['coins']} coins.")
    print(f"You finished with {player['energy']}  energy.")
    print(f"You finished at level {player['level']}.")
    print(f"You finished with {player['life']} lives.")
    return True