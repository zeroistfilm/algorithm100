class Animal:
    def __init__(self, name):
        self.name= name
    def move(self):
        print("move")
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("bark")
class Duck(Animal):
    def speak(self):
        print("quack")

#
# dog = Dog('doggy')
# n = dog.name
# dog.move()
# dog.speak()

animals = [Dog('ddddooooggg'), Duck('dckdckdck')]
for animal in animals:
    animal.speak()