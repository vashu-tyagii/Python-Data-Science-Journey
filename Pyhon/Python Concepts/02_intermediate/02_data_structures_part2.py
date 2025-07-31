# Data Structures - Dictionaries and Sets
# Dictionaries
my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # type: ignore
print(f"Original dict: {my_dict}")
print(f"Name: {my_dict['name']}")
my_dict["age"] = 26  # Dictionaries are mutable
my_dict["job"] = "Engineer"
print(f"Modified dict: {my_dict}")

# Sets
my_set = {1, 2, 3, 2, 1, 4}  # Duplicates are automatically removed
print(f"Original set: {my_set}")
my_set.add(5)
print(f"Set after adding 5: {my_set}")
print(f"Is 3 in set? {3 in my_set}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union: {set_a.union(set_b)}")
print(f"Intersection: {set_a.intersection(set_b)}")