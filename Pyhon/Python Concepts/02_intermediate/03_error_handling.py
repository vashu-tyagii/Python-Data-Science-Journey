# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except TypeError:
    print("Error: Type mismatch!")
else:
    print(f"Result: {result}")
finally:
    print("This block always executes.")


def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        return age
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


user_age = get_age()
if user_age is not None:
    print(f"You entered age: {user_age}")