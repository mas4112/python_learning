print("Welcome to the odd and even number checker")
number = int(input("Which number do you want to check?"))

odd_or_even = number % 2
if odd_or_even == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
