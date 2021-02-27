#!/usr/bin/python3

import os
from time import sleep


from enum import Enum


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8


class Symbol(Enum):
    X = 1
    O = 2


class Player():

    def __init__(self, name, symbol):
        if name == '':
            if symbol == 'X':
                self.name = 'Player 1'
            else:
                self.name = 'Player 2'
        else:
            self.name = name

        self.symbol = symbol
        self.score = 0

    def wins(self):
        self.score += 1

    def getScore(self):
        return self.score

    def getSymbol(self):
        return self.symbol

    def switchSymbol(self):
        if self.symbol == 'O':
            self.symbol = 'X'
        else:
            self.symbol = 'O'


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<class=Player(), name={self.name}, score={self.score}>"


class Cell():

    def __init__(self):
        self.value = '_'

    def isOccupied(self):
        if self.value == '_':
            return False
        return True

    def setValue(self, newValue):
        self.value = newValue

    def resetValue(self):
        self.value = '_'

    def getValue(self):
        return self.value


class Board():

    def __init__(self, size):
        self.size = size
        self.cells = [[ Cell() for i in range(size)] for j in range(size)]

    def cell(self, coord_x, coord_y):
        return self.cells[coord_x][coord_y]

    def draw(self):  # updates gaming board
        print('    ', end='')
        for i in range(self.size):
            print(str(i + 1).rjust(3), end='')
        print()


        print("   +", end='')
        for i in range(self.size * 3 + 2):
            print('-', end='')
        print('+')

        for m in range(self.size):
            print(str(m).rjust(2) + " | ", end='')
            for n in range(self.size):
                print(' {} '.format(self.cells[m][n].getValue()), end='')
            print(" |")

        print("   +", end='')
        for i in range(self.size * 3 + 2):
            print('-', end='')
        print('+')

    def outOfBounds(self, x, y):
        return x < 0 or x > self.size or y < 0 or y > self.size

    def check(self, x, y, dir, player):
        if self.outOfBounds(x, y) or board.cell(x, y).getValue() != player.getSymbol():
            return 0
        return self.check(x + dir[0], y + dir[1], dir, player) + 1

    def checkWin(self, x, y, player):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i in range(0, 8, 2):
            if self.check(x, y, dir[i], player) + self.check(x, y, dir[i + 1], player) >= 5 + 1:
                return True
        return False

    def get_coords(self):  # gets coords from input
        while True:
            try:
                f_row, f_column = input('Enter coordinates: ').split()

                if not f_row.isdigit() or not f_column.isdigit():
                    print('You should enter numbers!')
                    continue

                elif (int(f_row) < 1) or (int(f_row) > self.size) or (int(f_column) < 1) or (int(f_column) > self.size):
                    print('Coordinates should be from 1 to 15!')
                    continue

                elif self.cell(int(f_row) - 1, int(f_column) - 1).isOccupied():
                    print('This cell is occupied! Choose another one!')
                    continue

                else:
                    break
            except ValueError:
                print('Wrong input')
            except IndexError:
                print('Coords out of range')

        return int(f_row) - 1, int(f_column) - 1

    def reset(self):
        for row in self.cells:
            for cell in row:
                cell.setValue('_')



def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ------------- main program ---------------------

clearScreen()
board = Board(15)
p1 = Player(input("Enter name of player 1: "), 'X')
p2 = Player(input("Enter name of player 2: "), 'O')




while True:
    clearScreen()

    if p1.getSymbol() == 'X':
        print(f'{p1} begins!')
    else:
        print(f'{p2} begins!')
    sleep(1.5)

    clearScreen()
    board.reset()
    board.draw()
    move = 1




    # ------------ this is where game starts --------------

    while True:
        row, column = board.get_coords()

        if move % 2 != 0:
            board.cell(row, column).setValue('X')
        else:
            board.cell(row, column).setValue('O')

        move += 1
        clearScreen()
        board.draw()

        # ------------------ checking if win -----------------------
        if board.checkWin(row, column, p1):
            p1.wins()
            break
        elif board.checkWin(row, column, p2):
            p2.wins()
            break


    print('\nScore: \n{} vs {}\n{} vs {}\n'.format(p1, p2, p1.getScore(), p2.getScore()))
    selection = input('Do you wish to play again?(y/n)\n')

    if selection.lower() == 'y':
        p1.switchSymbol()
        p2.switchSymbol()
        continue
    elif selection.lower() == 'n':
        print('Bye bye!')
        break
    else:  # toto se mi uz nechtelo dodelavat :D
        print('not y, exiting')
        break
