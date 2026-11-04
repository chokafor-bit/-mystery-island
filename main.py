
# MYSTERY ISLAND - THE LOST LIGHTHOUSE



PURPLE = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"



player_name = input(YELLOW + "What is your name, adventurer? " + RESET)

print(GREEN + f"\nWelcome to Mystery Island, {player_name}!" + RESET)

current_location = "Beach"
coins = 0
energy = 5
inventory = []

# TRACK COLLECTED ITEMS
coins_collected = False
rope_collected = False
lantern_collected = False
crystal_collected = False

game_running = True



while game_running:

    print(PURPLE + BOLD)
    print("================================")
    print("       MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("================================")
    print(RESET)

    print(BLUE + f"\nLocation: {current_location}" + RESET)
    print(YELLOW + f"Coins: {coins}" + RESET)
    print(YELLOW + f"Energy: {energy}" + RESET)

    print(CYAN + "\n1. Explore the island")
    print("2. View inventory")
    print("3. View instructions")
    print("4. Quit game" + RESET)

    choice = input(YELLOW + "\nChoose an option: " + RESET)

    if choice == "2":

        print(PURPLE + "\n========== INVENTORY ==========" + RESET)
        print(f"Coins: {coins}")
        print(f"Items: {inventory}")
        print(f"Energy: {energy}")
        print(PURPLE + "================================" + RESET)

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

        print(YELLOW + "\nThanks for playing, adventurer!" + RESET)
        game_running = False

    # EXPLORE
    elif choice == "1":

        if current_location == "Beach":

            print(BLUE + "\nYou are at the Beach." + RESET)
            print("1. Collect coins")
            print("2. Travel to Jungle")

            action = input(YELLOW + "Choose an action: " + RESET)

            if action == "1":

                if not coins_collected:
                    coins += 5
                    coins_collected = True
                    print(GREEN + "You collected 5 coins!" + RESET)

                else:
                    print(RED + "You already collected these coins." + RESET)

            elif action == "2":

                current_location = "Jungle"
                energy -= 1
                print(GREEN + "You travelled to the Jungle!" + RESET)

            else:
                print(RED + "Invalid action!" + RESET)

        
        elif current_location == "Jungle":

            print(BLUE + "\nYou are in the Jungle." + RESET)
            print("1. Collect rope")
            print("2. Travel to Beach")
            print("3. Travel to Cave")
            print("4. Travel to Old Bridge")

            action = input(YELLOW + "Choose an action: " + RESET)

            if action == "1":

                if not rope_collected:
                    inventory.append("Rope")
                    rope_collected = True
                    print(GREEN + "You collected a rope!" + RESET)

                else:
                    print(RED + "You already have a rope." + RESET)

            elif action == "2":

                current_location = "Beach"
                energy -= 1
                print(GREEN + "You returned to the Beach!" + RESET)

            elif action == "3":

                current_location = "Cave"
                energy -= 1
                print(GREEN + "You entered the Cave!" + RESET)

            elif action == "4":

                if "Rope" in inventory:
                    current_location = "Old Bridge"
                    energy -= 1
                    print(GREEN + "You crossed the bridge safely!" + RESET)

                else:
                    print(RED + "You need a rope to cross the bridge!" + RESET)

            else:
                print(RED + "Invalid action!" + RESET)

        elif current_location == "Cave":

            print(BLUE + "\nYou are in the Cave." + RESET)
            print("1. Collect lantern")
            print("2. Collect energy crystal")
            print("3. Return to Jungle")

            action = input(YELLOW + "Choose an action: " + RESET)

            if action == "1":

                if not lantern_collected:
                    inventory.append("Lantern")
                    lantern_collected = True
                    print(GREEN + "You collected a lantern!" + RESET)

                else:
                    print(RED + "You already have a lantern." + RESET)

            elif action == "2":

                if not crystal_collected:
                    energy += 3
                    crystal_collected = True
                    print(GREEN + "You found an energy crystal! +3 energy." + RESET)

                else:
                    print(RED + "You already collected the crystal." + RESET)

            elif action == "3":

                current_location = "Jungle"
                energy -= 1
                print(GREEN + "You returned to the Jungle!" + RESET)

            else:
                print(RED + "Invalid action!" + RESET)

        elif current_location == "Old Bridge":

            print(BLUE + "\nYou are at the Old Bridge." + RESET)
            print("1. Return to Jungle")
            print("2. Travel to Lighthouse")

            action = input(YELLOW + "Choose an action: " + RESET)

            if action == "1":

                current_location = "Jungle"
                energy -= 1
                print(GREEN + "You returned to the Jungle!" + RESET)

            elif action == "2":

                current_location = "Lighthouse"
                energy -= 1
                print(GREEN + "You reached the Lighthouse!" + RESET)

            else:
                print(RED + "Invalid action!" + RESET)

        elif current_location == "Lighthouse":

            print(BLUE + "\nYou are inside the Lighthouse." + RESET)
            print("1. Light the lighthouse beacon")

            action = input(YELLOW + "Choose an action: " + RESET)

            if action == "1":

                if "Lantern" in inventory:

                    if energy > 0:

                        print(GREEN + BOLD)
                        print("================================")
                        print("      THE LIGHTHOUSE IS LIT!")
                        print("          YOU WIN!")
                        print("================================")
                        print(RESET)

                        print(f"Congratulations, {player_name}!")
                        print(f"You finished with {coins} coins.")

                        game_running = False

                    else:
                        print(RED + "You do not have enough energy!" + RESET)

                else:
                    print(RED + "You need a lantern to light the beacon!" + RESET)

            else:
                print(RED + "Invalid action!" + RESET)

    else:
        print(RED + "Invalid choice! Try again." + RESET)

    # CHECK ENERGY
    if game_running and energy <= 0:

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