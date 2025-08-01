# File I/O
# Writing to a file
with open("my_file.txt", "w") as file:
    file.write("Hello, Python learners!\n")
    file.write("This is a new line.\n")

# Reading from a file
with open("my_file.txt", "r") as file:
    content = file.read()
    print("--- File Content ---")
    print(content)
    print("--------------------")

# Appending to a file
with open("my_file.txt", "a") as file:
    file.write("This line was appended.\n")

with open("my_file.txt", "r") as file:
    lines = file.readlines()
    print("--- Lines in File ---")
    for line in lines:
        print(line.strip())  # .strip() removes newline characters
    print("--------------------")