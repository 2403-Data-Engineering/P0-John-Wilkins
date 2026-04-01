from service import automobile_service
from data.models import Car, Truck, SUV

def display_auto(auto):
    print(f"  {auto.auto_year} {auto.auto_make} — ${auto.auto_price}")
    if isinstance(auto, Car):
        print(f"    Doors: {auto.auto_doors}")
    elif isinstance(auto, Truck):
        print(f"    Drivetrain: {auto.auto_drive_type}")
    elif isinstance(auto, SUV):
        print(f"    Capacity: {auto.auto_pass_cap}")

def show_all():
    autos = automobile_service.get_all()
    for auto in autos:
        display_auto(auto)

def add_vehicle():
    choice = input("1=Car  2=Truck  3=SUV: ").strip()
    make  = input("Make: ")
    year  = int(input("Year: "))
    price = int(input("Price: $"))
    if choice == "1":
        automobile_service.add_car(make, year, price, int(input("Doors: ")))
    elif choice == "2":
        automobile_service.add_truck(make, year, price, input("Drive type (4WD/FWD/RWD): "))
    elif choice == "3":
        automobile_service.add_suv(make, year, price, int(input("Passenger capacity: ")))
    else:
        print("Invalid option.")

def remove_vehicle():
    autos = automobile_service.get_all()
    for i, auto in enumerate(autos, 1):
        print(f"  {i}. {auto.auto_year} {auto.auto_make}")
    try:
        automobile_service.remove(int(input("Enter number to remove: ")) - 1)
        print("Removed.")
    except ValueError as e:
        print(e)

def filter_vehicles():
    field = "year" if input("1=Year  2=Price: ") == "1" else "price"
    asc   = input("1=Ascending  2=Descending: ") == "1"
    for auto in automobile_service.get_sorted(field, asc):
        display_auto(auto)

def run():
    options = {
        "1": ("Browse all vehicles", show_all),
        "2": ("Add a vehicle",       add_vehicle),
        "3": ("Remove a vehicle",    remove_vehicle),
        "4": ("Filter results",      filter_vehicles),
    }
    while True:
        print("\n**** Car Dealership ****")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        print("  5. Exit")
        choice = input("Choice: ").strip()
        if choice == "5":
            print("Goodbye!"); break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid option.")