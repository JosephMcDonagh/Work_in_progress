# Your code to implement the playing of the game here. Impure functions are allowed.

from tic_tac_toe_model import TacBoard

def tic_tac_toe():
    board = TacBoard()
    count = 0
    print('X starts')
    while board.game_over() == False and count < 9:
        board.input()
        count+=1
    print(board)
    if count == 9:
        print('Draw')
    else:
        board.win_msg()
    
    



if __name__ == '__main__':
    tic_tac_toe()