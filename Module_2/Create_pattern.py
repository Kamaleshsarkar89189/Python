# Write a Python Script to create the following pattern
    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10
    # 11 12 13 14 15

def create_pattern():
    num = 1
    for i in range(1, 6):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()  # Move to the next line after each row

create_pattern()
