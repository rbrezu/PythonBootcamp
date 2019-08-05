from collections import OrderedDict
from math import inf as infinity


class Board:
    def __init__(self):
        self.display = OrderedDict()
        self.reset()

    def reset(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.display[i, j] = ' '

    def get_all(self):
        all = []
        for i in range(0, 3):
            line = ''.join([self[i, j] for j in range(0, 3)])
            all.append((line, 'l', i))

        for i in range(0, 3):
            col = ''.join([self[j, i] for j in range(0, 3)])
            all.append((col, 'c', i))

        diag0 = ''.join([self[i, i] for i in range(0, 3)])
        diag1 = ''.join([self[i, 2 - i] for i in range(0, 3)])
        all.append((diag0, 'd', 0))
        all.append((diag1, 'd', 1))

        return all

    def get_status(self):
        for line, type, pos in self.get_all():
            if line in ['XXX', 'OOO']:
                return line[0], type, pos

        return ' ', 0, 0

    def empty_cells(self):
        return [(x, y) for x, y in self.display.keys() if self.display[x, y] == ' ']

    def game_over(self):
        return self.get_status()[0] != ' ' or self.is_full()

    def is_full(self):
        return len(self.empty_cells()) == 0

    def __getitem__(self, item):
        return self.display[item]

    def __setitem__(self, key, value):
        if value not in ['O', 'X']:
            raise ValueError('Value must be X or O')
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError('Bad input!')

        x, y = key
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError('Input must be between 0 <= x < 3')
        if self.display[key] != ' ':
            raise ValueError('Value is already occupied')

        self.display[key] = value

    def __str__(self):
        return '{} | {} | {}\n' \
               '---------\n' \
               '{} | {} | {}\n' \
               '---------\n' \
               '{} | {} | {}'.format(*self.display.values())


class Player:
    def __init__(self, name='Player 1', val='X'):
        self.name = name
        self.val = val

    def get_move(self, board):
        while True:
            try:
                x = input('{} Put in position:\n'.format(self.name))
                pos = tuple(int(y) for y in x.split(' '))

                board[pos] = self.val
                break
            except ValueError as e:
                print(e)
            except IndexError as e:
                print(e)


class ComputerPlayer(Player):
    def get_move(self, board):
        pass

    def minimax(self, board, depth, player):
        # will be added
        pass


class XO:
    def __init__(self):
        self.board = Board()
        pass

    def start_game(self):

        self.board.reset()
        self.players = [
            Player('Player 1', 'X'),
            Player('Player 2', 'O')
        ]

        turn = 0
        while not self.board.game_over():
            print(self.board)
            self.players[turn].get_move(self.board)
            turn = (turn + 1) % 2

        print(self.board)
        type, line, col = self.board.get_status()
        if type == ' ':
            print('Game was a tie...')
        elif type == 'X':
            print('Player 1 wins')
        else:
            print('Player 2 wins')

        while True:
            try:
                x = input('Start another game y/n ?\n').strip()
                if x == 'y':
                    self.start_game()
                    break
                elif x == 'n':
                    return
                else:
                    raise AssertionError
            except AssertionError as e:
                print('Bad input retry!!!')


xo = XO()
xo.start_game()
