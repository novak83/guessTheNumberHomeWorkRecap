import random
import json
from datetime import datetime



def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list
        #score_list.sort()
        #print("Top scores: ", score_list[:3]) # ali print("Top scores: " +str(score_list))

def get_top_scores():
    score_list = get_score_list()
    new_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    for score in new_score_list:
        print(f"Player {score['player']} had {score['attempts']} attempts. The secret number was {score['secret_number']}, wrong guesses were: {score['wrong_guesses']}")
    # zgornji zapis, nujno morajo biti različni narekovaji kot je zapisano


def play_game(player):
    score_list = get_score_list()
    secret = random.randint(1, 30)
    print(secret) #remove this production
    attempts = 0
    wrong_guesses = []

    while True:
        guess = int(input("Vnesi število:"))
        attempts +=1
        wrong_guesses.append(guess)

        if guess == secret:
            score_list.append({"attempts": attempts,
                            "player": player,
                            "date": str(datetime.now()),
                            "secret_number": secret,
                            "wrong_guesses": wrong_guesses})
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))
            print(f"Bravo, rabil si {attempts} poskusov.")
            break
        elif guess > secret:
            print("Try something smaller.")
        elif guess < secret:
            print("Try something bigger.")

def main():
    get_top_scores()
    player = input("Your name:")

    while True:

        play = input("Do you want to play? (y/n)")
        if play == "y":
            play_game(player)
        else:
            break

    print("Finish")

if __name__ == "__main__":
    main()