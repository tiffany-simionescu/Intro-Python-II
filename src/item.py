class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self, item):
        print(f'\nYou have successfully picked up the {self.name}')

    def on_drop(self, item):
        print(f'\nYou have dropped the {self.name}')