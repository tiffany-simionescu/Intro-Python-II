# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        
    # def __str__(self):
    #     return f"{self.name}: {self.description}"
    def add_item(self, item):
        self.items.append(item)
        return self.items

    def remove_item(self, item):
        del self.items[item]

    def receive_item(self, item):
        self.items.append(item)

    def got_item(self, item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)
                return True
        return False

    def __str__(self):
        output = f"{self.name}: {self.description}\n"
        if self.n_to:
            output += "To the north is: " + self.n_to.name + '\n'
        if self.e_to:
            output += "To the east is: " + self.e_to.name + '\n'
        if self.s_to:
            output += "To the south is: " + self.s_to.name + '\n'
        if self.w_to:
            output += "To the west is: " + self.w_to.name + '\n'

        return output

    def __repr__(self):
        return f"self.name = {self.name} : self.description = {self.description}"