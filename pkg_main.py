import pkg.calculator

print("Add = ",pkg.calculator.add(5, 3))
print("Subtract = ",pkg.calculator.subtract(5, 3))

from pkg.calculator import add
print(add(10, 20))