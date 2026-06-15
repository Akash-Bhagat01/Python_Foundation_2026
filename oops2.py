from abc import ABC, abstractmethod

# ==========================
# Abstract Class
# ==========================
class Person(ABC):

    def __init__(self, name, age):
        self.name = name          # Public Variable
        self._age = age           # Protected Variable
        self.__salary = 50000     # Private Variable

    # Encapsulation
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Concrete Method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")

    # Abstract Method
    @abstractmethod
    def work(self):
        pass


# ==========================
# Inheritance
# ==========================
class Employee(Person):

    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    # Method Overriding
    def work(self):
        print(f"{self.name} works in {self.department}")


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Method Overriding
    def work(self):
        print(f"{self.name} studies {self.course}")


# ==========================
# Polymorphism Function
# ==========================
def show_work(person):
    person.work()


# ==========================
# Main Program
# ==========================
if __name__ == "__main__":

    print("\n----- Employee -----")
    emp = Employee("Akash", 25, "IT")

    emp.display()
    emp.work()

    print("Salary:", emp.get_salary())

    emp.set_salary(75000)

    print("Updated Salary:", emp.get_salary())

    print("\n----- Student -----")
    stu = Student("Rahul", 20, "MCA")

    stu.display()
    stu.work()

    print("\n----- Polymorphism -----")

    people = [
        Employee("John", 30, "HR"),
        Student("Priya", 22, "BCA")
    ]

    for p in people:
        show_work(p)