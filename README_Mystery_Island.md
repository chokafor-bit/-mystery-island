# 🏝️ Mystery Island: The Lost Lighthouse

## Python Beginner-to-Project Learning Guide

### Project Overview

Mystery Island is a text-based adventure game built with Python.

The player explores an island, collects coins and items, manages energy
and lives, visits a shop, and tries to light the lighthouse beacon to
win the game.

This project is designed to help a beginner learn Python by building a
real application step by step.

**Important learning rule:** Understand the logic first. Write the code
yourself second. Test it third. Do not rush to copy and paste complete
solutions.

------------------------------------------------------------------------

# 1. Project Objectives

By completing this project, you should understand:

-   Variables and data types
-   Strings, integers, floats, and booleans
-   User input and output
-   Type conversion
-   Conditional statements
-   Loops
-   Functions
-   Parameters and arguments
-   Return values
-   Lists
-   Dictionaries
-   Modules and imports
-   Boolean logic
-   Game state management
-   Error handling
-   Code organization
-   Debugging
-   Testing
-   Basic Git and GitHub workflow

------------------------------------------------------------------------

# 2. Game Requirements

## Player System

The player should have:

-   Name
-   Location
-   Level
-   Lives
-   Coins
-   Energy
-   Inventory

## Island Locations

The game should contain five locations:

1.  Beach
2.  Jungle
3.  Cave
4.  Old Bridge
5.  Lighthouse

## Exploration System

The player should be able to:

-   Explore different locations.
-   Travel between locations.
-   Collect coins.
-   Collect items.
-   Use energy when travelling.
-   Discover the lighthouse.

## Inventory System

The player should be able to:

-   Collect a rope.
-   Collect a lantern.
-   View collected items.
-   Avoid collecting the same special item multiple times.

## Energy System

The player starts with 5 energy. The player should:

-   Lose energy when travelling.
-   Find an energy crystal.
-   Recover energy.
-   Lose a life when energy runs out.

## Shop System

The shop should offer:

  Item              Price
  ------------ ----------
  Extra Life     10 coins
  Energy          5 coins
  Lantern        15 coins

The player should be able to:

-   View available items.
-   View their coins.
-   Buy an item.
-   Lose coins after purchasing.
-   Receive the purchased item.
-   Get a message when they cannot afford an item.
-   Leave the shop and return to the main menu.

## Winning System

To win, the player must:

-   Find the rope.
-   Cross the Old Bridge.
-   Find the lantern.
-   Reach the Lighthouse.
-   Light the beacon.

## Losing System

The player loses when all lives are exhausted.

## Main Menu

The main menu should contain:

1.  Explore the island
2.  View inventory
3.  View instructions
4.  Visit shop
5.  Quit game

------------------------------------------------------------------------

# 3. Learning Roadmap

## Phase 1: Understand Python Basics

### Step 1 --- Variables

Learn: - What a variable is. - How to store information. - How to change
a variable's value.

Exercise: Create variables for a player's name, coins, energy, and
lives.

Checkpoint: You can explain what each variable stores.

### Step 2 --- Data Types

Learn: - `str` - `int` - `float` - `bool`

Exercise: Create player information using different data types.

Checkpoint: You can identify the type of each variable.

### Step 3 --- Input and Output

Learn: - `print()` - `input()` - How Python receives information from
the user.

Exercise: Ask the player for their name.

Checkpoint: You can display a personalized welcome message.

### Step 4 --- Type Conversion

Learn: - `int()` - `float()` - Why `input()` returns a string.

Exercise: Ask the player how many coins they want to collect.

Checkpoint: You can convert input into a number and perform
calculations.

## Phase 2: Decision Making

### Step 5 --- If Statements

Learn: - `if` - `elif` - `else` - Comparison operators

Exercise: Check whether the player has enough coins to buy an item.

Checkpoint: You understand how Python chooses which condition to
execute.

### Step 6 --- Logical Operators

Learn: - `and` - `or` - `not`

Exercise: Check whether the player has a lantern and enough energy to
light the lighthouse.

Checkpoint: You can combine multiple conditions.

## Phase 3: Loops

### Step 7 --- While Loops

Learn: - `while` - Loop conditions - Infinite loops

