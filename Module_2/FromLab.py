n=int(input("Enter a number "))
k=0
if n<0 or n==0 :
    print("Enter the number gather than 0")
    exit()
else :
    for i in range(1,n+1) :
        k=k+(i**2)
    print(f"The summation is {k}")