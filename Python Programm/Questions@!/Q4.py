# wap to remove duplicate from the list

def remove_duplicates(input_list):
    # Using a dictionary to remove duplicates while preserving order
    return list(dict.fromkeys(input_list))

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("List after removing duplicates:", unique_list)