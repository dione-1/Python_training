suits = ["Clubs","Hearts","Spades","Diamonds"]
suit = suits[2]
ranks = ["A", "K", "Q", "J", '10', '9', '8', '7', '6', '5', '4', '3','2' ]
value = 10


cards = []


for suit in suits:
    for rank in ranks:
        print([suit,rank])
    
