from colors import PURPLE, BLUE, CYAN, GREEN, YELLOW, RED, BOLD, RESET

from features.player import create_player
from features.inventory import show_inventory
from features.locations import explore


# CREATE PLAYER
player = create_player()

print(GREEN + f"\nWelcome to Mystery Island, {player['name']}!" + RESET)

game_running = True


# MAIN GAME LOOP
while game_running:

    print(PURPLE + BOLD)
    print("================================")
    print("       MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("================================")
    print(RESET)

    print(BLUE + f"\nLocation: {player['location']}" + RESET)
    print(YELLOW + f"Coins: {player['coins']}" + RESET)
    print(YELLOW + f"Energy: {player['energy']}" + RESET)

    print(CYAN + "\n1. Explore the island")
    print("2. View inventory")
    print("3. View instructions")
    print("4. Quit game" + RESET)

    choice = input(YELLOW + "\nChoose an option: " + RESET)

    # EXPLORE
    if choice == "1":

        won = explore(player)

        if won:
            game_running = False

    # VIEW INVENTORY
    elif choice == "2":

        show_inventory(player)

    # VIEW INSTRUCTIONS
    elif choice == "3":

        print(CYAN + "\n========== INSTRUCTIONS ==========")
        print("Explore all five locations.")
        print("Collect coins and useful objects.")
        print("Find the rope in the Jungle.")
        print("Find the lantern in the Cave.")
        print("Use the rope to cross the bridge.")
        print("Use the lantern to light the Lighthouse.")
        print("Keep your energy above zero!")
        print("==================================" + RESET)

    # QUIT GAME
    elif choice == "4":

        print(YELLOW + "\nThanks for playing, adventurer!" + RESET)
        game_running = False

    else:

        print(RED + "Invalid choice! Try again." + RESET)

    # CHECK ENERGY
    if game_running and player["energy"] <= 0:

        print(RED + BOLD)
        print("================================")
        print("          GAME OVER!")
        print("      YOU RAN OUT OF ENERGY!")
        print("================================")
        print(RESET)

        game_running = False

    if game_running:

        input(YELLOW + "\nPress Enter to continue..." + RESET)


print(PURPLE + "\nThank you for playing Mystery Island!" + RESET)