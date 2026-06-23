# ==========================================
# PYTHON FILE HANDLING - COMPLETE EXAMPLE
# ==========================================

import os
import json
import csv

print("=" * 50)
print("PYTHON FILE HANDLING DEMO")
print("=" * 50)

# ==========================================
# 1. CREATE & WRITE FILE
# ==========================================

print("\n1. CREATE & WRITE FILE")

with open("sample.txt", "w") as file:
    file.write("Hello Akash\n")
    file.write("Welcome to Python File Handling\n")
    file.write("Learning Python is fun!\n")

print("sample.txt created successfully")

# ==========================================
# 2. READ COMPLETE FILE
# ==========================================

print("\n2. READ COMPLETE FILE")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)

# ==========================================
# 3. READ LINE BY LINE
# ==========================================

print("\n3. READ LINE BY LINE")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# ==========================================
# 4. READ ALL LINES INTO LIST
# ==========================================

print("\n4. READ ALL LINES")

with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)

# ==========================================
# 5. APPEND DATA
# ==========================================

print("\n5. APPEND DATA")

with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

print("Data appended successfully")

# ==========================================
# 6. FILE EXISTS CHECK
# ==========================================

print("\n6. FILE EXISTS CHECK")

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist")

# ==========================================
# 7. FILE INFORMATION
# ==========================================

print("\n7. FILE INFORMATION")

if os.path.exists("sample.txt"):

    print("File Name :", os.path.basename("sample.txt"))
    print("File Size :", os.path.getsize("sample.txt"), "bytes")
    print("Absolute Path :", os.path.abspath("sample.txt"))

# ==========================================
# 8. RENAME FILE
# ==========================================

print("\n8. RENAME FILE")

if os.path.exists("sample.txt"):

    os.rename("sample.txt", "new_sample.txt")
    print("File renamed")

# ==========================================
# 9. READ RENAMED FILE
# ==========================================

print("\n9. READ RENAMED FILE")

with open("new_sample.txt", "r") as file:
    print(file.read())

# ==========================================
# 10. CSV WRITE
# ==========================================

print("\n10. CSV WRITE")

data = [
    ["ID", "Name", "City"],
    [1, "Akash", "Mumbai"],
    [2, "Rahul", "Pune"],
    [3, "Amit", "Delhi"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV Created")

# ==========================================
# 11. CSV READ
# ==========================================

print("\n11. CSV READ")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# ==========================================
# 12. JSON WRITE
# ==========================================

print("\n12. JSON WRITE")

person = {
    "id": 1,
    "name": "Akash",
    "city": "Mumbai",
    "skills": ["Python", "PHP", "Laravel"]
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

print("JSON Created")

# ==========================================
# 13. JSON READ
# ==========================================

print("\n13. JSON READ")

with open("person.json", "r") as file:
    data = json.load(file)

print(data)

# ==========================================
# 14. BINARY FILE WRITE
# ==========================================

print("\n14. BINARY FILE WRITE")

binary_data = bytes([65, 66, 67, 68, 69])

with open("binary.dat", "wb") as file:
    file.write(binary_data)

print("Binary file created")

# ==========================================
# 15. BINARY FILE READ
# ==========================================

print("\n15. BINARY FILE READ")

with open("binary.dat", "rb") as file:
    data = file.read()

print(data)

# ==========================================
# 16. EXCEPTION HANDLING
# ==========================================

print("\n16. EXCEPTION HANDLING")

try:

    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)

# ==========================================
# 17. DELETE FILE
# ==========================================

print("\n17. DELETE FILE")

if os.path.exists("binary.dat"):
    os.remove("binary.dat")
    print("binary.dat deleted")

# ==========================================
# 18. DIRECTORY LISTING
# ==========================================

print("\n18. DIRECTORY FILES")

files = os.listdir(".")

for file in files:
    print(file)

# ==========================================
# 19. SEEK & TELL
# ==========================================

print("\n19. SEEK & TELL")

with open("new_sample.txt", "r") as file:

    print("Position:", file.tell())

    file.seek(5)

    print("Position:", file.tell())

    print(file.read())

# ==========================================
# 20. BEST PRACTICE
# ==========================================

print("\n20. BEST PRACTICE")

try:
    with open("new_sample.txt", "r") as file:
        content = file.read()

    print("Read Success")

except Exception as e:
    print("Error:", e)

print("\nPROGRAM FINISHED")