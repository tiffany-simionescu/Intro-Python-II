from item import Item

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}: {self.current_room}"

    def __repr__(self):
        return f"self.name = {self.name} : self.current_room = {self.current_room}"

    def move_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("\nThere's nothing over this way. Let's try a different direction.\n")
    
    def print_items(self):
        if len(self.inventory) > 0:
            print('Your current items:\n')
            for i in self.inventory:
                print(f'{i.name} - {i.description}')
        else:
            print('You have no items - explore the map to find some and add them to your collection!')

    def search_items(self, item):
        for i in self.inventory:
            if i.name.lower() == item:
                return i
            else:   
                return None

    def add_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def add_current_room_item(self, item):
        self.current_room.drop_item(item)
        self.add_item(item)
        item.on_take(item)

    def remove_player_item(self, item):
        self.current_room.add_item(item)
        self.drop_item(item)
        item.on_drop(item)