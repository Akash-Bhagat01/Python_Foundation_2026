

# -----------------------------------------------------
# 1. SIMPLE FUNCTION (NO PARAMETER, NO RETURN)
# -----------------------------------------------------
def say_hello():
    print("Hello, Python!")

say_hello()
# Output: Hello, Python!


# -----------------------------------------------------
# 2. FUNCTION WITH PARAMETER
# -----------------------------------------------------
def greet(name):
    print("Hello,", name)

greet("Akash")
# Output: Hello, Akash


# -----------------------------------------------------
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# -----------------------------------------------------
def add(a, b):
    print("Addition:", a + b)

add(10, 20)
# Output: Addition: 30


# -----------------------------------------------------
# 4. FUNCTION WITH RETURN VALUE
# -----------------------------------------------------
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)
# Output: Multiplication: 20


# -----------------------------------------------------
# 5. DEFAULT ARGUMENT FUNCTION
# -----------------------------------------------------
def power(base, exp=2):
    return base ** exp

print("Power:", power(5))

print("Power:", power(5, 3))


# -----------------------------------------------------
# 6. KEYWORD ARGUMENT FUNCTION
# -----------------------------------------------------
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Rahul")
# Output:
# Name: Rahul
# Age: 21


# -----------------------------------------------------
# 7. VARIABLE LENGTH ARGUMENTS (*args)
# -----------------------------------------------------
def total_sum(*numbers):
    print("Sum:", min(numbers))

total_sum(10, 20, 30, 40)
# Output: Sum: 100


# -----------------------------------------------------
# 8. VARIABLE KEYWORD ARGUMENTS (**kwargs)
# -----------------------------------------------------
def employee(**data):
    for key, value in data.items():
        print(key, ":", value)

employee(name="Amit", role="Developer", salary=50000)
# Output:
# name : Amit
# role : Developer
# salary : 50000


# -----------------------------------------------------
# 9. FUNCTION INSIDE FUNCTION (NESTED FUNCTION)
# -----------------------------------------------------
def parent():
    def child():
        print("Inside child Function")
    child()

parent()
# Output: Inside Inner Function


# -----------------------------------------------------
# 10. LAMBDA FUNCTION
# -----------------------------------------------------
square = lambda x,y: x * x
print("Square:", square(6,2))
# Output: Square: 36


# -----------------------------------------------------
# 11. RECURSIVE FUNCTION
# -----------------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
# Output: Factorial: 120
