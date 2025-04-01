new = {
    "no": 1,
    "name": "arpit",
    "age": 27,
}

# Function to find key by value
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found

# Example usage
key_for_value = get_key_by_value(new, "arpit")
print(key_for_value)  # Output: name

