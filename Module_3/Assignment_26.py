# Take a string from user and find the number of vowel using function.

def count_vowels(user_input):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Count the number of vowels in the input
    return sum(1 for char in user_input if char in vowels)

# Get input from the user
user_string = input("Enter a string: ")

# Call the function and display the result
vowel_count = count_vowels(user_string)
print(f"The number of vowels in the string is: {vowel_count}")
