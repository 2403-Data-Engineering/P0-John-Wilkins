from data import automobile_repo
from data.models import Car, Truck, SUV

def get_all():
    return automobile_repo.get_all()

def add_car(make, year, price, doors):
    automobile_repo.add(Car(make, year, price, doors))

def add_truck(make, year, price, drive_type):
    automobile_repo.add(Truck(make, year, price, drive_type))

def add_suv(make, year, price, pass_cap):
    automobile_repo.add(SUV(make, year, price, pass_cap))

def remove(index):
    removed = automobile_repo.remove_by_index(index)
    if not removed:
        raise ValueError("Invalid selection.")

def get_sorted(by, ascending=True):
    if by == "year":
        return automobile_repo.get_sorted_by_year(ascending)
    elif by == "price":
        return automobile_repo.get_sorted_by_price(ascending)
    else:
        raise ValueError(f"Unknown sort field: {by}")