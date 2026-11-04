from colors import YELLOW, RESET


def create_player():

    player_name = input(YELLOW + "What is your name, adventurer? " + RESET)

    player = {
        "name": player_name,
        "location": "Beach",
        "coins": 0,
        "energy": 5,
        "inventory": [],
        "coins_collected": False,
        "rope_collected": False,
        "lantern_collected": False,
        "crystal_collected": False
    }

    return player