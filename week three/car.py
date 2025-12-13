class Car:
    def __init__(self, make):
        self.make = make
    
    def get_make(self):
        return self.make
    
car = Car("BMW")
make = car.get_make()
print(make)