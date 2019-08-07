import random
import sys


class Player:

    def __init__(self, name):
        self.name = name

    def get_input(self):
        x = 'a'
        while True:
            print("Gib letter:")
            x = input().split(" ")[0]
            print(x)
            if ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
                break
            print("Invalid input")

        return x

stages = [
    "________        ",
    "|        |      ",
    "|        0      ",
    "|       /|\     ",
    "|       / \     ",
    "|               ",
    ""
]

def GetDrawing(index):
    if index == 0:
        return []
    if index == 1:
        return [stages[6],stages[6],stages[6],stages[5],stages[5]]
    if index == 2:
        return [stages[6],stages[5],stages[5],stages[5],stages[5]]
    if index == 3:
        return [stages[0],stages[5],stages[5],stages[5],stages[5]]
    if index == 4:
        return [stages[0],stages[1],stages[5],stages[5],stages[5]]
    if index == 5:
        return [stages[0],stages[1],stages[2],stages[5],stages[5]]
    if index == 6:
        return [stages[0],stages[1],stages[2],stages[3],stages[5]]
    if index == 7:
        return [stages[0],stages[1],stages[2],stages[3],stages[4]]

class Game:

    def __init__(self):
        self.player = Player("Player")
        self.game_loop()

    def game_loop(self):

        dictionar = eval(open("dict.txt", 'r').read())
        x = random.randint(1, 4)
        word = list(dictionar.get(x))

        idx = 0
        bitset = [0,0,0,0,0,0,0]
        letters = []

        while True:

            #Draw
            for li in GetDrawing(idx):
                print(li)
            print("GUESS THIS:", sep='', end="")
            for l in word:
                if l in letters:
                    print(l, sep='', end="")
                else:
                    print("._.", sep='', end="")
            print("")

            if 0 not in bitset:
                print("You won")
                break
            if idx == 7:
                print("You lose")
                break

            letter = self.player.get_input()

            if letter in letters:
                print("Already guessed letter")
                continue

            if letter in word:
                print("correct")
                for j in range(0,7):
                    if word[j] == letter:
                        bitset[j] = 1
                letters.append(letter)
            else:
                print("Wrong")
                idx += 1
                continue








game = Game()