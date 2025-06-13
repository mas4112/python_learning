# Fibonacci series.
n=int(input("Enter the desired Number for fibonacci series.\n"))
a=0
b=1
if n==1:
    print(a)
if n==2:
    print(a)
    print(b)
if n>2:
    print(a)
    print(b)
    i=1
    while i<=n-2:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1