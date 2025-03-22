# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

first_word_count = 0
second_word_count = 0

first_word_count += name1.count("t")
first_word_count += name1.count("r")
first_word_count += name1.count("u")
first_word_count += name1.count("e")
first_word_count += name2.count("t")
first_word_count += name2.count("r")
first_word_count += name2.count("u")
first_word_count += name2.count("e")

second_word_count += name1.count("l")
second_word_count += name1.count("o")
second_word_count += name1.count("v")
second_word_count += name1.count("e")
second_word_count += name2.count("l")
second_word_count += name2.count("o")
second_word_count += name2.count("v")
second_word_count += name2.count("e")

score = int(first_word_count * 10 + second_word_count)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
