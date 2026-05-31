def create_inventory(items):
    r_list = {}
    for item in items:
        if item in r_list:
            r_list[item] += 1
        else:
            r_list[item] = 1       
    return r_list

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] < 0:
                inventory[item] = 0
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    return [(key, value) for key, value in inventory.items() if value > 0]