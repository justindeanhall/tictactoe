from random import randrange

class TicTacToe():
    """A with modles to play TicTacToe"""

    def new_board(self):
        """A module that resets / creates a new board"""

        self.row1 = [' ', ' ', ' ']
        self.row2 = [' ', ' ', ' ']
        self.row3 = [' ', ' ', ' ']

    def show_board(self):
        """A module that shows the current board"""
        print("Current Board:")
        print(self.row1)
        print(self.row2)
        print(self.row3)
        print('\n')

    def request_move_player(self):
        """A module that requests users for thier move"""
        value = 0
        self.complete_row = self.row1 + self.row2 + self.row3
        print("Positions Key:")
        print("['1', '2', '3']")
        print("['4', '5', '6']")
        print("['7', '8', '9']")
        print('\n')

        while value == 0:
            self.user_input = input('Please input your move (1-9): ')
            try:
                self.user_input = int(self.user_input)
                if 1 <= self.user_input <= 9:
                    if self.complete_row[int(self.user_input) - 1] == " ":
                        self.user_input = int(self.user_input)
                        value = 1
                    else:
                        print("Spot taken!")
                else:
                    print("Please input a value from 1-9.")
            except ValueError:
                print("Please input an integer.")

    def update_board_player(self):
        """A module that updates the board with a recorded move for player"""
        # Combine lists into 1 long list
        self.complete_row = self.row1 + self.row2 + self.row3
        # Locate and update the index with X
        self.complete_row[self.user_input - 1] = "X"
        # Seperate complete list into 3 rows
        self.row1 = self.complete_row[0:3]
        self.row2 = self.complete_row[3:6]
        self.row3 = self.complete_row[6:9]

    def request_move_computer(self):
        """A module that decides a move for the computer"""
        self.complete_row = self.row1 + self.row2 + self.row3
        value = 0
        while value == 0:
            move = randrange(1, 9, 1)
            if self.complete_row[move - 1] == " ":
                self.computer_input = move
                value = 1

    def update_board_computer(self):
        """A module that updates the board with a recorded move for computer"""
        # Combine lists into 1 long list
        self.complete_row = self.row1 + self.row2 + self.row3
        # Locate and update the index with X
        self.complete_row[self.computer_input - 1] = "O"
        # Seperate complete list into 3 rows
        self.row1 = self.complete_row[0:3]
        self.row2 = self.complete_row[3:6]
        self.row3 = self.complete_row[6:9]

    def check_board(self):
        """Checks for a win/loss or full board"""
        self.complete_row = self.row1 + self.row2 + self.row3
        print('\n')
        # Check rows
        if self.complete_row[0] == self.complete_row[1] and self.complete_row[0] == self.complete_row[2]:
            if self.complete_row[0] != ' ':
                if self.complete_row[0] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0
        if self.complete_row[3] == self.complete_row[4] and self.complete_row[3] == self.complete_row[5]:
            if self.complete_row[3] != ' ':
                if self.complete_row[3] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0
        if self.complete_row[6] == self.complete_row[7] and self.complete_row[7] == self.complete_row[8]:
            if self.complete_row[6] != ' ':
                if self.complete_row[6] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0

        # Check columns
        if self.complete_row[0] == self.complete_row[3] and self.complete_row[0] == self.complete_row[6]:
            if self.complete_row[0] != ' ':
                if self.complete_row[0] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0
        if self.complete_row[1] == self.complete_row[4] and self.complete_row[1] == self.complete_row[7]:
            if self.complete_row[1] != ' ':
                if self.complete_row[1] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0
        if self.complete_row[2] == self.complete_row[5] and self.complete_row[2] == self.complete_row[8]:
            if self.complete_row[2] != ' ':
                if self.complete_row[2] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0

        # Check diagnals
        if self.complete_row[0] == self.complete_row[4] and self.complete_row[0] == self.complete_row[8]:
            if self.complete_row[0] != ' ':
                if self.complete_row[0] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0
        if self.complete_row[2] == self.complete_row[4] and self.complete_row[2] == self.complete_row[6]:
            if self.complete_row[2] != ' ':
                if self.complete_row[2] == "X":
                    print("Player wins!")
                    return 0
                else:
                    print("Computer wins!")
                    return 0

        # Check full board
        if self.complete_row[0] != " " and self.complete_row[1] != " " and \
        self.complete_row[2] != " " and self.complete_row[3] != " " and \
        self.complete_row[4] != " " and self.complete_row[5] != " " and \
        self.complete_row[6] != " " and self.complete_row[7] != " " and \
        self.complete_row[8] != " ":
            print("Yal losers!")
            return 0

        else:
            return 1
