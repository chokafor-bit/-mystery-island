from colors import CYAN, YELLOW, RESET
from features.locations import explore

def start_exploration(player):

    print(CYAN + "\n========== EXPLORATION ==========" + RESET)
    print("1. Explore current location")
    print("2. Check current location")
    choice = input(YELLOW + "Choose an option: " + RESET)
    if choice == "1":
        return explore(player)
    elif choice == "2":
        print(f"You are currently at {player['location']}.")
    else:
        print("Invalid exploration choice!")

    return False