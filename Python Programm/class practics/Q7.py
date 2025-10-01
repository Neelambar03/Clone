class InvalidModeError(Exception):
    """Custom exception for invalid file modes."""
    pass

def get_file_mode():
    mode = input("Enter the file mode ('read', 'write', 'append'): ").strip().lower()
    if mode not in ['read', 'write', 'append']:
        raise InvalidModeError(f"Invalid mode: {mode}. Please enter 'read', 'write', or 'append'.")
    return mode

try:
    file_mode = get_file_mode()
    print(f"File mode selected: {file_mode}")
except InvalidModeError as e:
    print(e)