from card import Card, Deck
 
class Hand:
    def __init__(self):
        self.cards = [] 
        self.bet   = 0
    
    def addCard(self, card):
        self.cards.append(card)

    def placeBet(self,bet):
        self.bet = bet

    def getHandValue(self):
        cards_total = 0
        ace_count = 0

        #if there are cards in the hand
        if self.cards:
            for card in self.cards:
                card_value = card.getCardValue()
                #count the number of aces in hand
                if card_value == 11:
                    ace_count += 1
                cards_total += card_value
            
            #adjust ace values if total exceeds 21
            while cards_total > 21 and ace_count:
                cards_total -= 10 #treat ace as 1 instead of 11
                ace_count -= 1

            return cards_total
        #handle empty hand
        else:
            #raise ValueError("Hand is empty")
            return cards_total

class Player:
    def __init__(self):
        self.hands = []
        self.active_hand = 0
        self. __max_split_limit = 3
        self.no_of_splits = 0

        
    def doubleDown(self):
        #if doubledown conditons met
        current_hand = self.hands[self.active_hand]
        if len(self.hands) == 1 and len(current_hand.cards) == 2:
            #restrict to specific hand totals
            hand_total = current_hand.getHandValue()
            if hand_total in [9,10,11]:
                #double bet
                current_hand.bet *= 2
        #if conditions not met
        else:
            print("Double down not allowed for this hand.")

    def split(self,hand,deck):
        #ensure 2 cards
        if len(hand.cards) == 2:
            card1_rank = hand.cards[0].rank
            card2_rank= hand.cards[1].rank
            
            #establish ey r of same rank
            if card1_rank == card2_rank:
                #ensure within maxsplit limit
                if self.no_of_splits < self.__max_split_limit:
                    #split Hand
                    split_card = hand.cards.pop()
                    dealt_card1 = deck.dealCard() 
                    hand.addCard(dealt_card1)

                    new_hand   = Hand()
                    bet = hand.bet
                    new_hand.placeBet(bet)
                    new_hand.addCard(split_card)
                    dealt_card2 = deck.dealCard()
                    new_hand.addCard(dealt_card2)
                    
                    #add new to hands list
                    self.hands.append(new_hand)

                    self.no_of_splits += 1
                else: 
                    print("Maximum split limit reached.")
            else:
                print("Cannot split. The cards are not of the same rank.")
        else:
            print("Cannot split. You must have exactly 2 cards to split.")

    def hit(self, hand, deck):
        if hand.getHandValue() < 21:
            card = deck.dealCard()
            hand.addCard(card)
        else:
             print("Player cannot hit (either has 21 or busted).")
    
    def stand(self, hand):
        hand_value = hand.getHandValue()
        if hand_value <= 21:
            print(f"Player stands with a hand value of {hand_value}.")
        else:
            print("Player cannot stand, they have busted.")

    def displayHand(self,hand):
        rows = ['','','','','']
        cards = hand.cards
        for card in cards:
            rank = card.rank
            suit = card.suit
            rows[0] += f' ___'
            rows[1] += f'|{rank}  |'
            rows[2] += f'| {suit} |'
            rows[4] += f'|__{rank}|'

        for row in rows:
            print(row)
        #create a space after displaying hands 
        print()

