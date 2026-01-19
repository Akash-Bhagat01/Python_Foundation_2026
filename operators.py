# ============================================================
# PYTHON OPERATORS
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Operators with examples and output
# ============================================================

a = 10
b = 3

print("----- ARITHMETIC OPERATORS -----")
print("Addition (a + b):", a + b)                 # 13
print("Subtraction (a - b):", a - b)              # 7
print("Multiplication (a * b):", a * b)           # 30
print("Division (a / b):", a / b)                 # 3.3333333333333335
print("Floor Division (a // b):", a // b)         # 3
print("Modulus (a % b):", a % b)                  # 1
print("Exponent (a ** b):", a ** b)               # 1000


print("\n----- COMPARISON OPERATORS -----")
print("Equal (a == b):", a == b)                   # False
print("Not Equal (a != b):", a != b)               # True
print("Greater Than (a > b):", a > b)              # True
print("Less Than (a < b):", a < b)                 # False
print("Greater or Equal (a >= b):", a >= b)        # True
print("Less or Equal (a <= b):", a <= b)           # False


print("\n----- LOGICAL OPERATORS -----")
print("AND (a > 5 and b < 5):", a > 5 and b < 5)   # True
print("OR (a > 5 or b > 5):", a > 5 or b > 5)      # True
print("NOT (not(a > b)):", not(a > b))             # False


print("\n----- ASSIGNMENT OPERATORS -----")
x = 5
print("Initial Value (x):", x)                     # 5

x += 2
print("Add & Assign (x += 2):", x)                 # 7

x -= 1
print("Subtract & Assign (x -= 1):", x)            # 6

x *= 2
print("Multiply & Assign (x *= 2):", x)            # 12

x /= 2
print("Divide & Assign (x /= 2):", x)              # 6.0


print("\n----- BITWISE OPERATORS -----")
print("AND (a & b):", a & b)                       # 2
print("OR (a | b):", a | b)                        # 11
print("XOR (a ^ b):", a ^ b)                       # 9
print("NOT (~a):", ~a)                             # -11
print("Left Shift (a << 1):", a << 1)              # 20
print("Right Shift (a >> 1):", a >> 1)             # 5


print("\n----- MEMBERSHIP OPERATORS -----")
lst = [1, 2, 3, 4, 5]
print("In (3 in list):", 3 in lst)                 # True
print("Not In (6 not in list):", 6 not in lst)     # True


print("\n----- IDENTITY OPERATORS -----")
p = 10
q = 10
print("Is (p is q):", p is q)                      # True
print("Is Not (p is not q):", p is not q)          # False
