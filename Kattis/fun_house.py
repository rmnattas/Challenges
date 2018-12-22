

def go(size, board, enter, move):
    while True:
        if move == 0:
            enter[0] += 1
        elif move == 1:
            enter[0] -= 1
        elif move == 2:
            enter[1] += 1
        elif move == 3:
            enter[1] -= 1

        if board[enter[0]][enter[1]] == "x":
            board[enter[0]][enter[1]] = "&"
            break
        elif board[enter[0]][enter[1]] == "/":
            if move == 0:
                move = 3
            elif move == 1:
                move = 2
            elif move == 2:
                move = 1
            elif move == 3:
                move = 0
        elif board[enter[0]][enter[1]] == "\\":
            if move == 0:
                move = 2
            elif move == 1:
                move = 3
            elif move == 2:
                move = 0
            elif move == 3:
                move = 1


def print_board(board):
    for row in board:
        print("".join(row))

i=0
while True:
    size = [int(x) for x in input().split()]
    if size[0] == 0 and size[1] == 0:
        break
    board = []
    enter_row = 0
    for j in range(size[1]):
        row = list(input())
        board.append(row)
        if "*" in row:
            enter_row = j

    print("HOUSE", i+1)
    if enter_row == 0:
        enter = [enter_row, board[enter_row].index("*")]
        go(size, board, enter, 0)
        print_board(board)
    elif enter_row == len(board)-1:
        enter =	[enter_row, board[enter_row].index("*")]
        go(size, board, enter, 1)
        print_board(board)
    else:

        if board[enter_row].index("*") == 0:
            enter = [enter_row, board[enter_row].index("*")]
            go(size, board, enter, 2)
            print_board(board)
        else:
            enter = [enter_row, board[enter_row].index("*")]
            go(size, board, enter, 3)
            print_board(board)
    i+=1
