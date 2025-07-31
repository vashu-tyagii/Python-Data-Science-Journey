# Loops
# For loop
for i in range(5):  # range(5) generates 0, 1, 2, 3, 4
    print(f"For loop iteration: {i}")

# While loop
count = 0
while count < 3:
    print(f"While loop iteration: {count}")
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue  # Skip to the next iteration
    if i == 7:
        break  # Exit the loop
    print(f"Current number: {i}")