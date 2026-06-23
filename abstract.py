from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def test(self):
        print("test")
        
    def sound(self):
        print("Meow")
dog = Dog()
dog.sound()

cat = Cat()
cat.test()