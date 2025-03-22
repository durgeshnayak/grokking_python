import random

person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)

if person_choice == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif person_choice == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif person_choice == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if computer_choice == 0:
    print("Computer chose:\n")
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice == 1:
    print("Computer chose:\n")
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computer_choice == 2:
    print("Computer chose:\n")
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if person_choice == computer_choice:
    print("It's a draw.")
else:
    if person_choice == 0:
        if computer_choice == 2:
            print("You win.")
        else:
            print("You lose.")
    elif person_choice == 1:
        if computer_choice == 0:
            print("You win.")
        else:
            print("You lose.")
    elif person_choice == 2:
        if computer_choice == 1:
            print("You win.")
        else:
            print("You lose.")
    else:
        print("You have entered an invalid input. You lose.")
