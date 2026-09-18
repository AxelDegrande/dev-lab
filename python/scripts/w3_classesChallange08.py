

class Cat:
    def sound(self):
        print(f"Meow!")


class Fox:
    def sound(self):
        print(f"Wa-pa-pa-pa-pow!")        

c1 = Cat()
f1 = Fox()

for animal in (c1, f1):
    animal.sound()