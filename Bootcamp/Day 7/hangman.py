import random
import hangman_words
import hangman_art

puzzle = random.choice(hangman_words.word_list)
puzzle_length = len(puzzle)

exit_game = False
player_lives = 6

print(hangman_art.logo)

display = []
for count in range(puzzle_length):
    display.append("_")

while not exit_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for count in range(puzzle_length):
        letter = puzzle[count]
        if letter == guess:
            display[count] = letter

    if guess not in puzzle:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        player_lives -= 1

        if player_lives == 0:
            exit_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        exit_game = True
        print("You win.")

    print(hangman_art.stages[player_lives])
