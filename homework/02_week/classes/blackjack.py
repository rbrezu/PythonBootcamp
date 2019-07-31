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

    @property
    def rank(self):
        return 10 if self.value in ['J', 'Q', 'K'] else \
            11 if self.value == 'A' else self.value

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '({}, {})'.format(self.value, self.suit)


# creating Deck, shuffle function and single dealing#

class Deck:
    def __init__(self):
        self.cards = Card.generate_all()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop(0)
        return card


class Hand:
    def __init__(self):
        self.cards = []

    def hit(self, card):
        self.cards.append(card)

    @property
    def score(self):
        aces = 0
        score = 0

        for card in self.cards:
            if card.value == 'A':
                aces += 1

            score += card.rank

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def __repr__(self):
        return '{} score of {}'.format(self.cards, self.score)

    def __dealer_hand__(self):
        return '{}'.format([('X', 'X'), *self.cards[-1:]])


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = Chips()

    def hit(self, deck):
        self.hand.hit(deck.draw_card())

    def take_bet(self):
        self.chips.take_bet()

    def take_hit(self, deck):
        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's'    ")
            if x[0].lower() == 'h':
                self.hit(deck)  # hit() function defined above
                return True
            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                return False

    def reset_hand(self):
        self.hand = Hand()

    def lose(self):
        self.chips.lose_bet()
        self.reset_hand()

    def win(self):
        self.chips.win_bet()
        self.reset_hand()

    def full_string(self):
        return '{} - {} --- {}'.format(self.name, self.hand,
                                       self.chips)  # '{} - {}'.format(self.name, self.hand.__dealer_hand__()) if self.name == 'Dealer' else\

    def __repr__(self):
        return '{} - {}'.format(self.name, self.hand.__dealer_hand__()) if self.name == 'Dealer' else \
            self.full_string()


class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def take_bet(self):
        while True:
            try:
                self.bet += int(input('How many chips would you like to bet?\n'))
            except ValueError:
                print("Sorry, a bet must be an integer!")
            else:
                if self.bet > self.total:
                    print('Sorry, your bet cannot exceed {} '.format(self.total))
                else:
                    break

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

    def __repr__(self):
        return '[{}, {}]'.format(self.bet, self.total)


if __name__ == '__main__':
    print("Welcome to Blackjack.")
    player = Player('Me')
    dealer = Player('Dealer')

    while True:
        deck = Deck()
        deck.shuffle()

        player.hit(deck)
        player.hit(deck)

        dealer.hit(deck)
        dealer.hit(deck)

        player.take_bet()

        print(player, dealer, sep='\n')

        playing = True
        while playing:
            playing = player.take_hit(deck)
            if player.hand.score > 21:
                break

            print(player, dealer, sep='\n')

        if player.hand.score <= 21:
            while dealer.hand.score < 17:
                dealer.hit(deck)

            print(player, dealer.full_string(), sep='\n')
            if dealer.hand.score > 21:
                print('\n\nDealer BUSTED')
                dealer.lose()
                player.win()
            elif dealer.hand.score < player.hand.score:
                print('\n\nPlayer WINS')
                dealer.lose()
                player.win()
            elif dealer.hand.score > player.hand.score:
                print('\n\nDealer WINS')
                dealer.win()
                player.lose()
            else:
                print('\n\nTie')
                dealer.reset_hand()
                player.reset_hand()
        else:
            print(player, dealer.full_string(), sep='\n')
            print('\n\nPlayer BUSTED')
            player.lose()
            dealer.win()

        print('Player status', player.chips, sep='\n')

        new_game = input("would you like to play again? Enter 'y' or 'n'  ")
        if new_game.strip() == 'y':
            continue
        else:
            print('Thanks for playing! ')
            break
