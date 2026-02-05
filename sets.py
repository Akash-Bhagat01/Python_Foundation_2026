# ============================================
# SET & FROZENSET - 10 PRACTICAL EXAMPLES
# ============================================

# 1️⃣ Remove duplicates using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("1️⃣ Unique numbers:", unique_numbers)

# --------------------------------------------

# 2️⃣ Membership testing (fast lookup)
users = {"akash", "rahul", "neha"}
print("2️⃣ Is 'akash' present?", "akash" in users)

# --------------------------------------------

# 3️⃣ Union of two sets
A = {1, 2, 3}
B = {3, 4, 5}
print("3️⃣ Union:", A | B)

# --------------------------------------------

# 4️⃣ Intersection of two sets
print("4️⃣ Intersection:", A & B)

# --------------------------------------------

# 5️⃣ Difference of sets
print("5️⃣ Difference A-B:", A - B)

# --------------------------------------------

# 6️⃣ Set comprehension
squares = {x * x for x in range(1, 6)}
print("6️⃣ Squares set:", squares)

# --------------------------------------------

# 7️⃣ Frozen set (immutable set)
permissions = frozenset(["read", "write", "delete"])
print("7️⃣ Permissions (frozenset):", permissions)

# permissions.add("update")  ❌ Not allowed

# --------------------------------------------

# 8️⃣ Frozenset as dictionary key
role_access = {
    frozenset(["read"]): "Viewer",
    frozenset(["read", "write"]): "Editor",
    frozenset(["read", "write", "delete"]): "Admin"
}
print("8️⃣ Role access:", role_access)

# --------------------------------------------

# 9️⃣ Subset and superset checks
frontend = {"html", "css"}
fullstack = {"html", "css", "js", "python"}

print("9️⃣ Frontend ⊆ Fullstack:", frontend.issubset(fullstack))
print("   Fullstack ⊇ Frontend:", fullstack.issuperset(frontend))

# --------------------------------------------

# 🔟 Compare set vs frozenset behavior
mutable_set = {1, 2, 3}
immutable_set = frozenset([1, 2, 3])

mutable_set.add(4)  # ✅ Allowed
# immutable_set.add(4) ❌ Error

print("🔟 Mutable set:", mutable_set)
print("   Immutable frozenset:", immutable_set)

# --------------------------------------------

print("\n✅ ALL 10 SET & FROZENSET EXAMPLES COMPLETED!")
