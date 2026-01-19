# ============================================================
# PYTHON Variables
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Variables with examples and output
# ============================================================



# =========================================
# 1️⃣ VARIABLE DECLARATION & ASSIGNMENT
# =========================================

a = 10
print("Value of a:", a)                 # Value of a: 10
print("Type of a:", type(a))            # <class 'int'>


# =========================================
# 2️⃣ MULTIPLE ASSIGNMENT
# =========================================

x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)        # x: 1 y: 2 z: 3


# =========================================
# 3️⃣ SAME VALUE TO MULTIPLE VARIABLES
# =========================================

p = q = r = 100
print("p:", p, "q:", q, "r:", r)        # p: 100 q: 100 r: 100


# =========================================
# 4️⃣ DYNAMIC TYPING (Type can change)
# =========================================

var = 10
print("var:", var, type(var))           # 10 <class 'int'>

var = "Python"
print("var:", var, type(var))           # Python <class 'str'>


# =========================================
# 5️⃣ VARIABLE NAMING RULES (Valid)
# =========================================

my_name = "Akash"
_age = 22
marks123 = 85

print(my_name)                          # Akash
print(_age)                             # 22
print(marks123)                         # 85


# =========================================
# 6️⃣ VARIABLE NAMING (Invalid - COMMENTED)
# =========================================

# 1name = "Error"        ❌ Cannot start with number
# my-name = "Error"      ❌ Hyphen not allowed
# class = 10             ❌ Keyword not allowed


# =========================================
# 7️⃣ CASE SENSITIVITY
# =========================================

num = 10
Num = 20
print("num:", num)                      # num: 10
print("Num:", Num)                      # Num: 20


# =========================================
# 8️⃣ GLOBAL VARIABLE
# =========================================

g = 50

def show_global():
    print("Global variable g:", g)      # 50

show_global()


# =========================================
# 9️⃣ LOCAL VARIABLE
# =========================================

def local_example():
    l = 30
    print("Local variable l:", l)       # 30

local_example()

# print(l)  ❌ Error (l is local to function)


# =========================================
# 🔟 GLOBAL KEYWORD
# =========================================

count = 5

def modify_global():
    global count
    count = count + 1

modify_global()
print("Modified global count:", count)  # 6


# =========================================
# 1️⃣1️⃣ DELETING A VARIABLE
# =========================================

temp = 99
print("Before delete:", temp)           # 99
del temp
# print(temp)  ❌ NameError (variable deleted)


# =========================================
# 1️⃣2️⃣ VARIABLE MEMORY REFERENCE
# =========================================

a = 10
b = 10
print("a is b:", a is b)                 # True (same memory reference)


# =========================================
# 1️⃣3️⃣ INPUT USING VARIABLE
# =========================================

# name = input("Enter name: ")
# print("Hello", name)
# (Output depends on user input)


# =========================================
# 1️⃣4️⃣ CONSTANT (By Convention)
# =========================================

PI = 3.14159
print("PI value:", PI)                  # 3.14159
# PI = 3.14  ❌ Should not change (by convention)


# =========================================
# 1️⃣5️⃣ TYPE CASTING WITH VARIABLES
# =========================================

num_str = "100"
num_int = int(num_str)

print("String:", num_str, type(num_str))  # '100' <class 'str'>
print("Integer:", num_int, type(num_int)) # 100 <class 'int'>









































































































#ab