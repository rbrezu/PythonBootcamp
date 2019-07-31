import random


class Card:
    card_values = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
        10: 10, 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
    }

    jack = 11
    queen = 12
    king = 13
    ace = 14

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print('The card is the {} of {}.'.format(Card.card_values[self.value], self.suit))

    def __str__(self):
        return '{} of {}'.format(Card.card_values[self.value], self.suit)


class Hand:
    card_blackjack_values = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
        10: 10, 11: 10, 12: 10, 13: 10
    }

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_hand_value(self):
        value_ace_one = 0
        value_ace_ten = 0
        for card in [x.value for x in self.cards]:
            if card == Card.ace:
                value_ace_one += 1
                value_ace_ten += 10
            else:
                value_ace_one += Hand.card_blackjack_values[card]
                value_ace_ten += Hand.card_blackjack_values[card]
        return value_ace_one, value_ace_ten

    def clear(self):
        self.cards.clear()


class Chips:
    start_chips = [10, 5, 1]
    # item in list gives amount of chips (1, 5, 10)
    # beginning value = 45$

    def __init__(self):
        self.chips = Chips.start_chips

    def place_bet(self, value):
        bet_valid = self.check_bet(value)
        if bet_valid is False:
            print('You can\'t bet that amount!')
            return False

        ten_chips = value // 10
        five_chips = (value - ten_chips * 10) // 5
        one_chips = (value - ten_chips * 10 - five_chips * 5)

        chips_removed = min(ten_chips, self.chips[2])
        self.chips[2] -= chips_removed
        ten_chips -= chips_removed

        if ten_chips > 0:
            # not enough 10$ chips, checking for 5$ chips
            five_chips += ten_chips * 2

        chips_removed = min(five_chips, self.chips[1])
        self.chips[1] -= chips_removed
        five_chips -= chips_removed

        if five_chips > 0:
            one_chips += five_chips * 5

        chips_removed = min(one_chips, self.chips[0])
        self.chips[0] -= chips_removed
        one_chips -= chips_removed

        return True

    def add_chips(self, value):
        self.chips[0] += value

    def check_bet(self, bet):
        possible_bets = []
        for i in range(self.chips[0] + 1):
            for j in range(self.chips[1] + 1):
                for k in range(self.chips[2] + 1):
                    possible_bets.append(i + j * 5 + k * 10)

        if bet in possible_bets:
            return True
        return False

    def show_chips(self):
        print('You currently have: ')
        for i in range(3):
            print('\t- {} {}$ chips'.format(self.chips[i], max(1, i * 5)))


class Deck:
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    def __init__(self):
        self.deck = []

    def build(self):
        for suit in Deck.suits:
            for value in range(1, 15):
                self.deck.append(Card(suit, value))

    def shuffle(self):
        total_cards = len(self.deck)
        for i in range(total_cards):
            new_index = random.randint(0, total_cards - 1)
            self.deck[i], self.deck[new_index] = self.deck[new_index], self.deck[i]

    def draw_card(self):
        first_card = self.deck[0]
        self.deck.pop(0)
        return first_card

    def __len__(self):
        return len(self.deck)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = Chips()

    def draw(self, deck):
        self.hand.add_card(deck.draw_card())

    def hand_value(self):
        return self.hand.get_hand_value()

    def show_chips(self):
        self.chips.show_chips()

    def show_cards(self):
        for i in self.hand.cards:
            print('\t', i)

    def clear_hand(self):
        self.hand.clear()


print('Welcome to the game of Blackjack!')
name = input('Your name: ')
player = Player(name)
dealer = Player('Dealer')


choice = ''
while choice is not 'e':
    choice = input('Choose what to do next.\n\tP - Play\n\tE - Exit\nYour choice: ')

    if choice is 'p':
        # init game resources
        deck = Deck()
        deck.build()
        deck.shuffle()
        player.clear_hand()
        dealer.clear_hand()

        # place bet
        player.show_chips()
        bet = int(input('Place your bet: '))
        valid_bet = player.chips.place_bet(bet)
        while valid_bet is False:
            print('Your bet is invalid. Bet again.')
            bet = int(input('Place your bet: '))
            valid_bet = player.chips.place_bet(bet)

        # play game
        game_running = True
        while game_running:
            for i in range(2):
                player.draw(deck)
                dealer.draw(deck)

            print('The dealer\'s first card is: ')
            dealer.hand.cards[0].show()

            print('Your cards are: ')
            player.show_cards()

            choice = input('Hit or Stand? (H / S): ').upper()
            busted = False

            while choice == 'H':
                player.draw(deck)
                print('Your cards are: ')
                player.show_cards()

                if min(player.hand_value()) > 21:
                    print('You busted! You lost your bet!')
                    game_running = False
                    busted = True
                    break
                else:
                    choice = input('Hit or Stand? (H / S): ').upper()

            if not busted:
                while max(dealer.hand_value()) < 17:
                    dealer.draw(deck)
                    print('The dealer took another card...')

                print('The dealer stands!')
                print('Dealer cards: ')
                dealer.show_cards()
                print('Your cards: ')
                player.show_cards()

                player_hand = max(player.hand_value())
                if player_hand > 21:
                    player_hand = min(player.hand_value())

                dealer_hand = max(dealer.hand_value())
                if dealer_hand > 21:
                    dealer_hand = min(dealer.hand_value())

                if player_hand > dealer_hand:
                    print('Congratulations! You won!')
                    player.chips.add_chips(bet * 2)
                else:
                    print('The dealer\'s won!')

                game_running = False





