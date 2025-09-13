import random
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("rock, paper, or scissors? ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    if player == computer:
        return "It's a tie!"
    elif win_conditions[player] == computer:
        return f"{player.capitalize()} > {computer}! Win"
    else:
        return f"{computer.capitalize()} > {player}! You lose"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