Exercise: Create a menu that keeps appearing until the player chooses to
quit.

Checkpoint: You understand why a game needs a loop.

### Step 8 --- Break and Continue

Learn: - `break` - `continue`

Exercise: Create a shop menu that keeps running until the player chooses
to leave.

Checkpoint: You understand how to exit a loop correctly.

## Phase 4: Data Structures

### Step 9 --- Lists

Learn: - Creating lists - Adding items with `append()` - Checking
whether an item exists - Removing items

Exercise: Create an inventory containing Rope and Lantern.

Checkpoint: You can add and display items.

### Step 10 --- Dictionaries

Learn: - Dictionary keys - Dictionary values - Accessing values -
Updating values

Exercise: Create a player dictionary with name, location, coins, energy,
lives, and inventory.

Checkpoint: You can explain how the player's information is stored.

## Phase 5: Functions

### Step 11 --- Creating Functions

Learn: - `def` - Function names - Function calls

Exercise: Create a function that displays the player's inventory.

Checkpoint: You can create and call a function.

### Step 12 --- Parameters and Arguments

Learn: - Parameters - Arguments - Passing information into functions

Exercise: Create a shop function that receives the player dictionary.

Checkpoint: You understand why `show_shop(player)` is different from
`show_shop()`.

### Step 13 --- Return Values

Learn: - `return` - Returning `True` or `False` - Using returned values

Exercise: Create a function that checks whether the player has won.

Checkpoint: You can use a function's result in another part of the
program.

## Phase 6: Build the Game

### Step 14 --- Create the Player

File: `features/player.py`

Learn: Functions, dictionaries, input, and return values.

Task: Create the player and initialize all player attributes.

### Step 15 --- Build the Main Menu

File: `main.py`

Learn: While loops, if/elif/else, and function calls.

Task: Create the main menu.

### Step 16 --- Build the Inventory

File: `features/inventory.py`

Learn: Lists, dictionaries, and functions.

Task: Allow the player to collect and view items.

### Step 17 --- Build the Coin System

File: `features/coins.py`

Learn: Arithmetic operators, boolean flags, and updating dictionary
values.

Task: Allow the player to collect coins only once.

### Step 18 --- Build the Energy System

File: `features/energy.py`

Learn: Conditions, arithmetic, and return values.

Task: Allow the player to use energy and collect an energy crystal.

### Step 19 --- Build the Locations

File: `features/locations.py`

Learn: Conditional statements, functions, dictionary updates, and game
state management.

Task: Create the five island locations and their travel options.

### Step 20 --- Build the Lighthouse

File: `features/lighthouse.py`

Learn: Multiple conditions and boolean return values.

Task: Allow the player to light the lighthouse beacon.

### Step 21 --- Build the Shop

File: `features/shop.py`

Learn: While loops, if/elif/else, dictionaries, arithmetic, and function
parameters.

Task: Allow the player to purchase items using coins.

### Step 22 --- Build the Life System

Learn: Conditions, arithmetic, and game state management.

Task: Deduct lives when energy runs out and end the game when lives
reach zero.

### Step 23 --- Add Colors

File: `colors.py`

Learn: Modules, imports, and ANSI terminal colors.

Task: Make the game colorful and easier to read.

------------------------------------------------------------------------

# 4. Project Folder Structure

The final project should be organized like this:

``` text
mystery-island/
├── main.py
├── colors.py
├── README.md
└── features/
    ├── __init__.py
    ├── player.py
    ├── coins.py
    ├── inventory.py
    ├── energy.py
    ├── locations.py
    ├── lighthouse.py
    └── shop.py
```

  File              Responsibility
  ----------------- --------------------------------
  `main.py`         Controls the main game loop
  `colors.py`       Stores terminal colors
  `player.py`       Creates the player
  `coins.py`        Handles coin collection
  `inventory.py`    Handles inventory items
  `energy.py`       Handles energy
  `locations.py`    Handles exploration and travel
  `lighthouse.py`   Handles the winning condition
  `shop.py`         Handles purchases

------------------------------------------------------------------------

# 5. How to Run the Application

This project runs on Python 3 and can be executed using the Ubuntu
terminal.

## Requirements

