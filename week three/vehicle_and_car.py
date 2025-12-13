class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Year: {self.year}")
    
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Model: {self.model}")

vehicle = Vehicle("BMW", 2010)
car = Car("Toyota", 2022, "Executive")

vehicle.info()
car.info()