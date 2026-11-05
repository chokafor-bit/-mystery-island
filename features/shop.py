from colors import PURPLE, GREEN, YELLOW, RED, RESET


def show_shop(player):

    while True:

        print(f"\nYou have {player['coins']} coins.")

        print(PURPLE + "\n============ MYSTERY ISLAND SHOP ===========")
        print("1. Buy Extra Life - 10 coins")
        print("2. Buy Energy - 5 coins")
        print("3. Buy Lantern - 15 coins")
        print("4. Leave Shop" + RESET)

        choice = input(YELLOW + "\nChoose an item: " + RESET)

        if choice == "1":

            print(GREEN + "You selected Extra Life!" + RESET)

        elif choice == "2":

            print(GREEN + "You selected Energy!" + RESET)

        elif choice == "3":

            print(GREEN + "You selected Lantern!" + RESET)

        elif choice == "4":

            print(YELLOW + "You left the shop!" + RESET)
            break

        else:

            print(RED + "Invalid choice! Try again." + RESET)