import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data import automobile_repo
from data.models import Car, Truck, SUV
from presentation import menu

automobile_repo.seed_inventory([
    Car("BMW", 2020, 20000, 4),
    Car("Honda", 2005, 2000, 4),
    Car("Ford", 2012, 5000, 2),
    Truck("Toyota", 2021, 15000, "4WD"),
    Truck("Ford", 2010, 6000, "FWD"),
    Truck("Chevrolet", 2021, 15000, "RWD"),
    SUV("Tesla", 2024, 30000, 5),
    SUV("Nissan", 1995, 1500, 5),
    SUV("Hyundai", 2009, 6500, 5),
])

menu.run()