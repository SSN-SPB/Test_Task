def find_key_path(data, target, path=None):
    if path is None:
        path = []

    # Case 1: Match found
    if data == target:
        return path

    # Case 2: Recursively search inside dictionaries
    if isinstance(data, dict):
        for key, value in data.items():
            result = find_key_path(value, target, path + [key])
            if result is not False:
                return result

    # Case 3: Recursively search inside lists
    elif isinstance(data, list):
        for index, item in enumerate(data):
            result = find_key_path(item, target, path + [index])
            if result is not False:
                return result

    # Case 4: Base case - target not found in this branch
    return False


# --- Example Usage ---

complex_json = {
    "company": "TechCorp",
    "departments": [
        {
            "name": "Engineering",
            "teams": [
                {"id": 101, "lead": "Alice"},
                {
                    "id": 102,
                    "lead": "Bob",
                    "projects": ["Alpha", "Beta", ["Y1", "Y2"]],
                },
            ],
        },
        {"name": "HR", "manager": "Carol"},
    ],
    "metadata": {"version": "1.0", "active": True},
}

# 1. Searching for a value deep inside nested lists and dicts
print(find_key_path(complex_json, "Beta"))
# Output: ['departments', 0, 'teams', 1, 'projects', 1]

# 1.2. Searching for a value that exist in nested list
print(find_key_path(complex_json, "Y2"))
# Output: ['departments', 0, 'teams', 1, 'projects', 2, 1]

# 2. Searching for a shallow value
print(find_key_path(complex_json, "TechCorp"))
# Output: ['company']

# 3. Searching for a value that doesn't exist
print(find_key_path(complex_json, "NonExistentValue"))
# Output: False

# 4. Searching for a value that exist in dictionary
print(find_key_path(complex_json, "Bob"))
# Output: ['departments', 0, 'teams', 1, 'lead']

# 5. Searching for a value that exist in dictionary
print(find_key_path(complex_json, 101))
# Output: ['departments', 0, 'teams', 1, 'lead']
