class Bird:
    def fly(self):
        print("Bird can fly")
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
        
birds = [Sparrow(), Penguin()]
for bird in birds:
    bird.fly()
