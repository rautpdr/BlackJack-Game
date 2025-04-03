#create a deck
#52 cards , 4 suits * 13 ranks
#shuffle deck

#calculate value of hand


#Deal cards
#Give 2cards to both players and dealer
#player can see both the cards and one of dealr's card

#player's turn
#Ask hit or stand
#if hit give a card
#if total > 21 , bust(loss)

#Dealer's turn
#Reveal hidden card
#dealer has to hit if value < 17
#if value > 21 dealer busts, player wins

#compare rules
#compare total values
#decide winners

import random
#constants
suits = ['Spades' , 'Diamonds', 'Clubs', 'Hearts']
ranks = ['2','3','4','6','7','8','9','10','J','Q','K','A']
card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

#create a deck
def create_deck():
    deck = [(suit , rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

#calculate value of hand
def calculate_value(hand):
    value = 0
    ace_value = 0
    for (suit,rank) in hand:
        value += card_values[rank]
        if rank == 'A':
            ace_value =+ 1

    while value > 21 and ace_value:
        value -= 10
        ace_value -= 1

    return value

#display hands
def display_hands(hand, name, isHidden = False):
    print(f"{name}'s hand : " )
    if isHidden:
        print("[Hidden " , hand[1] , "]")
    else:
        print(hand)


#main function
def play_black_jack():
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop() , deck.pop()]

    display_hands(player_hand , "Pratham")
    display_hands(dealer_hand , "Dealer", isHidden = True)

    #player turn
    while True:
        player_score = calculate_value(player_hand)
        if player_score > 21:
            print("Bust! Dealer Wins")
            return

        move = input("Do you want to hit or stand(h/s)? : ")
        if move =='h':
            player_hand.append(deck.pop())
            calculate_value(player_hand)
            display_hands(player_hand , "Pratham")
        elif move == 's':
            break


    #dealer turn
    display_hands(dealer_hand , "Dealer")
    dealer_score = calculate_value(dealer_hand)

    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_value(dealer_hand)
        display_hands(dealer_hand , "Dealer")

    #final score
    dealer_score = calculate_value(dealer_hand)
    player_score = calculate_value(player_hand)

    if dealer_score > 21 or dealer_score < player_score:
        print("Player Wins!")
    elif player_score < dealer_score:
        print("Dealer Wins!")
    else:
        print("It's a tie")

#start the game

play_black_jack()



