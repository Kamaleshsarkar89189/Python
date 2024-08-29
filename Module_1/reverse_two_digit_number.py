def reverse_two_digit_numebr(number):
    if 10<=number<=99:
        reversed_number = (number % 10)* 10+(number//10)
        return reversed_number
    else:
        return"Please enter a valid number"
number = 42
reversed_number = reverse_two_digit_numebr(number)
print(f"The reversed number is : ", reversed_number)

    
    