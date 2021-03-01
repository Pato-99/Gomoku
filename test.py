#!/usr/bin/python3

import sys
import pygame as pg
import time


SCREENSIZE = 750, 750



class Player:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.score = 0

    def wins(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_symbol(self):
        return self.number

    def switch_symbol(self):
        self.number = 1 if self.number != 1 else 0

    def __str__(self):
        return self.name


class Board:

    def __init__(self, size):
        self.size = size
        self.cells = [[-1 for i in range(size)] for j in range(size)]

    def is_occupied(self, x, y):
        if self.cells[x][y] != -1:
            return True
        return False

    def out_of_bounds(self, x, y):
        return x < 0 or x >= self.size or y < 0 or y >= self.size

    def check(self, x, y, direction, player):
        if self.out_of_bounds(x, y) or self.cells[x][y] != player:
            return 0
        return self.check(x + direction[0], y + direction[1], direction, player) + 1

    def check_win(self, x, y, player):
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i in range(0, 8, 2):
            if self.check(x, y, direction[i], player) + self.check(x, y, direction[i + 1], player) >= 5 + 1:
                return True
        return False

    def reset(self):
        self.cells = [[ -1 for i in range(self.size)] for j in range(self.size)]

    def draw(self):
        screen.fill(pg.Color("white"))

        for i in range(1, self.size):
            pg.draw.line(screen, pg.Color("black"), (0, i * 50), (SCREENSIZE[0], i * 50), 5)

        for i in range(1, self.size):
            pg.draw.line(screen, pg.Color("black"), (i * 50, 0), (i * 50, SCREENSIZE[0]), 5)

        for i in range(1, self.size):
            for j in range(1, self.size):
                if self.cells[i][j] == 0:
                    pg.draw.circle(screen, pg.Color("blue"), (25 + 50 * j, 25 + 50 * i), 20, 7)
                elif self.cells[i][j] == 1:
                    pg.draw.line(screen, pg.Color("red"), (10 + 50 * j, 10 + 50 * i), (40 + 50 * j, 40 + 50 * i), 9)
                    pg.draw.line(screen, pg.Color("red"), (40 + 50 * j, 10 + 50 * i), (10 + 50 * j, 40 + 50 * i), 9)




# ----------------- main -----------------

pg.init()
screen = pg.display.set_mode(SCREENSIZE)
board = Board(15)
move = 1

board.draw()
pg.display.flip()

end = False
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            row = y // 50
            col = x // 50
            if not board.is_occupied(row, col) and not end:
                board.cells[row][col] = move % 2

                if board.check_win(row, col, 1):
                    print("X wins")
                    end = True
                elif board.check_win(row, col, 0):
                    print("O wins")
                    end = True

                move += 1

            elif end:
                end = False
                board.reset()
                move = 1

            board.draw()
            pg.display.flip()

    time.sleep(0.01)


