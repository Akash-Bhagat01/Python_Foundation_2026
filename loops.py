# ============================================================
# PYTHON LOOPING STATEMENTS
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Looping Statements with examples and output
# ============================================================

# --------------------------------------------
# 1️⃣ FOR LOOP (Basic)
# --------------------------------------------
for i in range(1, 6):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5


# --------------------------------------------
# 2️⃣ FOR LOOP WITH LIST
# --------------------------------------------
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# mango


# --------------------------------------------
# 3️⃣ FOR LOOP WITH STRING
# --------------------------------------------
for ch in "PYTHON":
    print(ch)
# Output:
# P
# Y
# T
# H
# O
# N


# --------------------------------------------
# 4️⃣ WHILE LOOP
# --------------------------------------------
i = 1
while i <= 5:
    print(i)
    i += 1
# Output:
# 1
# 2
# 3
# 4
# 5


# --------------------------------------------
# 5️⃣ INFINITE LOOP (COMMENTED FOR SAFETY)
# --------------------------------------------
# while True:
#     print("Infinite Loop")


# --------------------------------------------
# 6️⃣ BREAK STATEMENT
# --------------------------------------------
for i in range(1, 6):
    if i == 4:
        break
    print(i)
# Output:
# 1
# 2
# 3


# --------------------------------------------
# 7️⃣ CONTINUE STATEMENT
# --------------------------------------------
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output:
# 1
# 2
# 4
# 5


# --------------------------------------------
# 8️⃣ PASS STATEMENT
# --------------------------------------------
for i in range(1, 4):
    if i == 2:
        pass   # does nothing
    print(i)
# Output:
# 1
# 2
# 3


# --------------------------------------------
# 9️⃣ NESTED LOOP
# --------------------------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


# --------------------------------------------
# 🔟 ELSE WITH FOR LOOP
# --------------------------------------------
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")
# Output:
# 1
# 2
# 3
# Loop completed


# --------------------------------------------
# 1️⃣1️⃣ ELSE WITH WHILE LOOP
# --------------------------------------------
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop completed")
# Output:
# 1
# 2
# 3
# While loop completed


# --------------------------------------------
# 1️⃣2️⃣ LOOP WITH USER INPUT (COMMENTED)
# --------------------------------------------
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i)
# Output depends on user input
