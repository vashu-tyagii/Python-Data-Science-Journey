# Generators and Iterators
def count_up_to(max_num):  # type:ignore
    count = 1
    while count <= max_num:
        yield count  # Pauses execution and returns value
        count += 1


# Using the generator
my_generator = count_up_to(5)
print(next(my_generator))  # 1
print(next(my_generator))  # 2

for num in count_up_to(3):
    print(f"Generated: {num}")

# A simple iterator (conceptual)
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator)) # Would raise StopIteration