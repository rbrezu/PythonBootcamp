import random

class Player:

    def __init__(self, name):
        self.name = name

    def get_input(self, board):
        x = int(input("Enter column to drop disc:"))
        return x

def minimax(board, player, depth):
    eval_ = board.is_game_over()

    if eval_ == 2:
        return 100 - depth
    if eval_ == 1:
        return -100 + depth
    if eval_ == 3:
        return 0

    if player == 2:
        bestVal = -1000
        for move in range(0, 7):
            if board.matrix[move][5] != 0:
                continue

            h = 0
            while True:
                if board.matrix[move][h] == 0:
                    board.matrix[move][h] = 2
                    break
                h += 1

            if depth < 4:
                value = minimax(board, player % 2 + 1, depth + 1)
                bestVal = max(bestVal, value)
            else:
                bestVal = 0

            board.matrix[move][h] = 0

        return bestVal
    else:
        bestVal = 1000
        for move in range(0, 7):
            if board.matrix[move][5] != 0:
                continue

            h = 0
            while True:
                if board.matrix[move][h] == 0:
                    board.matrix[move][h] = 1
                    break
                h += 1

            if depth < 4:
                value = minimax(board, player % 2 + 1, depth + 1)
                bestVal = min(bestVal, value)
            else:
                bestVal = -10

            board.matrix[move][h] = 0

        return bestVal

class AI(Player):

    def __init__(self, name):
        super().__init__(name)

    def get_input(self, board):
        savedMove = -1
        savedVal = -1000

        for move in range(0, 7):
            if board.matrix[move][5] != 0:
                continue

            h = 0
            while True:
                if board.matrix[move][h] == 0:
                    board.matrix[move][h] = 2
                    break
                h += 1

            moveVal = minimax(board, 1, 0)

            if moveVal > savedVal:
                savedVal = moveVal
                savedMove = move

            board.matrix[move][h] = 0
        return savedMove

class Board:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]

    def set(self, player_key, column):
        if column < 0 or column > 6:
            return False
        if self.matrix[column][5] != 0:#full
            return False
        h = 0
        while True:
            if self.matrix[column][h] == 0:
                self.matrix[column][h] = player_key
                break
            h += 1
        return True

    def is_full(self):
        for i in range(0,7):
            for j in range(0,6):
                if self.matrix[i][j] == 0:
                    return False
        return True

    def is_game_over(self):#acest cod este copiat si modificat pentru ca mi-e lene sa calculez
        if self.is_full():
            return 3

        for columns in range(7-3):
            for rows in range(6):
                if self.matrix[columns][rows] == self.matrix[columns+1][rows] == self.matrix[columns+2][rows] == self.matrix[columns+3][rows] != 0:
                    return self.matrix[columns][rows]

        # Check vertical locations for win
        for columns in range(7):
            for rows in range(6-3):
                if self.matrix[columns][rows] == self.matrix[columns][rows+1] == self.matrix[columns][rows+2] == self.matrix[columns][rows+3] != 0:
                    return self.matrix[columns][rows]

        # Check positively sloped diagonals
        for columns in range(7-3):
            for rows in range(6-3):
                if self.matrix[columns][rows] == self.matrix[columns+1][rows+1] == self.matrix[columns+2][rows+2] == self.matrix[columns+3][rows+3] != 0:
                    return self.matrix[columns][rows]

        # Check negatively sloped diagonals
        for columns in range(7-3):
            for rows in range(3, 6):
                if self.matrix[columns][rows] == self.matrix[columns+1][rows-1] == self.matrix[columns+2][rows-2] == self.matrix[columns+3][rows-3] != 0:
                    return self.matrix[columns][rows]

        return 0

    def draw(self):
        for row in [5,4,3,2,1,0]:
            for col in range(0,7):
                print("%d " % self.matrix[col][row], end = '')
            print("")

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
            column = -1
            if pindex == 1:
                column = self.player1.get_input(self.board)
            else:
                column = self.player2.get_input(self.board)

            if not self.board.set(pindex, column):
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