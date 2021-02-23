import numpy

board = numpy.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
p1symbol = 'X'
p2symbol = 'O'


def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1

        if count == 3:
            print(symbol, "won")
            return True
    return False


def check_columns(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1

        if count == 3:
            print(symbol, "won")
            return True
    return False


def check_diagonals(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        print(symbol, "won")
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        print(symbol, "won")
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)


def place(symbol):
    print(numpy.matrix(board))
    while 1:
        row = int(input("Enter row position (1/2/3): "))
        column = int(input("Enter column position (1/2/3): "))
        if 0 < row < 4 and 0 < column < 4 and board[row - 1][column - 1] == '-':
            break

        else:
            print("Invalid input. Please enter again.")

    board[row-1][column-1] = symbol


def play():
    for turn in range(9):  # 3x3 matrix (9 cells in the board)
        if turn % 2 == 0:
            print("X turn")
            place(p1symbol)
            if won(p1symbol):
                break

        else:
            print("O turn")
            place(p2symbol)
            if won(p2symbol):
                break

    if not won(p1symbol) and not won(p2symbol):
        print("Draw")


play()
