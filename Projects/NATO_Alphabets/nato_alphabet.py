import pandas

raw_data = pandas.read_csv(filepath_or_buffer="./nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in raw_data.iterrows()}

is_input_correct = False

while not is_input_correct:
    word = input("Please enter a word: ")

    try:
        phonetic_codes = [letter_dict[char.upper()] for char in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_input_correct = True
        print(f"NATO Alphabets for the word are: {phonetic_codes}")
