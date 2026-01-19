# ============================================================
# PYTHON DATA TYPES
# Instructor : Akash Sir
# Course     : Python Programming (Foundation) 2026 
# Topic      : Data Types with examples and output
# ============================================================


# ==============================
# NUMERIC DATA TYPES
# ==============================

a = 10
print("Integer:", a)                 # Integer: 10
print("Type:", type(a))              # <class 'int'>

b = 3.14
print("Float:", b)                   # Float: 3.14
print("Type:", type(b))              # <class 'float'>

c = 2 + 3j
print("Complex:", c)                 # Complex: (2+3j)
print("Type:", type(c))              # <class 'complex'>


# ==============================
# TEXT DATA TYPE
# ==============================

name = "Python"
print("String:", name)               # String: Python
print("Type:", type(name))           # <class 'str'>


# ==============================
# SEQUENCE DATA TYPES
# ==============================

lst = [1, 2, 3]
print("List:", lst)                  # List: [1, 2, 3]
print("Type:", type(lst))            # <class 'list'>

tup = (10, 20, 30)
print("Tuple:", tup)                 # Tuple: (10, 20, 30)
print("Type:", type(tup))            # <class 'tuple'>

rng = range(1, 4)
print("Range:", list(rng))           # Range: [1, 2, 3]
print("Type:", type(rng))            # <class 'range'>


# ==============================
# SET DATA TYPES
# ==============================

st = {1, 2, 2, 3}
print("Set:", st)                    # Set: {1, 2, 3}
print("Type:", type(st))             # <class 'set'>

fst = frozenset([1, 2, 3])
print("Frozen Set:", fst)            # frozenset({1, 2, 3})
print("Type:", type(fst))            # <class 'frozenset'>


# ==============================
# MAPPING DATA TYPE
# ==============================

d = {"name": "Akash", "age": 22}
print("Dictionary:", d)              # {'name': 'Akash', 'age': 22}
print("Type:", type(d))              # <class 'dict'>


# ==============================
# BOOLEAN DATA TYPE
# ==============================

status = True
print("Boolean:", status)            # True
print("Type:", type(status))         # <class 'bool'>


# ==============================
# NONE DATA TYPE
# ==============================

result = None
print("None Value:", result)         # None
print("Type:", type(result))         # <class 'NoneType'>


# ==============================
# BINARY DATA TYPES
# ==============================

by = b"ABC"
print("Bytes:", by)                  # b'ABC'
print("Type:", type(by))             # <class 'bytes'>

ba = bytearray([65, 66, 67])
print("Bytearray:", ba)              # bytearray(b'ABC')
print("Type:", type(ba))             # <class 'bytearray'>

mv = memoryview(by)
print("Memoryview:", mv)             # <memory at 0x...>
print("Type:", type(mv))             # <class 'memoryview'>
