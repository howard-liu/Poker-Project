

class Deck:

    NUM_CARDS = 52
    CARDS_PER_SUIT = 13
    NUM_SUITS = 4

    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

    CLUBS = 'C'
    DIAMONDS = 'D'
    HEARTS = 'H'
    SPADES = 'S'

    def __init__(self):
        """
        Initiates a Deck object
        """
        self.card = []

        for x in range(self.NUM_SUITS):
            for y in range(self.CARDS_PER_SUIT):
                new_card = Card()
                if x == 0:
                    new_card.suit = self.CLUBS
                elif x == 1:
                    new_card.suit = self.DIAMONDS
                elif x == 2:
                    new_card.suit = self.HEARTS
                elif x == 3:
                    new_card.suit = self.SPADES
                # Aces are 14
                new_card.value = y + 2
                self.card.append(new_card)

    def pop(self):
        return self.card.pop()


class Card:

    def __init__(self):
        """
        Initates a Card object
        """
        self.suit = ''
        self.value = ''

    def __str__(self):
        """
        To string function that prints out what the card is
        :return: 'suit''value' eg D13
        """
        if self.value == 11:
            return str(self.suit) + Deck.JACK
        elif self.value == 12:
            return str(self.suit) + Deck.QUEEN
        elif self.value == 13:
            return str(self.suit) + Deck.KING
        elif self.value == 14:
            return str(self.suit) + Deck.ACE
        else:
            return str(self.suit) + str(self.value)

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
