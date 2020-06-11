class Board:
    def __init__(self):
        self.board = [['*','*','*'],['*','*','*'],['*','*','*']]

    def display(self):
        print('--------')
        print(" -1-2-3-")
        for i in range(3):
            string_to_print = str(i+1)+' '
            for j in range(3):
                string_to_print += self.board[i][j]+" "
            print(string_to_print)
        print('--------')
    def update(self,row,column,symbol='*'):
        column = int(column) - 1
        row = int(row) - 1
        self.board[row][column] = symbol

    def check_winner(self,symbol='X'):
        if symbol == self.board[0][0] and symbol == self.board[1][1] and symbol == self.board[2][2]:
            return True
        if symbol == self.board[2][0] and symbol == self.board[1][1] and symbol == self.board[0][2]:
            return True
        if symbol == self.board[0][0] and symbol == self.board[1][0] and symbol == self.board[2][0]:
            return True
        if symbol == self.board[0][1] and symbol == self.board[1][1] and symbol == self.board[2][1]:
            return True
        if symbol == self.board[0][2] and symbol == self.board[1][2] and symbol == self.board[2][2]:
            return True
        if symbol == self.board[0][0] and symbol == self.board[0][1] and symbol == self.board[0][2]:
            return True
        if symbol == self.board[1][0] and symbol == self.board[1][1] and symbol == self.board[1][2]:
            return True
        if symbol == self.board[2][0] and symbol == self.board[2][1] and symbol == self.board[2][2]:
            return True
            
        return False



