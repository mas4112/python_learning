# Armstrong Number Checker.

n=int(input("Enter a Number to check if it's an armstrong number or not.\n"))
m=n
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if s==m:
    print("Number is Armstrong.")
else:
    print("Number is not Armstrong.")