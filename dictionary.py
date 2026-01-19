# ============================================================
# PYTHON DICTIONARY
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : DICTIONARY  with examples and output
# ============================================================

# --------------------------------------------
# 1️⃣ CREATING A DICTIONARY
# --------------------------------------------
student = {"name": "Akash", "age": 22, "course": "Python"}
print("Dictionary:", student)
# Output: {'name': 'Akash', 'age': 22, 'course': 'Python'}


# --------------------------------------------
# 2️⃣ ACCESSING VALUES USING KEYS
# --------------------------------------------
print("Name:", student["name"])          # Akash
print("Age:", student.get("age"))        # 22


# --------------------------------------------
# 3️⃣ MODIFYING VALUE
# --------------------------------------------
student["age"] = 23
print("Updated age:", student["age"])
# Output: 23


# --------------------------------------------
# 4️⃣ ADDING NEW KEY-VALUE PAIR
# --------------------------------------------
student["city"] = "Mumbai"
print("After adding city:", student)
# Output: {'name': 'Akash', 'age': 23, 'course': 'Python', 'city': 'Mumbai'}


# --------------------------------------------
# 5️⃣ REMOVING ELEMENTS
# --------------------------------------------
student.pop("course")
print("After pop:", student)
# Output: {'name': 'Akash', 'age': 23, 'city': 'Mumbai'}

del student["city"]
print("After del:", student)
# Output: {'name': 'Akash', 'age': 23}


# --------------------------------------------
# 6️⃣ DICTIONARY KEYS, VALUES & ITEMS
# --------------------------------------------
print("Keys:", student.keys())
# Output: dict_keys(['name', 'age'])

print("Values:", student.values())
# Output: dict_values(['Akash', 23])

print("Items:", student.items())
# Output: dict_items([('name', 'Akash'), ('age', 23)])


# --------------------------------------------
# 7️⃣ LOOPING THROUGH DICTIONARY
# --------------------------------------------
for key in student:
    print(key, ":", student[key])
# Output:
# name : Akash
# age : 23


# --------------------------------------------
# 8️⃣ CHECK KEY EXISTENCE
# --------------------------------------------
print("name" in student)        # True
print("marks" not in student)  # True


# --------------------------------------------
# 9️⃣ DICTIONARY LENGTH
# --------------------------------------------
print("Length:", len(student))
# Output: 2


# --------------------------------------------
# 🔟 COPY DICTIONARY
# --------------------------------------------
student_copy = student.copy()
print("Copied dictionary:", student_copy)
# Output: {'name': 'Akash', 'age': 23}


# --------------------------------------------
# 1️⃣1️⃣ CLEAR DICTIONARY
# --------------------------------------------
student_copy.clear()
print("Cleared dictionary:", student_copy)
# Output: {}


# --------------------------------------------
# 1️⃣2️⃣ NESTED DICTIONARY
# --------------------------------------------
students = {
    "student1": {"name": "Amit", "age": 21},
    "student2": {"name": "Neha", "age": 22}
}
print("Nested dictionary:", students)
# Output: {'student1': {'name': 'Amit', 'age': 21}, 'student2': {'name': 'Neha', 'age': 22}}


# --------------------------------------------
# 1️⃣3️⃣ FROMKEYS METHOD
# --------------------------------------------
keys = ["id", "name", "marks"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys dictionary:", new_dict)
# Output: {'id': 0, 'name': 0, 'marks': 0}


# --------------------------------------------
# 1️⃣4️⃣ UPDATE METHOD
# --------------------------------------------
student.update({"marks": 85})
print("After update:", student)
# Output: {'name': 'Akash', 'age': 23, 'marks': 85}


# --------------------------------------------
# 1️⃣5️⃣ DICTIONARY WITH DIFFERENT DATA TYPES
# --------------------------------------------
info = {
    "id": 1,
    "name": "Python",
    "fees": 2500.50,
    "active": True
}
print("Mixed dictionary:", info)
# Output: {'id': 1, 'name': 'Python', 'fees': 2500.5, 'active': True}
