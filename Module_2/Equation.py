# b^2 - 4ac

import cmath
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*b)
print('the solution are {0} and {1}'.format(sol1,sol2))