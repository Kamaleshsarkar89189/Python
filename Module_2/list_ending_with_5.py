num_list = []
n = int(input("Enter the number of elements you want to input: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    num_list.append(element)

count = 0

for num in num_list:
    if num % 10 == 5:
        count += 1

print(f"Number of integers ending with 5: {count}")
