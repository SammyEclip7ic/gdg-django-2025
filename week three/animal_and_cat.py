class Animal:
    def make_sound(self):
        print("Animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meooow")

animal = Animal()
animal.make_sound()

cat = Cat()
cat.make_sound()
