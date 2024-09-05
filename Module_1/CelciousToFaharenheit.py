# Write a Python Program to calculate Celsious to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("Choose the conversion type:")
print("1) Celsius to Fahrenheit")
print("2) Fahrenheit to Celsius")
choice = input("Enter your choice (1/2 ): ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(celsius,"C is equal to ",fahrenheit,"F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(fahrenheit,"F is equal to ",celsius,"C")
else:
    print("Invalid choice! Please choose either '1' or '2'.")