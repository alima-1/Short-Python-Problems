import random
import itertools              


def get_player_names():
    max_players = 6
    while True:
        player_names = input("Please enter name(s) of player(s)."
                            "(Seperated by commas if there's more than one player)\n-->")
        player_names = [name.strip().capitalize() for name in player_names.split(",") if name.strip()]
        #Handle No entries
        if len(player_names) == 0:
            print("No valid names entered.\nPlease try Again")
            continue
        #handle players exceeding max players
        if len(player_names) > 6:
            print(f"Only {max_players} players are allowed.
                  Truncating the list to {max_players} players.")
            player_names = player_names[:max_players]
        #Handle dulpicates
        if len(player_names) != len(set(player_names)):
            print("Duplicate names found."
                  "\nPlease ensure all names are unique.")
            continue
        break
    return player_names


class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.bets = []
        self.hands = []
        self.splits = 0

    def place_bet(self):
        max_bet = 500
        min_bet = 100
        #validation loop
        while True:
            try:
                bet = int(input(f"Place a bet (between {min_bet}-{max_bet}):"))
                if bet < min_bet or bet > max_bet:
                    raise ValueError(f"Your bet must be between {min_bet} and {max_bet}. Please try again.")
                else:
                   self.bets.append(bet) 
                break
            except ValueError as e:
                print(f"{e}. That's not a valid integer. Please try again.")
    

    def show_cards(self):    
        for hand in self.hands:
            rows = ['','','','','']
            for (rank, suit) in hand:
                rows[0] += ' ___ '
                rows[1] += f'|{rank:<2} |'
                rows[2] += f'| {suit} |'
                rows[3] += f'|_{rank:>2}|'
            #print()
            for row in rows:
                print(row)
            print()  # Add space between hands


    def getHandValue(self,player_hand,hide_value=False):
        if hide_value:
            return "???"
        #evaluates the total of a hand
        total   = 0
        no_aces = 0 # keeps track of the number of aces in 
                    #a hand so it can added to the total last
                    #so as to better decide whether the ace can be a 1 or 11
        for rank, _ in player_hand:
            if rank.isdigit():
                total += int(rank)
            elif rank in ('J','Q','K'):
                total += 10
            else:
                no_aces += 1
        #handle aces
        total += no_aces # adds aces as 1
        for _ in range(no_aces):
            if total + 10 <= 21: #(10 + 1 = 11) testin for ace as 11
                total += 10
        return total
    
    def doubleDown(self, dealer_object):
        #The player can only double down on their initial two-card hand
        #implying that the length of the hands list must be equal to 1
        start_index = 0
        #the first hand in hands
        first_hand = self.hands[start_index]
        if len(self.hands) == 1 and len(first_hand) == 2:
            #the no of hands a player has will always match
            #the no of bets placed.
            doubled_bet = self.bets[start_index] * 2
            #replacing old bet with doubled bet
            self.bets.insert(start_index, doubled_bet)
            self.hands[start_index].append(dealer_object.deal_cards())
        else:
            print("You can only double down on the initial 2 card hand.")

    def hit(self,hand_index, dealer_object):
        #adds a card to the respective hand
        self.hands[hand_index].append(dealer_object.deal_cards())

    def split(self, hand_index, dealer_object):
        #Only split cards of the same rank not value
        hand = self.hands[hand_index]
        #check if the cards have the same rank
        if len(hand) == 2 and hand[0][0] == hand[1][0]:
            if self.splits >= 3:
                print("Cannot split more than 3 times.")
                return
            first_card = hand.pop()
            second_card = hand.pop()
            #place an additional bet equal to the original
            #bet
            #there may be more bets than one so pick the 
            #most recent bet
            bet = self.bets[-1]
            self.bets.append(bet)
            #dealing cards
            first_hand = [first_card, dealer_object.deal_cards()]
            second_hand = [second_card,dealer_object.deal_cards()]
            # Update self.hands with the new hands
            self.hands[hand_index] = first_hand
            self.hands.append(second_hand)
            self.splits += 1
        else:
            print("Cannot Split: The cards are not of the same rank.")

    def stand(self, hand_index):
        print(f"{self.name} stands on Hand #{hand_index + 1}.")



class Dealer(Player):
    NUM_DECKS = 3

    def __init__(self):
        self.name = "Dealer"
        self.hands= [] # B'se a player can have multiple hands (spliting)
        self.deck = self._create_deck() 
    
    def _create_deck(self,num_decks = NUM_DECKS ):
        rank = ('2', '3', '4','5', '6', '7','8','9', '10', 'J', 'Q', 'K', 'A')
        suit = {"Hearts":"\u2665", "Diamonds":"\u2666", "Clubs":"\u2663", "Spades":"\u2660"}
        #create deck of cards = to num of decks 
        deck = list(itertools.product(rank, suit.values())) * num_decks
        #shuffle the created deck of cards
        random.shuffle(deck)
        return deck
    
    def deal_cards(self):
        return self.deck.pop()
    
    def show_cards(self,hide_first_card=False):
        for hand in self.hands:
            rows = ['','','','','']
            for i, (rank, suit) in enumerate(hand):
                if i == 0 and hide_first_card == True:
                    rank = suit = '#'
                    rows[0] += ' ___ '
                    rows[1] += f'|{rank:<2} |'
                    rows[2] += f'| {suit} |'
                    rows[3] += f'|_{rank:>2}|'
                else:
                    rows[0] += f' ___ '
                    rows[1] += f'|{rank:<2} |'
                    rows[2] += f'| {suit} |'
                    rows[3] += f'|_{rank:>2}|'
            #print()
            for row in rows:
                print(row)
            print()  # Add space between hands


    def getHandValue(self, player_hand, hide_value=False):
        return super().getHandValue(player_hand, hide_value)


if __name__ == "__main__":
    players = []
    #get the names/name of player
    player_names = get_player_names()
    #create a player object for each player
    #show the name of the player that has to place a bet.
    #get the players bet
    #add this player to a list to keep track and access it
    for name in player_names:
        player = Player(name)
        print(player.name)
        player.place_bet()
        players.append(player)   
    #Initialise dealer
    dealer = Dealer()
    #deal initial cards to each player 
    for player in players:
        player.hands.append([dealer.deal_cards(), dealer.deal_cards()])
    #deal initial cards to dealer
    dealer.hands.append([dealer.deal_cards(), dealer.deal_cards()])
    #Display cards
    print(f"{dealer.name}: {player.getHandValue(dealer.hands[0],hide_value=True)}")
    dealer.show_cards(hide_first_card=True)        
    for player in players:
        print(f"{player.name}: {player.getHandValue(player.hands[0])}")
        player.show_cards()