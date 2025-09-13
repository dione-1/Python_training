import random

# numbers list
numbers = [str(n) for n in range(37)] + ["00"]


# numbers colors association 
red_numbers = {"1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"}
black_numbers = {"2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"}
green_numbers = {"0", "00"}


def roulette_color(number):
    number = str(number)
    if number in green_numbers:
        return "green"
    elif number in red_numbers:
        return "red"
    elif number in black_numbers:
        return "black"
    else:
        return "unknown"

# Balance system and error try catch
balance = 100 #
print("Welcome to Roulette! You have: " ,balance , "chips ")


while balance >0 :
    print("You have: " ,balance)
    bet_type = input("You can bet on 'color' or 'number', or type 'quit' to stop the game: ").lower()
    
    if bet_type == "quit":
        print("Thank's your final balance is :" , balance , "chips")
        break
    if bet_type not in ["number","color"]:
        print("Invalid bet, select color or number")
        continue
    try:
        bet_amount = int(input("Bet amount will be equal to: "))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount")
            continue
    except:
        print("Bet amount will be equal to: ")
        continue
    
    
    
    if bet_type == "number":
        player_choice = input("type in 0-36 or 00: ")
        if player_choice not in numbers :
            print('Wrong number')
            continue
    elif bet_type == "color":
        player_choice = input("type in red ,black : ")
        if player_choice not in ["red","black"]:
            print("Type in RED or BLACK")
            continue
    # Spin the wheel
    result = random.choice(numbers)
    result_color = roulette_color(result)
   
    
    print(f"Result: {result} | Color: {result_color}")

    
  # Check win
    win = False
    if bet_type == "number" and player_choice == result:
        win = True
        payout = bet_amount * 35
        balance += payout
        print(f"Congratulations! You won {payout} chips!")
    elif bet_type == "color" and player_choice == result_color:
        win = True
        payout = bet_amount
        balance += payout
        print(f"You won {payout} chips on color!")
    
    if not win:
        balance -= bet_amount
        print("You lost this round.")
    
    if balance <= 0:
        print("You ran out of chips! Game over.")
        break   
    


    



    





