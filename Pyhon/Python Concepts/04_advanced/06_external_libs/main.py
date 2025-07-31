# main.py
import requests

try:
    response = requests.get("https://api.github.com/users/octocat")
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    print(f"GitHub Octocat Name: {data['name']}")
    print(f"GitHub Octocat Bio: {data['bio']}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

# You could also use numpy/pandas for data manipulation
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Numpy array sum: {np.sum(arr)}")