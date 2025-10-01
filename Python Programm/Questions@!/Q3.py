# Function to reverse a list in place without using built-in methods
def reverse_list_in_place(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        # Swap elements at left and right indices
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

# Example usage
my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print("Reversed list:", my_list)