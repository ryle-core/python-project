class animal:
    ismammal = True
    hasfur = True

class dog(animal):
    def bark(self):
        print("woof!! woof!!")

class cat(animal):
    def meow(self):
        print("meow! meow!")

d =dog()
d.bark()

c = cat()
c.meow()