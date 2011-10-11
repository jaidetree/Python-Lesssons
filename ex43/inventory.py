class Inventory(object):
    def __init__(self):
        self.inventory = {}

    def add_to_inventory(self, item_name, item_label):
        self.inventory[item_name] = item_label 

    def remove_from_inventory(self, item_name):
        if self.inventory[item_name]:
            del self.inventory[item_name]

        elif has_item(item_name):
            key = find_item_by_label(item_name)
            del self.inventory[key]

    def has_item(self, item_name):
        if item_name in self.inventory:
            return True
        else:
            return find_item_by_label(item_name) in self.inventory

    def find_item_by_label(self, label):
        for name, value in self.inventory.items():
            if value == label:
                return name
        return ''
