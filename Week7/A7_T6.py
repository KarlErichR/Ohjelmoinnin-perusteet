import random
random.seed(1234)

result = ["wins", "losses", "draws"]

class Move:
    rock = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
    paper = "     _______\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)"
    scissors = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"

def  displayResult(player: list[str], bot: list[str], name):
    print("\nResults:")
    print(f"{name} - wins ({player[0]}), losses ({player[1]}), draws ({player[2]})")
    print(f"RPS-3PO - wins ({bot[0]}), losses ({bot[1]}), draws ({bot[2]})")
    return None



def senario(player_move, bot_move, player_name, player_result: list[str], bot_result: list[str]) -> None:
    if player_move == bot_move:
        print(f"Draw! Both players chose {player_move}.")
        player_result[2] += 1
        bot_result[2] += 1
        return None
    elif (player_move == "Rock" and bot_move == "Scissors"):
        print(f"{player_name} rock beats RPS-3PO scissors.")
        player_result[0] += 1
        bot_result[1] += 1
        return None
    elif (player_move == "Paper" and bot_move == "Rock"):
        print(f"{player_name} paper beats RPS-3PO rock.")
        player_result[0] += 1
        bot_result[1] += 1
        return None
    elif (player_move == "Scissors" and bot_move == "Paper"):
        print(f"{player_name} scissors beats RPS-3PO paper.")
        player_result[0] += 1
        bot_result[1] += 1
        return None
    elif (bot_move == "Rock" and player_move == "Scissors"):
        print(f"RPS-3PO rock beats {player_name} scissors.")
        bot_result[0] += 1
        player_result[1] += 1
        return None
    elif (bot_move == "Paper" and player_move == "Rock"):
        print(f"RPS-3PO paper beats {player_name} rock.")
        bot_result[0] += 1
        player_result[1] += 1
        return None
    elif (bot_move == "Scissors" and player_move == "Paper"):
        print(f"RPS-3PO scissors beats {player_name}  paper.")
        bot_result[0] += 1
        player_result[1] += 1
        return None
    return None


def gameMenu():
    print("\nOptions :")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    return None


def main():
    player_result: list[str] = [0] * len(result)
    bot_result: list[str] = [0] * len(result)
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...")
    choice = -1
    while choice != 0:
        gameMenu()
        choice = int(input("Your choice: "))
        if choice == 0:
            break
        elif choice in [1, 2, 3]:
            move = ["Rock", "Paper", "Scissors"]
            moves = [Move.rock,  Move.paper, Move.scissors]
            player_move = move[choice - 1]
            player_moves = moves[choice -  1]
            bot_choice = random.randint(1, 3)
            bot_move = move[bot_choice - 1]
            bot_moves = moves[bot_choice - 1]
            print(f"\n#########################\n{player_name} chose {player_move}.\n\n{player_moves}\n\n#########################")
            print(f"\n#########################\nRPS-3PO chose {bot_move}.\n\n{bot_moves}\n\n#########################")
            senario(player_move, bot_move, player_name, player_result, bot_result)
    displayResult(player_result, bot_result, player_name)
    print("\nProgram ending.")
    return None
    

if __name__ == "__main__":
    main()