def occupied(field, x, y):  # checks if place is occupied
    if field[x][y] != 'X' and field[x][y] != 'O':
        return False
    else:
        return True


def get_coords(field):  # gets coords from input
    while True:
        try:
            f_row, f_column = input('Enter coordinates: ').split()

            if not f_row.isdigit() or not f_column.isdigit():
                print('You should enter numbers!')
                continue

            elif (int(f_row) < 1) or (int(f_row) > 15) or (int(f_column) < 1) or (int(f_column) > 15):
                print('Coordinates should be from 1 to 15!')
                continue

            elif occupied(field, int(f_row) - 1, int(f_column) - 1):
                print('This cell is occupied! Choose another one!')
                continue

            else:
                break
        except ValueError:
            print('Wrong input')
        except IndexError:
            print('Coords out of range')

    return int(f_row) - 1, int(f_column) - 1


def draw_board(field):  # updates gaming board
    print('-------------------------------------------------')

    for n in range(15):
        print('|  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  |'.format(field[n][0], field[n][1],
                                                                                        field[n][2], field[n][3],
                                                                                        field[n][4], field[n][5],
                                                                                        field[n][6], field[n][7],
                                                                                        field[n][8], field[n][9],
                                                                                        field[n][10], field[n][11],
                                                                                        field[n][12], field[n][13],
                                                                                        field[n][14]))

    print('-------------------------------------------------')


'''def spaces_check(field):
    for f_row in field:
        if '_' in f_row:
            return True
    return False'''


'''def one_symbol_count(field, one_symbol):
    count = 0
    for f_row in field:
        for symbol in f_row:
            if symbol == one_symbol:
                count += 1
    return count'''

# -------------- functions that are checking win conditions --------------


def check_row(symbol, pos_row, pos_column, board):
    right_count = 0
    left_count = 0

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        right_count += 1
        if temp_column == 14:
            break
        else:
            temp_column += 1

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        left_count += 1
        if temp_column == 0:
            break
        else:
            temp_column -= 1

    if right_count + left_count - 1 >= 5:
        return True
    else:
        return False


'''def check_column(symbol, pos_row, pos_column, board):
    up_count = 0
    down_count = 0

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        down_count += 1
        if temp_row == 14:
            break
        else:
            temp_row += 1

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        up_count += 1
        if temp_row == 0:
            break
        else:
            temp_row -= 1

    if up_count + down_count - 1 >= 5:
        return True
    else:
        return False'''


def check_diagonal_1(symbol, pos_row, pos_column, board):
    right_count = 0
    left_count = 0

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        right_count += 1
        if temp_column == 14 or temp_row == 14:
            break
        else:
            temp_column += 1
            temp_row += 1

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        left_count += 1
        if temp_column == 0 or temp_row == 0:
            break
        else:
            temp_column -= 1
            temp_row -= 1

    if right_count + left_count - 1 >= 5:
        return True
    else:
        return False


def check_diagonal_2(symbol, pos_row, pos_column, board):
    right_count = 0
    left_count = 0

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        right_count += 1
        if temp_column == 14 or temp_row == 0:
            break
        else:
            temp_column += 1
            temp_row -= 1

    temp_row = pos_row
    temp_column = pos_column

    while board[temp_row][temp_column] == symbol:
        left_count += 1
        if temp_column == 0 or temp_row == 14:
            break
        else:
            temp_column -= 1
            temp_row += 1

    if right_count + left_count - 1 >= 5:
        return True
    else:
        return False


def win(symbol, pos_row, pos_column, board):
    if (
        check_row(symbol, pos_column, pos_row, board)
        or check_row(symbol, pos_row, pos_column, board)
        or check_diagonal_1(symbol, pos_row, pos_column, board)
        or check_diagonal_2(symbol, pos_row, pos_column, board)
    ):

        return True


# ------------- main program ---------------------

x_wins = 0
o_wins = 0

while True:
    cells = ['_' for i in range(15 ** 2)]  # setting up plain board
    nested_cells = []
    for i in range(0, len(cells), 15):
        nested_cells.append([cells[i], cells[i + 1], cells[i + 2], cells[i + 3], cells[i + 4],
                             cells[i + 5], cells[i + 6], cells[i + 7], cells[i + 8], cells[i + 9],
                             cells[i + 10], cells[i + 11], cells[i + 12], cells[i + 13], cells[i + 14]])

    draw_board(nested_cells)
    move = 1

# ------------ this is where game starts --------------

    while True:
        row, column = get_coords(nested_cells)

        if move % 2 != 0:
            nested_cells[row][column] = 'X'
        else:
            nested_cells[row][column] = 'O'

        move += 1
        draw_board(nested_cells)

        # ------------------ checking if win -----------------------
        if win('X', row, column, nested_cells):
            print('X wins')
            x_wins += 1
            break
        elif win('O', row, column, nested_cells):
            print('O wins')
            o_wins += 1
            break

    print('\nScore: \nX vs Y\n{} vs {}\n'.format(x_wins, o_wins))
    selection = input('Do you wish to play again?(y/n)\n')

    if selection.lower() == 'y':
        continue
    elif selection.lower() == 'n':
        print('Bye bye!')
        break
    else:  # toto se mi uz nechtelo dodelavat :D
        print('not y, exiting')
        break
