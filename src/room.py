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

    def __str__(self):
        output = ""
        if self.n_to:
            output += "To the north is the " + self.n_to.name + '\n'
        if self.e_to:
            output += "To the east is the " + self.e_to.name + '\n'
        if self.s_to:
            output += "To the south is the " + self.s_to.name + '\n'
        if self.w_to:
            output += "To the west is the " + self.w_to.name + '\n'

        return output

    def __repr__(self):
        return f"self.name = {self.name} : self.description = {self.description}"

    def print_items(self):
        if len(self.items) > 0:
            print('This room has the following items:')
            for i in self.items:
                print(f'{i.name} - {i.description}')
        else:
            print("There doesn't appear to be any items in this room.")
            
    def search_items(self, item):
        for i in self.items:
            if i.name.lower() == item:
                return i
        else:   
            print("That item is not in this room. Let's keep searching...")
            self.print_items()

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)