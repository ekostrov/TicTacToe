from Board import Board
from Player import Player
def main():
    who = True
    win = False
    board = Board()
    player1 = Player('X')
    player2 = Player('O')
    for i in range(9):
        currentPlayer =''
        if who:
            currentPlayer = player1
        else:
            currentPlayer = player2
        board.display()
        row = input(f"Player {currentPlayer.player} choose row: ")
        column = input(f"Player {currentPlayer.player} choose column: ")
        board.update(row,column,currentPlayer.player)
        if board.check_winner():
            print(f"Player {currentPlayer.player} WINS!!!!!!!!")
            win = True
            break
        else:
            who = not who
            
    if not win:
        print("This is a tie!")

if __name__ == '__main__':
    main()




