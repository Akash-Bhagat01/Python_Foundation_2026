# ==================================================
# PYTHON EXCEPTION HANDLING - COMPLETE SINGLE FILE
# ==================================================


print("\n🚀 Python Exception Handling Demo Started\n")
# This is the most common Python exception handling pattern used in real projects:
try:
    x = 10 / 0
except Exception as e:
    print("Type:", type(e))
    print("Message:", e)
    
 
# --------------------------------------------------
# 1️⃣ Basic try-except
# --------------------------------------------------
print(" Basic try-except")
try:
    x = int("abc")   # ValueError
except ValueError:
    print("Error: Cannot convert string to integer")

# --------------------------------------------------
# 2️⃣ Multiple except blocks
# --------------------------------------------------
print("\n Multiple except blocks")
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")

# --------------------------------------------------
# 3️⃣ Catch multiple exceptions together
# --------------------------------------------------
print("\n Catch multiple exceptions together")
try:
    data = int("hello")
except (ValueError, TypeError) as e:
    print("Caught error:", e)

# --------------------------------------------------
# 4️⃣ Using else block
# --------------------------------------------------
print("\n try-except-else")
try:
    num = int("100")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", num)

# --------------------------------------------------
# 5️⃣ Using finally block
# --------------------------------------------------
print("\n try-except-finally")
try:
    file = open("demo.txt", "w")
    file.write("Hello Python")
except IOError:
    print("File error")
finally:
    file.close()
    print("File closed (finally always runs)")

# --------------------------------------------------
# 6️⃣ Handling runtime errors
# --------------------------------------------------
print("\n Runtime error handling")
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range")

# --------------------------------------------------
# 7️⃣ Handling KeyError
# --------------------------------------------------
print("\n KeyError handling")
user = {"name": "Akash"}
try:
    print(user["Name"])
except KeyError:
    print("Error: Key not found")

# --------------------------------------------------
# 8️⃣ Raising custom exceptions
# --------------------------------------------------
print("\n Raising custom exceptions")
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

try:
    print(check_age(15))
except ValueError as e:
    print("Custom Error:", e)

# --------------------------------------------------
# 9️⃣ User-defined exception class
# --------------------------------------------------
print("\n User-defined exception class")

class BalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise BalanceError("Insufficient balance")
    return balance - amount

try:
    print(withdraw(5000, 7000))
except BalanceError as e:
    print("Bank Error:", e)

# --------------------------------------------------
# 🔟 Exception chaining
# --------------------------------------------------
print("\n Exception chaining")
try:
    try:
        int("xyz")
    except ValueError as e:
        raise RuntimeError("Conversion failed") from e
except RuntimeError as err:
    print("Final Error:", err)

# --------------------------------------------------
# 1️⃣1️⃣ Using assert
# --------------------------------------------------
print("\nUsing assert")
try:
    x = -5
    assert x > 0, "x must be positive"
except AssertionError as e:
    print("Assertion Error:", e)

# --------------------------------------------------
# 1️⃣2️⃣ Finally with return
# --------------------------------------------------
print("\n Finally with return")

def demo_finally():
    try:
        return "Try block"
    finally:
        print("Finally block executed")

print(demo_finally())

# --------------------------------------------------

print("\n ALL PYTHON EXCEPTION HANDLING CONCEPTS COVERED!")
