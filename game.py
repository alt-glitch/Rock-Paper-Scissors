import random


def calculate_win(user_choice, game_plays, scoreboard, name):
    length = len(game_plays)
    computer_choice = random.choice(game_plays)

    if user_choice == computer_choice: # draw
        print("There is a draw ({})".format(user_choice))
        scoreboard[name] += 50
        return 0

    lose_list = []
    ind = game_plays.index(user_choice) + 1
    for _ in range(length // 2):
        if ind < length:
            lose_list.append(game_plays[ind])
        else:
            lose_list.append(game_plays[ind % length])
        ind += 1

    if computer_choice in lose_list:
        print("Sorry, but the computer chose", computer_choice)
    else:
        print("Well done. Computer chose {} and failed".format(computer_choice))
        scoreboard[name] += 100


def main():
    scoreboard = {}
    ratings = open("rating.txt", 'r')
    for line in ratings:
        user, score = line.split()
        scoreboard[user] = int(score)

    allowed_inputs = ["!rating", "!exit"]
    game_plays = []
    name = input("Enter your name: ")
    print("Hello,", name)
    if name not in scoreboard.keys():
        scoreboard[name] = 0
    user_input = str(input())

    if len(user_input.split(",")) != 1:
        game_plays.extend(user_input.split(","))

        print("Okay, let's start")
        user_input = str(input())
    else:
        game_plays.extend(["rock", "paper", "scissors"])

    while True:
        if user_input not in allowed_inputs and user_input not in game_plays:
            print("Invalid input")
        elif user_input == allowed_inputs[0]:
            print("Your rating:", scoreboard[name])
        elif user_input == allowed_inputs[1]:
            print("Bye!")
            ratings.close()
            break
        else:
            calculate_win(user_input, game_plays, scoreboard, name)
        user_input = str(input())

    return 0


main()
