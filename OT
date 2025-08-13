def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
user_input = input("Enter numbers separated by spaces or commas: ")
try:
    numbers = list(map(int, user_input.replace(',', ' ').split()))
    sorted_numbers = merge_sort(numbers)
    print("Sorted list:", sorted_numbers)
except ValueError:
    print("ERROR: Please enter only numbers separated by spaces or commas.")


// Another one
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]   
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
print("Original list:",numbers)
selection_sort(numbers)
print("Sorted list:",numbers)
