# ============================================================
# PYTHON DECISION MAKING
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Decision Making with examples and output
# ============================================================

# =========================================
# 1️⃣ SIMPLE IF STATEMENT
# =========================================

age = 20

if age >= 18:
    print("Eligible to vote")     # Eligible to vote
    if age >= 18:
     print("Eligible to vote")     # Eligible to vote


# =========================================
# 2️⃣ IF - ELSE STATEMENT
# =========================================

num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")           # Odd number


# =========================================
# 3️⃣ IF - ELIF - ELSE STATEMENT
# =========================================

marks = 65

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")          # First Class
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# =========================================
# 4️⃣ NESTED IF STATEMENT
# =========================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful") # Login successful
    else:
        print("Wrong password")
else:
    print("Invalid username")


# =========================================
# 5️⃣ LOGICAL OPERATORS IN DECISION MAKING
# =========================================

a = 10
b = 5

if a > 5 and b < 10:
    print("AND condition is True")    # AND condition is True

if a > 20 or b < 10:
    print("OR condition is True")     # OR condition is True

if not(a < b):
    print("NOT condition is True")    # NOT condition is True


# =========================================
# 6️⃣ RELATIONAL OPERATORS IN IF
# =========================================

x = 15
y = 20

if x != y:
    print("x is not equal to y")       # x is not equal to y


# =========================================
# 7️⃣ SHORT HAND IF (ONE-LINE IF)
# =========================================

n = 10
if n > 5: print("n is greater than 5") # n is greater than 5


# =========================================
# 8️⃣ SHORT HAND IF - ELSE (TERNARY OPERATOR)
# =========================================

p = 4
q = 6

print("p is greater") if p > q else print("q is greater")
# q is greater


# =========================================
# 9️⃣ DECISION MAKING WITH INPUT (EXAMPLE)
# =========================================

# user_age = int(input("Enter age: "))
# if user_age >= 18:
#     print("Adult")
# else:
#     print("Minor")
# Output depends on user input


# =========================================
# 🔟 PASS STATEMENT IN IF
# =========================================

value = 5

if value > 0:
    pass   # pass does nothing, used as placeholder

print("Program completed")            # Program completed
