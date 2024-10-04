import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def getCardValue(self):
        if self.rank.isdigit():
            return int(self.rank)
        
        elif self.rank in ['J','Q','K']:
                return 10
        
        elif self.rank == 'A':
            return 11 #or 1, depending on the game logic
        

class Deck:
    def __init__(self, num_of_decks = 1):
        if num_of_decks <= 0:
            raise ValueError("Number of decks must be a positive integer.")
        self.num_of_decks = num_of_decks
        self.cards = self.createDeck(self.num_of_decks)
        #shuffle the deck
        self._shuffle()

    def createDeck(self, num_of_decks):
        ranks = ['2','3','4','5','6','7','8','9','10',
                 'J','Q','K','A']
        suits = {'Hearts':'\u2665', 'Diamond': '\u2666',
                  'Club':'\u2663', 'Spade':'\u2660'}
        #use list comprehension to create the deck of cards
        cards  = [Card(rank, suit) 
                 for rank in ranks
                 for suit in suits.values()
                 for _ in range(self.num_of_decks)]
        return cards
    
    def _shuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()

