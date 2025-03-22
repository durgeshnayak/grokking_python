import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
guessed = False

if difficulty_level == 'easy':
    attempts = 10
elif difficulty_level == 'hard':
    attempts = 5
else:
    print("You have selected an incorrect option for difficulty level.")


while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You have guessed correctly. YOU WON!")
        attempts = 0
        guessed = True
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1
    else:
        print("Too high.\nGuess again.")
        attempts -= 1

if not guessed:
    print("You have exhausted all your attempts. YOU LOSE!")


