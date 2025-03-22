# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
total_bill = float(bill)

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_amount = 1.00 + (float(tip) / 100)

people = input("How many people to split the bill? ")
people_number = int(people)

tip_final = (total_bill / people_number) * tip_amount
tip_final = round(tip_final, 2)

print(f"Each person should pay: ${tip_final}")
