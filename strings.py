# ============================================================
# PYTHON STRING
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Strings  with examples and output
# ============================================================

print("----- STRING CREATION -----")

s1 = 'Hello Python'
s2 = "World"
s3 = '''This is
a multi-line
gj
afkasj
string'''

print(s1)
print(s2)
print(s3)


print("\n----- STRING INDEXING -----")

text = "Python"
print(text[0])    # P
print(text[1])    # y
print(text[-1])   # n (last character)


print("\n----- STRING SLICING -----")

print(text[0:4])   # Pyth
print(text[:2])    # Py
print(text[2:])    # thon
print(text[::-1])  # Reverse string


print("\n----- STRING IMMUTABILITY -----")

# Strings cannot be changed
# text[0] = 'J'  # This will cause an error

new_text = "J" + text[1:]
print(new_text)


print("\n----- STRING CONCATENATION -----")

a = "Hello"
b = "Python"

print(a + " " + b)
print(a * 3)


print("\n----- STRING LENGTH -----")

msg = "Python"
print(len(msg))


print("\n----- STRING METHODS -----")

sample = "  hello python  "

print(sample.upper())
print(sample.lower())
print(sample.capitalize())
print(sample.title())
print("Strip() :"+sample.strip())
print(sample.replace("hello", "welcome"))
print(sample.count("o"))
print(sample.find("python"))
print(sample.startswith("  h"))
print(sample.endswith("  "))



print("\n----- STRING FORMATTING -----")

name = "Alice"
age = 25

# Old style
print("Name: %s, Age: %d" % (name, age))

# format()
print("Name: {}, Age: {}".format(name, age))

# f-string (recommended)
print(f"Name: {name}, Age: {age}")


print("\n----- ESCAPE CHARACTERS -----")

print("Hello\nWorld")
print("Hello\tWorld")
print("He said: \"Python is awesome\"")


print("\n----- STRING SPLIT AND JOIN -----")

sentence = "Python is very powerful"
words = sentence.split(" ")

print(words)
print("-".join(words))


print("\n----- LOOPING THROUGH STRING -----")

for char in "ABC":
    print(char)


print("\n----- MEMBERSHIP OPERATORS -----")

print("Py" in "Python")
print("Java" not in "Python")

