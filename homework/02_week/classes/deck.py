import random

class Card:
    values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    suits = ('♠', '♣', '♦', '♥')

    def __init__(self, value, suit):
        if not (value in self.values and suit in self.suits):
            raise ValueError('No such suit or value')

        self.value = value
        self.suit = suit

    @classmethod
    def generate_all(cls):
        return [cls(v, s) for v in cls.values for s in cls.suits]

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '({}, {})'.format(self.value, self.suit)

class Deck:
    def __init__(self):
        self.cards = Card.generate_all()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop(0)
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        print ('Gigel drew {}'.format(self.hand[-1]))

if __name__ == '__main__':
    d = Deck()
    print (d.cards)

    p = Player('Gigel')
    p.draw(d)