-   Ubuntu Linux
-   Python 3
-   Visual Studio Code (recommended)
-   A terminal

## Step 1 --- Check Python Installation

Open your terminal and run:

``` bash
python3 --version
```

Example output:

``` text
Python 3.12.3
```

If Python is not installed, install it:

``` bash
sudo apt update
sudo apt install python3
```

## Step 2 --- Navigate to the Project Folder

The project folder in the current development environment is named
`-mystery-island`.

Run:

``` bash
cd ~/ -mystery-island
```

If that command gives an error because of the space, use this exact
command instead:

``` bash
cd ~/-mystery-island
```

Confirm your location:

``` bash
pwd
```

Expected output may look like:

``` text
/home/student/-mystery-island
```

## Step 3 --- Check Project Files

Run:

``` bash
ls
```

You should see files similar to:

``` text
main.py
colors.py
features
README.md
```

## Step 4 --- Run the Application

Start the game:

``` bash
python3 main.py
```

The game should ask:

``` text
What is your name, adventurer?
```

Enter your name and press Enter. The main menu will then appear.

## Step 5 --- Play the Game

The main menu should display:

``` text
================================
       MYSTERY ISLAND
    THE LOST LIGHTHOUSE
================================

1. Explore the island
2. View inventory
3. View instructions
4. Visit Shop
5. Quit game

Choose an option:
```

Enter the number of the option you want.

## Step 6 --- Stop the Application

To quit normally, select:

``` text
5. Quit game
```

To stop the application manually, press:

``` text
Ctrl + C
```

## Step 7 --- Run After Making Changes

Whenever you modify the code:

1.  Save the file in VS Code.
2.  Return to the terminal.
3.  Run:

``` bash
python3 main.py
```

Python will execute the latest saved version.

## Quick Start

Use these commands to launch the game:

``` bash
cd ~/-mystery-island
python3 main.py
```

------------------------------------------------------------------------

# 6. How to Learn Each Feature

For every feature, follow this learning process:

1.  **Understand:** Learn what the feature does and why the game needs
    it.
2.  **Plan:** Write the logic in simple English.
3.  **Attempt:** Write the Python code yourself.
4.  **Review:** Check the code for mistakes.
5.  **Test:** Run the game in the terminal.
6.  **Debug:** Understand the error before fixing it.
7.  **Explain:** Explain in your own words how the code works.
8.  **Continue:** Move to the next feature only when you understand the
    current one.

------------------------------------------------------------------------

# 7. Testing Checklist

Before considering the project complete, test these situations:

-   [ ] Player can enter their name.
-   [ ] Main menu displays correctly.
-   [ ] Invalid menu choices are handled.
-   [ ] Player can explore all five locations.
-   [ ] Player cannot cross the bridge without Rope.
-   [ ] Player cannot light the lighthouse without Lantern.
-   [ ] Coins are collected only once.
-   [ ] Special items are collected only once.
-   [ ] Energy decreases correctly.
-   [ ] Lives decrease correctly.
-   [ ] Player can visit the shop.
-   [ ] Player can leave the shop.
-   [ ] Player cannot buy an item without enough coins.
-   [ ] Coins are deducted after successful purchases.
-   [ ] Purchased items are added to the player's inventory.
-   [ ] Player can win the game.
-   [ ] Player can lose the game.
-   [ ] Player can quit the game.

------------------------------------------------------------------------

# 8. Important Learning Rules

1.  Do not copy code without understanding it.
2.  Write one feature at a time.
3.  Test every feature before continuing.
4.  Ask questions whenever you are confused.
5.  Understand indentation.
6.  Learn to read error messages.
7.  Keep functions small and focused.
8.  Do not be afraid of making mistakes.
9.  Explain what you learned after each feature.
10. Build the project yourself with guidance.

------------------------------------------------------------------------

# 9. Final Goal

By the end of this project, you should be able to:

-   Build a Python application from scratch.
-   Organize code into modules.
-   Use functions to avoid repeating code.
-   Work with lists and dictionaries.
-   Manage a program using loops and conditions.
-   Debug common Python errors.
-   Explain how your game works without depending on AI to write every
    line.

**The goal is not just to finish Mystery Island. The goal is to become a
Python programmer who understands the code they write.**
