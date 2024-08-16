import random, itertools              


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
            print(f"Only {max_players} players are allowed."
                "Truncating the list to {max_players} players.")
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

    def place_bet(self):
        max_bet = 500
        min_bet = 100

        while True:
            try:
                bet = int(input(f"Place a bet (between {min_bet}-{max_bet}):"))
                if bet < min_bet or bet > max_bet:
                    raise ValueError(f"Your bet must be between {min_bet} and {max_bet}. Please try again.")
                else:
                   self.bets.append(bet) 
                break
            except ValueError:
                print("that's not a valid integer. Please try again.")
    
    def show_cards(self):
        rows = ['','','','','']
        
        for hand in self.hands:
            for (rank, suit) in hand:
                rows[0] += f' ___ '
                rows[1] += f'|{rank}  |'
                rows[2] += f'| {suit} |'
                rows[3] += f'|__{rank}|'

            print()
            print(player.name)
            for row in rows:
                print(row)


    def getHandValue(self,player_hand):
        #evaluates the total of a hand
        total   = 0
        no_aces = 0 # keeps track of the number of aces in 
                    #a hand so it can added to the total last
                    #so as to better decide w

        for rank, _ in player_hand():
            if rank.isdigit():
                total += int(rank)
            elif rank in ('J','Q','K'):
                total += 10
            else:
                no_aces += 1

        total += no_aces # adds aces as 1
        for _ in range(no_aces):
            if total + 10 <= 21: #(10 + 1 = 11) testin for ace as 11
                total += 10


        return total


class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hands= [] # B'se a player can have multiple hands (spliting)
    
    def _create_deck(self,num_decks = 3 ):
        rank = ('2', '3', '4','5', '6', '7','8','9', '10', 'J', 'Q', 'K', 'A')
        suit = {"Hearts":"\u2665", "Diamonds":"\u2666", "Clubs":"\u2663", "Spades":"\u2660"}

        #create deck of cards = to num of decks 
        deck = list(itertools.product(rank, suit.values())) * num_decks
        
        #shuffle the created deck of cards
        random.shuffle(deck)
        return deck
    
    def deal_cards(self):
        deck = self._create_deck()
        #return tuple containing (rank,suit)
        return deck.pop()
        
    
    def show_cards(self,hide=False):
        rows = ['','','','','']

        for hand in self.hands:
            for i, (rank, suit) in enumerate(hand):
                if i == 0 and hide == True:
                    rank = suit = '#'
                    rows[0] += f' ___ '
                    rows[1] += f'|{rank}  |'
                    rows[2] += f'| {suit} |'
                    rows[3] += f'|__{rank}|'
                else:
                    rows[0] += f' ___ '
                    rows[1] += f'|{rank}  |'
                    rows[2] += f'| {suit} |'
                    rows[3] += f'|__{rank}|'

            print()
            print(player.name)
            for row in rows:
                print(row)

    

if __name__ == "__main__":
    players = []
    #get the names/name of player
    player_names = get_player_names()
     
    #create a player object for each player
    #show the name of the player that has to place a bet
    #add this player to a list to keep track and access it
    for index,name in enumerate(player_names):
        player = Player(name)
        print(player.name)
        player.place_bet()
        players.append(player)
       
       
       
    #insert dealer as first player in the list of players
    dealer = Dealer()
    players.insert(0,dealer)

    #deal cards to all players
    for player in players:
        hand = []
        for _ in range(2):
            hand.append(dealer.deal_cards())
        player.hands.append(hand)
            
    for player in players:
        if player.name == 'Dealer':
            player.show_cards(hide=True)
        else:
            player.show_cards()