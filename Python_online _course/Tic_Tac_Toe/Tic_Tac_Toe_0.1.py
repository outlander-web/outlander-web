from random import randrange
board = [[1,4,7],[2,'X',8],[3,6,9]]

def display_board(board):
    for i in range(3):
        print('+','+','+','+', sep = '-'*7)
        print('|','|','|','|', sep = ' '*7)
        print('|',board[0][i],'|',board[1][i],'|',board[2][i],'|', sep = ' '*3)
        print('|','|','|','|', sep = ' '*7)
    print('+','+','+','+', sep = '-'*7)

def enter_move(board):
    O = int(input("Enter your move: "))
    if O < 1 or O > 9:
        print("You can only put an integer from 1 to 9")
    elif O % 3 == 0: 
        board[2] = [n if n != O else "O" for n in board[2]]
    elif O % 2 == 0 and O != 4:
        board[1] = [n if n != O else "O" for n in board[1]]
    else:
        board[0] = [n if n != O else "O" for n in board[0]]

def make_list_of_free_fields(board):
    list_of_free_fields = []
    for i_1 in range(len(board)):
        for i_2 in range(len(board[i_1])):
            if type(board[i_1][i_2]) != int:
                continue
            else:
                list_of_free_fields.append((i_1, i_2))
    return list_of_free_fields

def victory_for(board,sign):
    diagonal_1 = diagonal_2 = True
    for itr in range(3):
        if board[itr][0] == sign and board[itr][1] == sign and board[itr][2] == sign:
            return True
        if board[0][itr] == sign and board[1][itr] == sign and board[2][itr] == sign:
            return True
        if board[itr][itr] != sign:
            diagonal_1 = False
        if board[2 - itr][2 - itr] != sign:
            diagonal_2 = False
    if diagonal_1 or diagonal_2:
        return True
    return 
    
def draw_move(board):
    X_list = make_list_of_free_fields(board)
    Random_tuple = randrange(len(X_list))
    tup = X_list[Random_tuple]
    board[tup[0]][tup[1]] = "X"
    
for i in range(10):
    display_board(board)
    enter_move(board)
    draw_move(board)
    if victory_for(board, "O"):
        print("I won!")
    elif victory_for(board, "X"):
        print("You won!")
    else:
        continue