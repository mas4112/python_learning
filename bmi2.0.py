print("Welcome to the BMI calculator 2.0")
height = float(input("Enter your height in meters e.g., 1.55>>>"))

weight = int(input("Enter your weight in kilograms e.g., 72>>>"))


bmi = weight / (height ** 2)

if bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi >=30:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")     
else:
  print(f"Your BMI is {bmi}, you are underweight.")
