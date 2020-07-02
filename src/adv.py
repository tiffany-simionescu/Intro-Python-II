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

print(f"Hi {player.name}! Current Room: {player.current_room.name}")
print(room['outside'].description)
print("It looks like there might be some items. Press 'G' to find out!")

# Created Item
map = Item("map", "With this map, you can easily find your way and see what items are near you!")
room["outside"].add_item(map)

gem = Item("ruby", "Useful for wizards and to enhance certain items.")
room["treasure"].add_item(gem)

sword = Item("sword", "This particular sword can cut through diamonds!")
room["foyer"].add_item(sword)

while True:
    direction = input(
    'Where to next? \n  N (north), S (south), E (east), W (west), G (Get Item), D (Drop Item), I (inventory), Q (quit): ').lower().strip()
    print(direction)

    # N-S-E-W == Directions
    if direction in ["n", "s", "e", "w"]:
        current_room = player.current_room
        next_room = getattr(current_room, f"{direction}_to")

        if next_room is not None:
            player.current_room = next_room
            print(f"You have enetered the {player.current_room}")

            if current_room.items:
                print("It looks like this room has the following items: ")
                for item in player.current_room.items:
                    print(f"{item}")
                print("If you want to get these items, press 'G'")

        else:
            print("There's nothing in that direction.")

    # G == Get Item
    elif direction == "g":
        if not player.current_room.items:
            print("It looks like there are no items in the room. Let's keep going!")

        else:
            for item in player.current_room.items:
                player.pickup(item)
                # player.current_room.remove_item(item)
                print(f"Congradulations! You found the following:\n {item}")

    # D == Drop Item
    elif direction == "d":
        if player.inventory:
            drop_item = input("Which of the following items would you like to drop? ")
            for item in player.inventory:
                if item.name == drop_item:
                    player.inventory.remove(item)
                    print("The item was successfully removed.")
        elif item.name != drop_item:
            print("It doesn't look like you have that item.")
        else:
            print(f"It looks like {player.name} doesn't haven anything in their inventory.")
    
    # I == Inventory
    elif direction == "i":
        if player.inventory:
            print(f"{player.name} has the following in their inventory: ")
            for items in player.inventory:
                print(f"{items}")
        else:
            print(f"It looks like {player.name} doesn't haven anything in their inventory.")

    # Q == Quit
    elif direction == "q":
        print("See you later!")
        exit()

    # Not a valid entry
    else:
        print("Don't give up! Let's keep going!")