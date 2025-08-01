# Regular Expressions
import re

text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
match = re.search(r"fox", text)
if match:
    print(f"Pattern 'fox' found at index {match.start()} to {match.end()}")

# Find all occurrences
all_words = re.findall(r"\b\w+\b", text)  # Find all words
print(f"All words: {all_words}")

# Replace occurrences
new_text = re.sub(r"fox", "cat", text)
print(f"Text after replacement: {new_text}")

# Extracting numbers
numbers_text = "My phone is 123-456-7890 and my old one was 987-654-3210."
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", numbers_text)
print(f"Phone numbers found: {phone_numbers}")