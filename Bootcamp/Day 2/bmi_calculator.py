# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_num = float(height)
weight_num = float(weight)

bmi = (weight_num / (height_num ** 2))

bmi_num = int(bmi)

print(str(bmi_num))
