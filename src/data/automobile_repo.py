# In a real app this would talk to a database.
# Here it manages the in-memory list — that's still the "data layer."

_inventory = []

def seed_inventory(items):
    _inventory.extend(items)

def get_all():
    return list(_inventory)

def add(automobile):
    _inventory.append(automobile)

def remove_by_index(index):
    if 0 <= index < len(_inventory):
        del _inventory[index]
        return True
    return False

def get_sorted_by_year(ascending=True):
    return sorted(_inventory, key=lambda a: a.auto_year, reverse=not ascending)

def get_sorted_by_price(ascending=True):
    return sorted(_inventory, key=lambda a: a.auto_price, reverse=not ascending)