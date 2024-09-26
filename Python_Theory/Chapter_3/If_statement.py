# Python - if Statement

'''Let us consider an example of a customer entitled to 10% discount if his purchase amount is > 1000; if not, then no discount is applicable.'''

amount = int(input("Enter the amount: "))
discount = 0
if amount > 1000:
    discount = amount * 10 / 100
    
print("Amount = ", amount - discount)