# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}: {self.current_room}"

    def __repr__(self):
        return f"self.name = {self.name} : self.current_room = {self.current_room}"

    # def get_item(self, item):
    #     # self.current_room.remove_item(item)
    #     # self.items.append(item)
    #     # return f"Congradulations! You picked up the {item.name}"
    #     if item in self.current_room.items:
    #         self.inventory.append(item)
    #         print(f"Congradulations! You have the {item.name}!")
    def pickup(self, item):
        self.inventory.append(item)
        # if item in self.current_room.items:
        #     self.inventory.append(item)
        # else:
        #     print("The item is not in the room")

    def dropped_item(self, item_name):
        for i in self.inventory:
            if i.name == item_name:
                self.inventory.remove(i)
                return True
        return False

    def list_inventory(self):
        if len(self.inventory) < 1:
            print("You have no inventory.")
        for item in self.inventory:
            print(f"{item.name}: {item.description}")