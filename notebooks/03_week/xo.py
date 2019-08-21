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
        # if value not in ['O', 'X']:
        #     raise ValueError('Value must be X or O')
        if not isinstance(key, tuple) or len(key) != 2:
            raise IndexError('Bad input!')

        x, y = key
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise IndexError('Input must be between 0 <= x < 3')
        # if self.display[key] != ' ':
        #     raise ValueError('Value is already occupied')

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
        best, x, y = self.minimax(board, self.val)
        board[x, y] = self.val

    def minimax(self, board, player, depth=0):
        best = -10 if player == 'O' else 10
        best_x, best_y = None, None

        if board.game_over():
            type, line, col = board.get_status()
            if type == 'X':
                return -10 + depth, best_x, best_y
            elif type == 'O':
                return 10 - depth, best_x, best_y
            else:
                return 0, best_x, best_y

        empty_cells = board.empty_cells()
        for x, y in empty_cells:
            board[x, y] = player
            val, _, _ = self.minimax(board, 'X' if player == 'O' else 'O', depth + 1)
            board[x, y] = ' '

            if player == 'O':
                if val >= best:
                    best, best_x, best_y = val, x, y
            else:
                if val <= best:
                    best, best_x, best_y = val, x, y

        return best, best_x, best_y


class XO:
    def __init__(self):
        self.board = Board()
        pass

    def start_game(self):

        self.board.reset()
        self.players = [
            Player('Player 1', 'X'),
            ComputerPlayer('Player 2', 'O')
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



import argparse
import os
import sys
import socket

args = argparse.ArgumentParser()
args.add_argument('-s', default='server')
args.add_argument('-host', default='localhost')
args.add_argument('-port', default='9999', type=int)

ar = args.parse_args()


class Game:
    def __init__(self, type, host, port):
        self.board = Board()
        self.type = type
        self.host = host
        self.port = port
        self.player = 'X' if type == 'server' else 'O'
        self.my_move = type == 'client'

        if type == 'server':
            self.serve()
        else:
            self.connect()


    def serve(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        conn, addr = s.accept()

        self.s = conn

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        self.s = s


    def run(self):
        while not self.board.game_over():
            if self.my_move:
                x, y = [int(x) for x in input('Set move to send: ').split(' ')]
                player = self.player
                self.s.sendall('{} {}'.format(x, y).encode('utf-8'))
            else:
                x, y = [int(x) for x in self.s.recv(1024).decode('utf-8').split(' ')]
                player = 'O' if self.player == 'X' else 'X'

            self.my_move = not self.my_move
            self.board[x, y] = player
            print (self.board)

game = Game(ar.s, ar.host, ar.port)
game.run()


# python xo.py -s server
# python xo.py -s client



#
# xo = XO()
# xo.start_game()
