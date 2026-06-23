from abc import ABC, abstractmethod

class Parent(ABC):
    def show(self):
        print("Parent method")

    @abstractmethod    
    def abc(self):
        pass    

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")
    
# class Boy(Child):
#     def show(self):
#         super().show()
#         print("Boy method")
#     # 
c = Child()
c.show()
c.abc()