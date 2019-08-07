import random

class Player:

    def __init__(self, name):
        self.name = name

    def get_input(self, board):
        x = int(input("Enter x:"))
        y = int(input("Enter y:"))
        return x, y

def minimax(board, player, depth):
    eval_ = board.is_game_over()

    if eval_ == 2:
        return 10 - depth
    if eval_ == 1:
        return -10 + depth
    if eval_ == 3:
        return 0

    if player == 2:
        bestVal = -1000
        for move in [(x, y) for x in range(0, 3) for y in range(0, 3) if board.matrix[x][y] == 0]:
            board.matrix[move[0]][move[1]] = 2
            value = minimax(board, player % 2 + 1, depth + 1)
            bestVal = max(bestVal, value)
            board.matrix[move[0]][move[1]] = 0
        return bestVal
    else:
        bestVal = 1000
        for move in [(x, y) for x in range(0, 3) for y in range(0, 3) if board.matrix[x][y] == 0]:
            board.matrix[move[0]][move[1]] = 1
            value = minimax(board, player % 2 + 1, depth + 1)
            bestVal = min(bestVal, value)
            board.matrix[move[0]][move[1]] = 0
        return bestVal

class AI(Player):

    def __init__(self, name):
        super().__init__(name)

    def get_input(self, board):
        savedMove = (-1,-1)
        savedVal = -1000
        for move in [(x, y) for x in range(0, 3) for y in range(0, 3) if board.matrix[x][y] == 0]:
            board.matrix[move[0]][move[1]] = 2
            moveVal = minimax(board, 1, 0)
            if moveVal > savedVal:
                savedVal = moveVal
                savedMove = move
            board.matrix[move[0]][move[1]] = 0
        return savedMove

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
        result = 0

        pindex = 1
        while not result:

            self.board.draw()

            print("Player %d turn:" % pindex)
            coord = (-1, -1)
            if pindex == 1:
                coord = self.player1.get_input(self.board)
            else:
                coord = self.player2.get_input(self.board)

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

class AIGame(Game):

    def __init__(self):
        self.player1 = Player("PlayerOne")
        self.player2 = AI("PlayerTwo")
        self.board = Board()
        self.game_loop()

game = AIGame()