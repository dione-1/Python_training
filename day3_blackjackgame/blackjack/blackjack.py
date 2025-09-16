import random

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0

        self.dealer = dealer
    def add_card(self, card):
        self.cards.extend(card)
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card.value = int(card.rank["value"])
            self.value += card.value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10
    def get_value(self):
        self.calculate_value()
        return self.value
    def is_blackjack(self):
        return self.value == 21
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards \
                    and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "hearts", "clubs", "diamonds"]
        ranks = [{"rank": "A", "value": 11},
             {"rank": "K", "value": 10},
             {"rank": "Q", "value": 10},
             {"rank": "J", "value": 10},
             {"rank": "10", "value": 10},
             {"rank": "9", "value": 9},
             {"rank": "8", "value": 8},
             {"rank": "7", "value": 7},
             {"rank": "6", "value": 6},
             {"rank": "5", "value": 5},
             {"rank": "4", "value": 4},
             {"rank": "3", "value": 3},
             {"rank": "2", "value": 2}
             ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    def shuffle(self):
        if len(self.cards) > 1 :
            random.shuffle(self.cards)
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while game_number <= 0:
            try:
                game_to_play = int(input("How many games do you want to play : ").lower())
            except:
                print("Invalid input")
        while game_number <= games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

        for x in range(2):
            player_hand.add_card(deck.deal(1))
            dealer_hand.add_card(deck.deal(1))
        print()
        print("*" * 30)

        print(f"Game {game_number} of {games_to_play}")
        player_hand.display()
        dealer_hand.display()
    def check_win(self, player_hand, dealer_hand, game_over=False):
        if player_hand.get_value() > 21:
            print("You went over. You lose!")
            return True
        elif dealer_hand.get_value() > 21:
            print("Dealer went over. You win!")
            return True
        elif player_hand.is_blackjack() == dealer_hand.is_blackjack():
            print("It's a tie!")
            return True
        elif player_hand.is_blackjack():
            print("Blackjack! You win!")
            return True
        elif dealer_hand.is_blackjack():
            print("Dealer has Blackjack. You lose!")
            return True
        return False




g = Game()
g.play()