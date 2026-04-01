class Automobile:
    def __init__(self, make, year, price):
        self.auto_make  = make
        self.auto_year  = year
        self.auto_price = price

class Car(Automobile):
    def __init__(self, make, year, price, doors):
        super().__init__(make, year, price)
        self.auto_doors = doors

class Truck(Automobile):
    def __init__(self, make, year, price, drive_type):
        super().__init__(make, year, price)
        self.auto_drive_type = drive_type

class SUV(Automobile):
    def __init__(self, make, year, price, pass_cap):
        super().__init__(make, year, price)
        self.auto_pass_cap = pass_cap