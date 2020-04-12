# Import tictactoe
from tictactoe import TicTacToe
ttt = TicTacToe()

# Create new board
ttt.new_board()


# Run tictactoe
while True:

    while True:
        ttt.show_board()
        ttt.request_move_player()
        ttt.update_board_player()
        value = ttt.check_board()
        if value == 0:
            print('\n')
            ttt.show_board()
            break
        ttt.request_move_computer()
        ttt.update_board_computer()
        value = ttt.check_board()
        if value == 0:
            print('\n')
            ttt.show_board()
            break

    # Offer reply
    play_request = input('Type "y" to play again or anything else to quit: ')
    if play_request == 'y':
        ttt.new_board()
    else:
        break
