
# =====================================================
# PYTHON DICTIONARY AND LOOPS - COMPLETE SINGLE FILE
# =====================================================

print("=" * 50)
print("PYTHON DICTIONARY AND LOOPS")
print("=" * 50)

# 1. Creating a dictionary
student = {
    "name": "Akash",
    "age": 24,
    "course": "Python",
    "marks": 85
}

print("\n1. CREATE DICTIONARY")
print(student)

# 2. Accessing values
print("\n2. ACCESS VALUES")
print("Name:", student["name"])
print("Age:", student.get("age"))
print("City:", student.get("city", "Not Available"))

# 3. Adding and updating values
print("\n3. ADD AND UPDATE")
student["city"] = "Mumbai"
student["marks"] = 95
print(student)

# 4. Removing elements
print("\n4. REMOVE ELEMENTS")
temp = student.copy()
print("pop():", temp.pop("city"))
print("After pop:", temp)

print("popitem():", temp.popitem())
print("After popitem:", temp)

# 5. Loop through keys
print("\n5. LOOP THROUGH KEYS")
for key in student:
    print(key)

# 6. Loop through values
print("\n6. LOOP THROUGH VALUES")
for value in student.values():
    print(value)

# 7. Loop through keys and values
print("\n7. LOOP THROUGH ITEMS")
for key, value in student.items():
    print(key, ":", value)

# 8. Dictionary length
print("\n8. LENGTH")
print("Length:", len(student))

# 9. Check whether a key exists
print("\n9. CHECK KEY")
if "name" in student:
    print("Name key exists")

if "salary" not in student:
    print("Salary key does not exist")

# 10. While loop
print("\n10. WHILE LOOP")
keys = list(student.keys())
i = 0

while i < len(keys):
    key = keys[i]
    print(key, ":", student[key])
    i += 1

# 11. enumerate()
print("\n11. ENUMERATE")
for index, (key, value) in enumerate(student.items(), start=1):
    print(index, key, "=", value)

# 12. Dictionary methods
print("\n12. DICTIONARY METHODS")
data = {"a": 10, "b": 20}

print("keys():", list(data.keys()))
print("values():", list(data.values()))
print("items():", list(data.items()))
print("get():", data.get("a"))
print("copy():", data.copy())

data.setdefault("c", 30)
print("setdefault():", data)

data.update({"b": 50, "d": 40})
print("update():", data)

# 13. fromkeys()
print("\n13. FROMKEYS")
keys_list = ["name", "age", "city"]
new_dict = dict.fromkeys(keys_list, "Unknown")
print(new_dict)

# 14. Nested dictionary
print("\n14. NESTED DICTIONARY")
students = {
    1: {"name": "Akash", "marks": 85},
    2: {"name": "Rahul", "marks": 92},
    3: {"name": "Priya", "marks": 78}
}

for roll_no, details in students.items():
    print(
        "Roll:", roll_no,
        "| Name:", details["name"],
        "| Marks:", details["marks"]
    )

# Access a nested value
print("First student:", students[1]["name"])

# 15. Dictionary comprehension
print("\n15. DICTIONARY COMPREHENSION")
squares = {x: x ** 2 for x in range(1, 6)}
print("Squares:", squares)

# 16. Filter dictionary using a loop
print("\n16. FILTER MARKS >= 80")
for roll_no, details in students.items():
    if details["marks"] >= 80:
        print(details["name"], details["marks"])

# 17. Count frequency using a dictionary
print("\n17. FREQUENCY COUNTER")
fruits = [
    "apple", "banana", "apple",
    "orange", "banana", "apple"
]

frequency = {}

for fruit in fruits:
    frequency[fruit] = frequency.get(fruit, 0) + 1

print(frequency)

# 18. Calculate total and average
print("\n18. TOTAL AND AVERAGE")
marks = {
    "Math": 80,
    "Python": 90,
    "English": 75
}

total = 0

for mark in marks.values():
    total += mark

average = total / len(marks)

print("Total:", total)
print("Average:", average)

# 19. Find maximum and minimum
print("\n19. MAXIMUM AND MINIMUM")
scores = {
    "Akash": 95,
    "Rahul": 75,
    "Priya": 85
}

print("Highest:", max(scores.values()))
print("Lowest:", min(scores.values()))

topper = max(scores, key=scores.get)
print("Topper:", topper, scores[topper])

# 20. Sort dictionary by keys
print("\n20. SORT BY KEYS")
for name in sorted(scores):
    print(name, ":", scores[name])

# 21. Sort dictionary by values
print("\n21. SORT BY VALUES")
sorted_scores = dict(
    sorted(scores.items(), key=lambda item: item[1])
)
print(sorted_scores)

# 22. Merge dictionaries
print("\n22. MERGE DICTIONARIES")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}
print(merged)

# 23. Reverse keys and values
print("\n23. REVERSE DICTIONARY")
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {
    value: key for key, value in original.items()
}
print(reversed_dict)

# 24. Remove all elements
print("\n24. CLEAR DICTIONARY")
temp = {"x": 1, "y": 2}
temp.clear()
print(temp)

# 25. Loop with a condition
print("\n25. EVEN AND ODD VALUES")
numbers = {
    "first": 10,
    "second": 15,
    "third": 20,
    "fourth": 25
}

for key, value in numbers.items():
    if value % 2 == 0:
        print(key, value, "is Even")
    else:
        print(key, value, "is Odd")

# 26. Build a dictionary from a loop
print("\n26. BUILD DICTIONARY USING LOOP")
number_squares = {}

for number in range(1, 6):
    number_squares[number] = number ** 2

print(number_squares)

# 27. Loop through a list of dictionaries
print("\n27. LIST OF DICTIONARIES")
employees = [
    {"name": "Amit", "salary": 30000},
    {"name": "Neha", "salary": 40000},
    {"name": "Ravi", "salary": 35000}
]

for employee in employees:
    print(
        employee["name"],
        "earns",
        employee["salary"]
    )

# 28. Dictionary membership
print("\n28. MEMBERSHIP")
person = {"name": "Akash", "city": "Mumbai"}

print("'name' in person:", "name" in person)
print("'age' in person:", "age" in person)
print("'Akash' in values:", "Akash" in person.values())

# 29. Dictionary unpacking
print("\n29. DICTIONARY UNPACKING")
first = {"a": 1, "b": 2}
second = {"b": 20, "c": 3}

combined = {**first, **second}
print(combined)  # second dictionary overrides b

# 30. Final summary
print("\n" + "=" * 50)
print("ALL DICTIONARY AND LOOP EXAMPLES COMPLETED")
print("=" * 50)
