board = []
for _ in range(4):
    board.append([int(x) for x in input().split()])
move = int(input())
    
def line_col(o_line):
    line = o_line[:]
    while 0 in line:
        del line[line.index(0)]

    i = 0
    while i < len(line)-1:
        if line[i] == line[i+1]:
            line[i] *= 2
            line.pop(i+1)
        i += 1

    while len(line) < 4:
        line.append(0)

    return(line)


def print_board():
    for i in range(4):
        print(board[i][0], board[i][1], board[i][2], board[i][3])


if move == 0:
    for i in range(4):
        board[i] = line_col(board[i])
    print_board()

elif move == 1:
    for i in range(4):
        line = []
        for j in range(4):
            line.append(board[j][i])
        new_line = line_col(line)
        for j in range(4):
            board[j][i] = new_line[j]
    print_board()

elif move == 2:
    for i in range(4):
        line = board[i][:]
        line.reverse()
        new_line = line_col(line)
        new_line.reverse()
        board[i] = new_line
        
    print_board()
    
else:
    for i in range(4):
        line = []
        for j in range(4):
            line.append(board[j][i])
        line.reverse()
        new_line = line_col(line)
        new_line.reverse()
        for j in range(4):
            board[j][i]	= new_line[j]
    print_board()







