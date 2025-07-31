# Context Managers
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # type:ignore
        print("Exiting the context.")
        if exc_type:
            print(f"An exception occurred: {exc_type}: {exc_val}")
        return False  # Propagate the exception if it occurred

    def do_something(self):
        print("Doing something inside the context.")


with MyContextManager() as mcm:
    mcm.do_something()
    # raise ValueError("Something went wrong!") # Uncomment to see exception handling
print("Outside the context.")

# Using with for files (most common use case)
with open("another_file.txt", "w") as f:
    f.write("This is written using a context manager.")
print("File operations complete.")
