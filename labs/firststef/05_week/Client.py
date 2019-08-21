import random
import time
import socket

class Player:

    def __init__(self, name):
        self.name = name

    def get_input(self, board):
        x = int(input("Enter x:"))
        y = int(input("Enter y:"))
        return x, y


class Board:
    def __init__(self):
        self.matrix = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    def set(self, player_key, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            return False
        if self.matrix[row][column] != 0:
            return False
        self.matrix[row][column] = player_key
        return True

    def is_full(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def is_game_over(self):
        for i in range(0,3):
            ok = True
            for j in range(0,3):
                if self.matrix[i][j] != self.matrix[i][0]:
                    ok = False
            if ok == True and self.matrix[i][0] != 0:
                return self.matrix[i][0]

        for j in range(0,3):
            ok = True
            for i in range(0,3):
                if self.matrix[i][j] != self.matrix[0][j]:
                    ok = False
            if ok == True and self.matrix[0][j] != 0:
                return self.matrix[0][j]

        if self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] != 0:
            return self.matrix[0][0]

        if self.matrix[0][2] == self.matrix[1][1] and self.matrix[2][0] == self.matrix[1][1] and self.matrix[1][1] != 0:
            return self.matrix[1][1]

        if self.is_full() == True:
            return 3
        else:
            return 0

    def draw(self):
        print("{} {} {}\n{} {} {}\n{} {} {}".format(*[self.matrix[i][j] for i in range(0,3) for j in range(0,3)]))

class Game:

    def __init__(self):
        self.player1 = Player("PlayerOne")
        self.player2 = Player("PlayerTwo")
        self.board = Board()
        self.game_loop()

    def game_loop(self):
        pindex = 1
        ownIndex = 0

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 65432))

            ownIndex = int(s.recv(1024))
            print("You are player %d" % ownIndex)

            data = (0,0)

            while True:

                self.board.draw()

                print("Player %d turn:" % pindex)
                coord = (-1, -1)
                if pindex != ownIndex:
                    x = s.recv(1024)
                    y = s.recv(1024)
                    coord = (int(x), int(y))
                    if not coord:
                        break
                else:
                    if ownIndex == 1:
                        coord = self.player1.get_input(self.board)
                    else:
                        coord = self.player2.get_input(self.board)
                    s.send(str(coord[0]).encode("utf-8"))
                    s.send(str(coord[1]).encode("utf-8"))

                time.sleep(1)
                if coord[0] > 2 or coord [0] < 0 or coord[1] > 2 or coord [1] < 0:
                    print("Incorrect coordinates")
                    s.send(str(pindex).encode('utf-8'))
                    continue

                if not self.board.set(pindex, *coord):
                    print("Invalid choice")
                    s.send(str(pindex).encode('utf-8'))
                    continue

                state = self.board.is_game_over()

                if state == 1 or state == 2:
                    print("Player %d wins:" % pindex)
                    self.board.draw()
                    break
                elif state == 3:
                    print("The game ended in draw")
                    self.board.draw()
                    break

                pindex = pindex % 2 + 1
                s.send(str(pindex).encode('utf-8'))

game = Game()