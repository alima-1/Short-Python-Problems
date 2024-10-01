import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.cards = self.createDeck(self.num_decks)
        #shuffle the deck
        self._shuffle()

    def createDeck(self, num_decks):
        ranks = ['2','3','4','5','6','7','8','9','10',
                 'J','Q','K','A']
        suits = {'Hearts':'\u2665', 'Diamond': '\u2666',
                  'Club':'\u2663', 'Spade':'\u2660'}
        #use list comprehension to create the deck of cards
        cards  = [Card(rank, suit) 
                 for rank in ranks
                 for suit in suits.values()
                 for _ in range(self.num_decks)]
        return cards
    
    def _shuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        return self.cards.pop()

if __name__ == '__main__':
    deck = Deck(3)
    print(len(deck.cards))