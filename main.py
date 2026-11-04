game_running = True

while game_running:

    print("================================")
    print("       MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("================================")

    print("You have survived a terrible storm.")
    print("You are stranded on a mysterious island.")

    print("Your mission: Restore the lighthouse")
    print("before your energy runs out.")

    print()
    print("1. Explore the island")
    print("2. View instructions")
    print("3. Quit game")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You are exploring the island!")

    elif choice == "2":
        print("Find the lighthouse to escape!")

    elif choice == "3":
        print("Thanks for playing!")
        game_running = False

    else:
        print("Invalid choice! Try again.")

    input("\nPress Enter to return to the menu...")