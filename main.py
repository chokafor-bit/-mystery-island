from colors import PURPLE, BLUE, CYAN, GREEN, YELLOW, RED, BOLD, RESET

from features.player import create_player
from features.inventory import show_inventory
from features.locations import explore
from features.shop import show_shop


# Create the player
player = create_player()

print(GREEN + f"\nWelcome to Mystery Island, {player['name']}!" + RESET)
print(f"Level: {player['level']}")
print(f"Life: {player['life']}")

game_running = True

while game_running:

    print(PURPLE + BOLD)
    print("================================")
    print("       MYSTERY ISLAND           ")
    print("    THE LOST LIGHTHOUSE         ")
    print("================================")
    print(RESET)

    # Display player information
    print(BLUE + f"\nLocation: {player['location']}" + RESET)
    print(YELLOW + f"Coins: {player['coins']}" + RESET)
    print(YELLOW + f"Energy: {player['energy']}" + RESET)
    print(YELLOW + f"Lives: {player['life']}" + RESET)

    # Main menu
    print(CYAN + "\n1. Explore the island")
    print("2. View inventory")
    print("3. View instructions")
    print("4. Visit Shop")
    print("5. Quit game" + RESET)

    choice = input(YELLOW + "\nChoose an option: " + RESET)

    if choice == "1":

        won = explore(player)

        if won:
            game_running = False

    elif choice == "2":

        show_inventory(player)

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

    elif choice == "4":

        show_shop(player)

    elif choice == "5":

        print(YELLOW + "\nThanks for playing, adventurer!" + RESET)
        game_running = False

    else:

        print(RED + "Invalid choice! Try again." + RESET)

    # Check player's energy
    if game_running and player["energy"] <= 0:

        player["life"] -= 1
        player["energy"] = 5

        print(RED + f"\nYou lost a life! Lives remaining: {player['life']}" + RESET)

        # Check if player has lost all lives
        if player["life"] <= 0:

            print(RED + BOLD)
            print("================================")
            print("          GAME OVER!            ")
            print("   YOU LOST ALL YOUR LIVES!     ")
            print("================================")
            print(RESET)

            game_running = False

    if game_running:
        input(YELLOW + "\nPress Enter to continue..." + RESET)

print(PURPLE + "\nThank you for playing Mystery Island!" + RESET)