print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L>>>")  
add_pepperoni = input("Do you want pepperoni? Y or N>>>") 
extra_cheese = input("Do you want extra cheese? Y or N>>>") 

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  else:
    bill = 15
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}.")
  else:
    print(f"Your final bill is: ${bill}.")
if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  else:
    bill = 20
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}.")
  else:
    print(f"Your final bill is: ${bill}.")
if size =="L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  else:
    bill = 25
  if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is: ${bill}.")
  else:
    print(f"Your final bill is: ${bill}.")
