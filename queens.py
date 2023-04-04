import random
def print_board(board_size=8):
    """
    Prints a chess board of given size
    """
    for _ in range(board_size):
        print('|', '|'.join(['---']*board_size), '|',sep='')
        print('|', '|'.join(['...']*board_size), '|',sep='')
    print('|', '|'.join(['---']*board_size), '|',sep='')


def validate_board(board):
    rows = len(board)
    for row in board:
        assert rows == len(row),"Invalid board dimension"

def decode_position(pos, board_size):
    row, col = int(pos.upper()[1]), ord(pos.upper()[0])
    return (board_size - row, col - ord('A'))

def is_valid_move(board, pos_coord):
    all_moves = find_all_moves(pos_coord, len(board))
    for move in all_moves:
        if board[move[0]][move[1]] == 'Q':
            return False

    return True


def find_all_moves(pos_coord, board_size):
    all_moves = []
    
    # vertical
    x_pos = pos_coord[0]
    while x_pos >= 0:
        all_moves.append((x_pos, pos_coord[1]))
        x_pos -= 1

    x_pos = pos_coord[0]
    while x_pos < board_size:
        all_moves.append((x_pos, pos_coord[1]))
        x_pos += 1

    # horizontal
    y_pos = pos_coord[1]
    while y_pos >= 0:
        all_moves.append((pos_coord[0], y_pos))
        y_pos -= 1

    y_pos = pos_coord[1]
    while y_pos < board_size:
        all_moves.append((pos_coord[0], y_pos))
        y_pos += 1

    # diagonals
    x_pos = pos_coord[0]
    y_pos = pos_coord[1]

    while x_pos > -1 and y_pos > -1:
         all_moves.append((x_pos, y_pos))
         x_pos -= 1
         y_pos -= 1

    x_pos = pos_coord[0]
    y_pos = pos_coord[1]

    while x_pos < board_size and y_pos < board_size:
         all_moves.append((x_pos, y_pos))
         x_pos += 1
         y_pos += 1

    x_pos = pos_coord[0]
    y_pos = pos_coord[1]

    while x_pos > -1 and y_pos < board_size:
         all_moves.append((x_pos, y_pos))
         x_pos -= 1
         y_pos += 1

    x_pos = pos_coord[0]
    y_pos = pos_coord[1]

    while x_pos < board_size and y_pos > -1:
         all_moves.append((x_pos, y_pos))
         x_pos += 1
         y_pos -= 1
    
    return all_moves

def update_all(board, mask, pos_coord, update_char):
    validate_board(board)
    mask_fill = 1 if update_char == ' ' else 0
    update_pos_list = find_all_moves(pos_coord, len(board))
    for update_pos in update_pos_list:
        mask[update_pos[0]][update_pos[1]] = mask_fill
    
    board[pos_coord[0]][pos_coord[1]] = update_char

    return board,mask


def print_board(board):
    validate_board(board)
    board_size = len(board)

    print('   ', '   '.join(list('ABCDEFGH')), '  ',sep='')
    for i,row in enumerate(board):
        print(' |', '|'.join(['---']*board_size), '|',sep='')
        print(board_size-i,'|', '|'.join(list(map(lambda x : f' {str(x) } ', row))), '|',board_size-i,sep='')
    print(' |', '|'.join(['---']*board_size), '|',sep='')
    print('   ', '   '.join(list('ABCDEFGH')), '  ',sep='')

def initialize_board(board_size):
    board = [[' ']*board_size for _ in range(board_size) ]
    mask = [[1]*board_size for _ in range(board_size) ]
    return board,mask

def solve_board(board_size):
    board, mask = initialize_board(board_size)
    queens_pos_queue = []
    row_num = 0
    col_num = random.randint(0, board_size-1)
    while row_num < board_size and row_num > -1:
        while col_num < board_size and col_num > -1:
            pos_coord = (row_num, col_num)
            if is_valid_move(board, pos_coord):
                board, mask = update_all(board, mask, pos_coord, 'Q')
                queens_pos_queue.append((row_num, col_num))
                row_num += 1
                col_num = 0
                break
            else:
                col_num+=1
        if col_num == board_size:
            row_num+=1
        if row_num  != len(queens_pos_queue):
            if len(queens_pos_queue) > 0:
                row_num, col_num = queens_pos_queue.pop()
                board, mask = update_all(board, mask, (row_num, col_num), ' ')
                col_num += 1
            else:
                row_num = 0
                col_num = 0

    if len(queens_pos_queue) == board_size:
        print_board(board)
    else:
        print("Failed")

        

if __name__ == '__main__':
    solve_board(8)
    

    