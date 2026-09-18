class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")


class Dog(Animal):
    pass


d1 = Dog("Rex")

d1.speak()
