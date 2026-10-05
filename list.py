# Python List - All Main Concepts

numbers = [10, 20, 30, 20, 40]

print("Original:", numbers)

# Indexing
print("First:", numbers[0])
print("Last:", numbers[-1])

# Change value
numbers[0] = 100
print("Change:", numbers)


# Add
numbers.append(50)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.extend([60, 70])
print("extend:", numbers)

# Remove
numbers.remove(20)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

# Slicing
print("Slice:", numbers[1:4])

# Functions
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Total:", sum(numbers))
print("Count of 20:", numbers.count(20))

# Index
print("Index of 40:", numbers.index(40))

# Sort
numbers.sort()
print("Sorted:", numbers)

# Reverse
numbers.reverse()
print("Reverse:", numbers)

# Check value
print("40 exists:", 40 in numbers)

# Copy
new_list = numbers.copy()
print("Copy:", new_list)

# Loop
print("Loop:")
for value in numbers:
    print(value)

# List comprehension
squares = [x * x for x in numbers]
print("Squares:", squares)

# Clear
new_list.clear()
print("After clear:", new_list)