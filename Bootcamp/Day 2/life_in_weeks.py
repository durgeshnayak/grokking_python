# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
age_diff = 90 - age_int
num_months = age_diff * 12
num_weeks = age_diff * 52
num_days = age_diff * 365

print(f"You have {num_days} days, {num_weeks} weeks, and {num_months} months left.")
