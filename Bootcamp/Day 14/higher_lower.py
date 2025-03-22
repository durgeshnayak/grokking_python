import random
import art
import data

print(art.logo)
score = 0
exit_game = False


def get_participant():
    return random.choice(data.data)


participant_1 = get_participant()

while not exit_game:
    participant_2 = get_participant()
    while participant_1["name"] == participant_2["name"]:
        participant_2 = get_participant()
    print(f"Compare A: {participant_1['name']}, {participant_1['description']} from {participant_1['country']}.")
    print(art.vs)
    print(f"Compare B: {participant_2['name']}, {participant_2['description']} from {participant_2['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A":
        if int(participant_1["follower_count"]) > int(participant_2["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")
            participant_1 = participant_2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit_game = True
    elif choice == "B":
        if int(participant_1["follower_count"]) < int(participant_2["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")
            participant_1 = participant_2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit_game = True
    else:
        print(f"You have entered an invalid choice, Goodbye! Final score: {score}")
