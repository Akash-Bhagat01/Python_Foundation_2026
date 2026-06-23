import os
with open("python.txt", "w") as file:
    file.write("Hello Akash\n")
    file.write("Welcome to Python File Handling\n")
    file.write("Learning Python is fun!\n")

if os.path.exists("sample111.txt"):
    print("File exists")
else:
    print("File does not exist")
    with open("sample111.txt", "w") as file:
        file.write("Hello Akash\n")
        file.write("Welcome to Python File Handling\n")
        file.write("Learning Python is fun!\n")


# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# with open("sample.txt", "a") as file:
#     file.write("This line was appended.\n")
