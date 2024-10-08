from card import Card, Deck
from player import Hand, Player, Dealer

print('''
Rules:
 Try to get as close to 21 without going over.
 Kings, Queens, and Jacks are worth 10 points.
 Aces are worth 1 or 11 points.
 Cards 2 through 10 are worth their face value.
 (H)it to take another card.
 (S)tand to stop taking cards.
 (Sp)lit to split your hand into two separate hands 
 if the first two cards have the same rank. You can 
 split a maximum of 3 times, resulting in up to 4 separate hands. 
 Each hand will then be played independently.
 On your first play, you can (D)ouble down to increase your bet
 but must hit exactly one more time before standing.
 In case of a tie, the bet is returned to the player.
 The dealer stops hitting at 17.''')
print()

#Initial game setup
no_of_decks = 4
max_no_players = 6
players = []
shoe = Deck(4)

#function to handle the number of players and initial bet
def setupPlayers():
    print('''The game takes a maximum of 6 players.\nHow many people will be playing?''')
    while True:
        no_players = input('>')
        try:
            no_players = int(no_players)
            if no_players not in range(1,8):
                raise ValueError('invalid input:Number of players must be between 1-7.') 
        except ValueError as ve:
            if 'invalid literal for int()' in str(ve):
                print('invalid input: must be a number')
            else:
                print(ve)
            print('Please try again.')
        else:
            #play game
            for i in range(no_players):
                players.append(Player())#place player obj in player list
                handleBet(i)
            break    

def handleBet(player_index):
    players[player_index].hands.append(Hand())#place hand obj in player hands list
    hand = players[player_index].hands[0]
    print(f'Player#{player_index+1}')
    print('How much do you bet? (1-5000)')
    while True:
        bet = input('>')
        #bet input validation
        try:
            bet = int(bet)
            if bet not in range(1,5001):
                raise ValueError('invalid input: bet should be between 1-5000.')
            else:
                hand.bet = bet
                card1 = shoe.dealCard()
                card2 = shoe.dealCard()
                hand.addCard(card1)
                hand.addCard(card2)
                break # break out of the bet input loop
        except ValueError as err:
            if 'invalid literal for int()' in str(err):
                print('invalid input: should be a number between 1-6.')
            else: 
                print(err)
                print('Please try again')
    print() #create space between asking players to place their bets

 #function to check for naturalblackjack          
def checkNaturalBlackjack(dealer, players):
    exitted_players = []#holds player that are done playing
    dealer_hand_value = dealer.hand.getHandValue()
    for i,player in enumerate(players):
        hand = player.hands[0]
        player_hand_value = hand.getHandValue()
        
        if dealer_hand_value == 21 and player_hand_value == 21:
            exitted_players.append(player)#player exits game
            displayOutcome(player, player_hand_value, i, hand, dealer, dealer_hand_value,'Tie')
        elif dealer_hand_value == 21 and player_hand_value < 21:
            exitted_players.append(player)#player exits game
            displayOutcome(player, player_hand_value, i, hand, dealer, dealer_hand_value,'Loss')
        elif dealer_hand_value < 21 and player_hand_value == 21:
            exitted_players.append(player)#player exits game
            displayOutcome(player, player_hand_value, i, hand, dealer, dealer_hand_value,'Win')
    return exitted_players

#function to display outcomes of the naturalblackjack check
def displayOutcome(p_obj, p_hand_value, p_index, p_hand, d_obj, d_hand_value, result): 
    print(f'DEALER: {d_hand_value}')
    d_obj.displayHand()
    print()
    print(f'PLAYER{p_index+1}: {p_hand_value}')
    p_obj.displayHand()  
    if result == 'Tie':         
        print(f'Its a TIE. You get back ${p_hand.bet}')
    elif result == 'Loss':
         print(f'You LOSE ${p_hand.bet}')
    else:
        print(f'You WIN ${p_hand.bet}')
    print()

while True: #main game loop
    setupPlayers()

    #dealer's play setup
    dealer = Dealer()
    dealer.hand.addCard(shoe.dealCard())
    dealer.hand.addCard(shoe.dealCard())

    #Natural Blackjack Check
    exitted_players = checkNaturalBlackjack(dealer, players)
 
    break

