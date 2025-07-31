# Data Structures - Lists and Tuples
# Lists
my_list = [1, 2, 3, "apple", True]  # type: ignore
print(f"Original list: {my_list}")
my_list.append(4)  # type: ignore
print(f"List after append: {my_list}")
print(f"First element: {my_list[0]}")
my_list[0] = 100  # Lists are mutable
print(f"Modified list: {my_list}")

# Tuples
my_tuple = (10, 20, "banana")
print(f"Original tuple: {my_tuple}")
# my_tuple[0] = 50 # This would raise an error (tuples are immutable)
print(f"First element of tuple: {my_tuple[0]}")