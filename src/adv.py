from room import Room
from player import Player
from item import Item

# Declare all the rooms

# Prefer this format in the future:
# outside = Room("outside", """Dim light filters in from...""")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# Prefer this format in the future:
# outside.n_to = foyer

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Commands for directions and actions
item_actions = ['get', 'take', 'drop']
directions = ['n', 'e', 's', 'w']

# Make a new player object that is currently in the 'outside' room.
player = Player("Tiffany", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# Created Item
map = Item("map", "With this map, you can easily find your way and see what items are near you!")
room["outside"].add_item(map)

### STRETCH - If you find the gem, you win ###
gem = Item("ruby", "Useful for wizards and to enhance certain items.")
room["treasure"].add_item(gem)

sword = Item("sword", "This particular sword can cut through diamonds!")
room["foyer"].add_item(sword)

# Rooms can hold more than one item:
staff = Item("staff", "A very powderful wizard's staff.")
room["foyer"].add_item(staff)


# Beginning of Game
print(f"\nHi {player.name}!\nCurrent Room: {player.current_room.name}\n")
print(room['outside'].description)
print("""\nIt looks like there's a map here. Type in 'get map' or 'take map' 
    to add the map to your inventory. To remove the item from your inventory, 
    type 'drop map'. Go ahead and try!\n""")

# While Loop for functionality
while True:
    # Player Input
    player_input = input(
    '\nWhat are you waiting for? Onward!\nN (north), S (south), E (east), W (west),\nget [ITEM], take [ITEM], drop [ITEM], I (inventory), Q (quit): ').lower().split(' ')

    # Player Input Error Handling
    if len(player_input) > 2 or len(player_input) < 1:
        print("Invalid entry. Please try again.")

    # Conditionals for actions
    elif len(player_input) == 2:
        if player_input[0] in item_actions:

            if player_input[0] == 'get' or player_input[0] == 'take':
                item = player.current_room.search_items(player_input[1])

                if item in player.current_room.items:
                    player.add_current_room_item(item)

                    ### STRETCH - If you find the gem, you win ###
                    if gem in player.inventory:
                        print("You win the game!\nFarewell!")
                        exit()
                else:
                    print("\nIt doesn't look like this item exist. Please try again...")

            elif player_input[0] == 'drop':
                item = player.search_items(player_input[1])
                if item in player.inventory:
                    player.remove_player_item(item)
                else:
                    print("\nYou don't have that item in your inventory.")

    else:
        # Conditionals for directions
        if player_input[0] in directions:
                try:
                    player.move_room(player_input[0])
                    print(f'\nYou are in the {player.current_room.name} - {player.current_room.description}\n')
                    print(player.current_room)
                    player.current_room.print_items()
                except AttributeError:
                    print("\nThere seems to be no room in that direction. Let's keep searching...")

        # Inventory
        elif player_input[0] == "i" or player_input[0] == "inventory":
            player.print_items()

        # Quit Game
        elif player_input[0] == "q":
            print("\nFarewell!")
            exit()

        # Error Handling for directionals
        else:
            print("\nDon't give up! Let's keep going!")