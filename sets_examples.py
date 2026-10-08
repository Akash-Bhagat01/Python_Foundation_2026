# 1. Create Set
a = {1, 2, 3, 4}
print(a)
# 2. Remove duplicates
a = {1, 2, 2, 3, 3, 4}
print(a)
# 3. Add
a.add(5)
print(a)
# 4. Remove
a.remove(5)
print(a)
# 5. Membership
print(3 in a)
# 6. Union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
# 7. Intersection
print(a & b)
# 8. Difference
print(a - b)
# 9. Symmetric Difference
print("symmetric: ",a ^ b)
# 10. Subset
a = {1, 2}
b = {1, 2, 3, 4}
print("a.issubset(b): ",a.issubset(b))

# 11. Remove duplicates from List
numbers = [1, 2, 2, 3, 3, 4]
print(set(numbers))

# 12. Find common skills
python = {"Python", "Django", "SQL"}
php = {"PHP", "Laravel", "SQL"}
test = {"Python", "Laravel", "SQL"}
print(python & php & test)
# 13. Frozenset
a = frozenset([1, 2, 3, 4])
print(a)

# 14. Frozenset cannot be changed
a = frozenset([1, 2, 3])
# a.add(4)       # Error

# But set operations work
b = frozenset([3, 4, 5])
print(a | b)

# 15. Frozenset as dictionary key
permissions = frozenset(["read", "write"])
data = {"Admin":permissions}

print(data)