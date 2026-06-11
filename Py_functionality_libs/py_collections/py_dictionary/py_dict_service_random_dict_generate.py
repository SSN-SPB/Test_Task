import random
import string

# Function to generate a random dictionary with 5 elements
def generate_random_dict():
    """Generate a dictionary with 5 random key-value pairs."""
    random_dict = {}
    for _ in range(5):
        # Random key: 5-character string
        key = ''.join(random.choices(string.ascii_lowercase, k=5))
        # Random value: random integer between 1-100
        value = random.randint(1, 100)
        random_dict[key] = value
    return random_dict

# Generate three random dictionaries
dict1 = generate_random_dict()
dict2 = generate_random_dict()
dict3 = generate_random_dict()

# Display in console
print("Dictionary 1:")
print(dict1)
print("\nDictionary 2:")
print(dict2)
print("\nDictionary 3:")
print(dict3)