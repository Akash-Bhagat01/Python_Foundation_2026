# =====================================================
# CLASSES AND OBJECTS IN PYTHON
# =====================================================

# -----------------------------------------------------
# 1. SIMPLE CLASS AND OBJECT
# -----------------------------------------------------
class Person:
    pass

p1 = Person()
print(p1)
# Output: <__main__.Person object at 0x...>


# -----------------------------------------------------
# 2. CLASS WITH ATTRIBUTES
# -----------------------------------------------------
class Student:
    name = "Akash"
    age = 22

s1 = Student()
print(s1.name)
# Output: Akash
print(s1.age)
# Output: 22


# -----------------------------------------------------
# 3. CLASS WITH METHOD
# -----------------------------------------------------
class Greeting:
    def say_hello(self):
        print("Hello from class")

g = Greeting()
g.say_hello()
# Output: Hello from class


# -----------------------------------------------------
# 4. __init__ CONSTRUCTOR
# -----------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Rahul", 50000)
print(e1.name)
# Output: Rahul
print(e1.salary)
# Output: 50000


# -----------------------------------------------------
# 5. MULTIPLE OBJECTS OF SAME CLASS
# -----------------------------------------------------
e2 = Employee("Amit", 60000)
print(e2.name, e2.salary)
# Output: Amit 60000


# -----------------------------------------------------
# 6. INSTANCE METHOD USING SELF
# -----------------------------------------------------
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()
print("Addition:", c.add(10, 20))
# Output: Addition: 30


# -----------------------------------------------------
# 7. CLASS VARIABLE
# -----------------------------------------------------
class Company:
    company_name = "TechSoft"

    def show(self):
        print(self.company_name)

emp1 = Company()
emp2 = Company()

emp1.show()
# Output: TechSoft
emp2.show()
# Output: TechSoft


# -----------------------------------------------------
# 8. INSTANCE VARIABLE
# -----------------------------------------------------
class User:
    def __init__(self, username):
        self.username = username

u1 = User("akash")
u2 = User("rahul")

print(u1.username)
# Output: akash
print(u2.username)
# Output: rahul


# -----------------------------------------------------
# 9. MODIFY INSTANCE VARIABLE
# -----------------------------------------------------
u1.username = "akash_bhagat"
print(u1.username)
# Output: akash_bhagat


# -----------------------------------------------------
# 10. INHERITANCE
# -----------------------------------------------------
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
# Output: Animal speaks
d.bark()
# Output: Dog barks


# -----------------------------------------------------
# 11. METHOD OVERRIDING
# -----------------------------------------------------
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()
# Output: Child method


# -----------------------------------------------------
# 12. ENCAPSULATION (PRIVATE VARIABLE)
# -----------------------------------------------------
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

b = Bank(10000)
print(b.get_balance())
# Output: 10000
# print(b.__balance)  ❌ Error (private)


# -----------------------------------------------------
# 13. POLYMORPHISM
# -----------------------------------------------------
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

# Output:
# Sparrow flies
# Penguin cannot fly



# -----------------------------------------------------
# 14. CLASS METHOD
# -----------------------------------------------------
class School:
    school_name = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school_name)

School.show_school()
# Output: ABC School


