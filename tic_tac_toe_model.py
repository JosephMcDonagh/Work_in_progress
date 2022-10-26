# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

from collections import namedtuple



# class TicBoard:

#     def __init__(self):
#         GameState = namedtuple('GameState', [f'p_{i}' for i in range(1, 10)])
#         self.current = GameState('-','-', '-', '-', '-', '-', '-', '-', '-')

#     def __str__(self):
#          return f' {self.current.p_1}  {self.current.p_2}  {self.current.p_3} \n {self.current.p_4}  {self.current.p_5}  {self.current.p_6} \n {self.current.p_7}  {self.current.p_8}  {self.current.p_9} '
        
#     def move_x(self, number):
#         self.current = self.current._replace( p_1 = 'X')
    
#     def move_o(self, number):
#         self.current = self.current._replace( p_1 = 'O')


GameState = namedtuple('GameState',['user', 'board'])


class TacBoard:
    def __init__(self):
        self.current = ['-' for i in range(1, 10)]
        self.marker = 'O'

    def __str__(self):
        a = ''
        index = 0
        for i in range(3):
            for j in range(3):
                a += f'{self.current[index]} ' 
                index += 1
            a += '\n'
        return a

    def move_X(self, position):
        self.current[position-1] = 'X'

    def move_O(self, position):
        self.current[position-1] = 'O'
    
    def change_marker(self):
        if self.marker == 'X':
            self.marker = 'O'
        else:
            self.marker = 'X'
    
    def game_over(self):
        winning_positions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2, 5, 8], [3,6,9], [1,5,9], [3,5,7]]
        for winning_line in winning_positions:
            counter = 0
            for i in range(2):
                if self.current[winning_line[i]-1] == self.current[winning_line[i+1]-1] and self.current[winning_line[i]-1] != '-':
                    counter +=1
                if counter == 2:
                    return True
        return False

    def input(self):
        print(self)
        self.change_marker()
        if self.marker == 'X':
            user_input = input('Player 1, what number position do you want to play?  ')
            self.move_X(int(user_input))
        if self.marker == 'O':
            user_input = input('Player 2, what number position do you want to play?  ')
            self.move_O(int(user_input))
    
    def win_msg(self):
        if self.marker == 'X':
            print("Player 1 (X's) wins")
        else:
            print("Player 2 (O's) wins")





