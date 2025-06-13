height = input("Input your height in meter.")
weight = input("Input your weight in KG.")
weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)
