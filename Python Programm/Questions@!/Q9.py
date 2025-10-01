def key_with_highest_value(data):
    """
    This function takes a dictionary as input and returns the key with the highest value.
    If the dictionary is empty, it returns None.
    """
    if not data:
        return None
    return max(data, key=data.get)