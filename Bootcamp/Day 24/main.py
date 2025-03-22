
letter_body = ""
names_list = []
with open(file="./Input/Letters/starting_letter.txt", mode="r") as letter_body_stream:
    letter_body = letter_body_stream.read()

with open(file="./Input/Names/invited_names.txt", mode="r") as names_stream:
    names_list = names_stream.readlines()

for name in names_list:
    name = name.strip()
    letter = letter_body.replace("[name]", name)
    file_name = f"{name} - Birthday Invitation.txt"
    with open(file=f"./Output/ReadyToSend/{file_name}", mode="w") as invitation_stream:
        invitation_stream.write(letter)

print("Printing done!")

