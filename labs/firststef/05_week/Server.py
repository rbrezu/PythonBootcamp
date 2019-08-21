import random
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

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', 65432))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)

                data = (0,0)

                while True:

                    self.board.draw()

                    print("Player %d turn:" % pindex)
                    coord = (-1, -1)
                    if pindex == 1:
                        coord = self.player1.get_input(self.board)
                        conn.send(str(coord[0]).encode("utf-8"))
                        conn.send(str(coord[1]).encode("utf-8"))
                    else:
                        x = conn.recv(1024)
                        y = conn.recv(1024)
                        coord = (int(x), int(y))
                        if not coord:
                            break

                    if coord[0] > 2 or coord [0] < 0 or coord[1] > 2 or coord [1] < 0:
                        print("Incorrect coordinates")
                        continue

                    if not self.board.set(pindex, *coord):
                        print("Invalid choice")
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

import threading

def serve_clients(a, b, room_num):
    conn1, addr1 = a
    conn2, addr2 = b

    conn1.send(str(1).encode('utf-8'))
    conn2.send(str(2).encode('utf-8'))

    pIndex = 1
    while True:
        if pIndex == 1:
            print("Room %d: Player 1 turn" % room_num)
            x = int(conn1.recv(1024))
            y = int(conn1.recv(1024))
            pIndex = int(conn1.recv(1024))
            conn2.send(str(x).encode('utf-8'))
            conn2.send(str(y).encode('utf-8'))
            pIndex = int(conn2.recv(1024))
        else:
            print("Room %d: Player 2 turn" % room_num)
            x = int(conn2.recv(1024))
            y = int(conn2.recv(1024))
            pIndex = int(conn2.recv(1024))
            conn1.send(str(x).encode('utf-8'))
            conn1.send(str(y).encode('utf-8'))
            pIndex = int(conn1.recv(1024))

def start_server():
    rooms = []
    waiting = []
    threads = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 65432))

        while True:
            print("Waiting for players")
            s.listen()
            conn, addr = s.accept()
            print("Connected with a client")

            if 0 == len(waiting):
                print("The client will wait for a partner")
                waiting.append((conn, addr))
            else:
                print("Found partner. Starting game")
                pair = (waiting.pop(), (conn, addr))
                rooms.append(pair)
                t = threading.Thread(target=serve_clients, args=(*pair, len(rooms)))#args->?
                t.start()
                threads.append(t)

start_server()
