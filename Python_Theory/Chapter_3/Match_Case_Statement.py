# Python - Match - Case Statament

# A python match-case statement takes an expression and compare its value to successive patterns gives as one or more case blocks. Only the first pattern that matches gets executed. It is also possible to extract components (sequence element or object attributes) from the value into variables.

        # match-case is similar to switch-case


# Example

def week(d):
    match d:
        case 0: return "Sunday"
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case _: return "Invalid day number"

print(week(3))
print(week(5))
print(week(7))

# Combined Cases in Match Statement

# Sometimes, there may be a situation where for more than one cases, a similar action has to be taken. For this, you can combine cases with OR operator represented by "|" symble.

# Example

def acces(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Limited access"
        case _: return "No access"
print(acces("manager"))
print(acces("Guest"))
print(acces("Kamalesh"))


# List as the Argument in Match Case Statement

def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time, *names]:
            message=''
            for name in names:
                message+=f'Good {time} {name}!\n'
            return message
        
print (greeting(["Morning", "Kamalesh"]))
print (greeting(["Afternoon", "Samalesh"]))
print (greeting(["Night", "Kamalesh", "Pallabi", "Piu"]))
