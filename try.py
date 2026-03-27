class Dog:
    def sound(self):
        return "Woof, woof!"

class Cat:
    def sound(self):
        return "Meow, meow!"

def make_animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

for obj in [dog,cat]:
    obj.sound()
