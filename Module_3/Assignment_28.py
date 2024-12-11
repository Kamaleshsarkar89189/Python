# Bubble sort in a user input list of integers.

def bubble_sort(int_list):
    n = len(int_list)
    for i in range(n):
        # Track whether a swap was made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
        # If no swaps were made, the list is already sorted
        if not swapped:
            break
    return int_list

# Input: List of integers from the user
user_input = input("Enter a list of integers separated by spaces: ")
int_list = list(map(int, user_input.split()))

# Call the function and display the result
sorted_list = bubble_sort(int_list)
print(f"Sorted list: {sorted_list}")
