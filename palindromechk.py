# Palindrome Number checker

n=int(input("Enter a Number to check if it's palindrome or not.\n"))
m=n
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if s==m:
    print("Number is palindrome.")
else:
    print("Number is not Palindrome.")