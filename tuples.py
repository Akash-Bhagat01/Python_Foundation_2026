# ==========================================
# PYTHON TUPLE - ALL FUNCTIONS & OPERATIONS
# ==========================================

t = (10, 20, 30, 20, 40, 50)

print("Original Tuple:", t)
# 1. len() - number of elements
print("1. len():", len(t))
# 2. count() - count an element
print("2. count():", t.count(20))
# 3. index() - position of an element
print("3. index():", t.index(30))
# 4. min() - smallest value
print("4. min():", min(t))
# 5. max() - largest value
print("5. max():", max(t))
# 6. sum() - total of values
print("6. sum():", sum(t))
# 7. sorted() - sort tuple
print("7. sorted():", sorted(t))
# Convert sorted list back to tuple
print("   Sorted Tuple:", tuple(sorted(t)))
# 8. tuple() - convert another iterable to tuple
my_list = [1, 2, 3, 4, 5]
new_tuple = tuple(my_list)
print("8. tuple():", new_tuple)
# 9. list() - convert tuple to list
my_list = list(t)
print("9. list():", my_list)

# 10. any() - True if at least one value is True
values = (0, 0, 10, 0)
print("10. any():", any(values))
# 11. all() - True if all values are True
values = (1, 2, 1, 2)
print("11. all():", all(values))
# 12. reversed() - reverse tuple
print("12. reversed():", tuple(reversed(t)))
# 13. enumerate() - index + value
print("13. enumerate():")
for index, value in enumerate(t):
    print(index, value)
# for i in t:
#     print(i)
# 14. zip() - combine tuples
names = ("Akash", "Rahul", "Priya")
marks = (85, 90, 95)
sub = ("math", "sci", "eng")

print("14. zip():")
for name, mark,s in zip(names, marks,sub):
    print(name, mark,s)
# 15. abs() - absolute value
numbers = (-10, -20, 30)
print("15. abs():", tuple(abs(x) for x in numbers))
# 16. pow() - power
numbers = (2, 3, 4)
print("16. pow():", tuple(pow(x, 2) for x in numbers))


# 17. round() - rounding values
numbers = (10.456, 20.789, 30.123)

print("17. round():", tuple(round(x, 2) for x in numbers))


# ==========================================
# TUPLE OPERATIONS
# ==========================================
a = (1, 2, 3)
b = (4, 5, 6)
# 18. Indexing
print("18. Indexing:", a[0])
print("   Last:", a[-1])
# 19. Slicing
print("19. Slicing:", a[0:2])


# 20. Concatenation (+)
print("20. Concatenation:", a + b)
# 21. Repetition (*)
print("21. Repetition:", a * 3)
# 22. Membership - in
print("22. Membership:", 2 in a)
# 23. Membership - not in
print("23. Not in:", 10 not in a)
# 24. Comparison
x = (1, 2, 3)
y = (1, 2, 3)
print("24. Comparison:", x == y)
# 25. Tuple unpacking
student = ("Akash", 25, "Python")
name, age, course = student
print("25. Unpacking:")
print(name)
print(age)
print(course)
# 26. Extended unpacking
numbers = (10, 20, 30, 40, 50)
first, *middle, lb,last = numbers
print("26. Extended Unpacking:")
print("First:", first)
print("Middle:", middle)
print("lb:", lb)
print("Last:", last)


# 27. Nested tuple
students = (
    ("Akash", 85),
    ("Rahul", 90,("python","java")),
    ("Priya", 95)
)

print("27. Nested Tuple:", students)
print("Akash marks:", students[1][2][0])


# 28. Loop through tuple
print("28. Loop:")

for value in t:
    print(value)


# 29. Tuple comprehension using generator
numbers = (1, 2, 3, 4, 5)

squares = tuple(x * x for x in numbers)

print("29. Squares:", squares)
print("111 : ", numbers)

# 30. Delete tuple
temp = (1, 2, 3)

del temp

print("30. Tuple deleted successfully")