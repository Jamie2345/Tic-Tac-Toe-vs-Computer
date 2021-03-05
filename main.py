# Jamie's noughts and crosses game against computer
# I made this because my dictionary knowledge was bad now its good

# 1 issue that I fixed

'''
    Everything works fine there is one issue where the computer sometimes picks to block instead of winning
    I could fix this by adding a dict of moves that will win or block and if one of there values is means a win pick
    that one.

    Edit:
    This has been added and it is working

    originally I had it so once it found a move it would instantly do that but now it adds all moves to a
    dict and picks the best move out of that dictionary

    there is still one bug where it sometimes gets list index out of range error # unfixable error

    also Ive got it to print all of the moves the computer can make this can be removed at the bottom of code
'''

# Imports

import random  # used to decide some of the computers decisions at the start

# Dictionary for representing the board
board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ', 'middle-l': ' ', 'middle-m': ' ', 'middle-r': ' ', 'bottom-l': ' ', 'bottom-m': ' ', 'bottom-r': ' '}

# ive put it in a class because then I can use self to get what the player and computer are


class Game:

    # Greets the user and starts the game
    def greet(self):
        print("Welcome To Tic Tac Toe!")
        valid_choice = False
        while not valid_choice:  # validating that they chose X or O
            player = input("Do You Want To Be X or O? ")
            self.player = player.upper()  # just so x and o works
            if self.player == "X" or "O":
                valid_choice = True

        # Making O go first

        if self.player == "X":   # if player is x
            self.computer = "O"
            self.computer_turn()  # computer goes first

        else:  # if player is not x  (if player is o)
            print('\n')
            self.print_board()
            self.computer = "X"
            self.user_turn()

    # function to check if there is a draw
    def is_draw(self):
        draw_happened = True
        for k in board:
            if board[k] == ' ':
                draw_happened = False
        if draw_happened:
            print('\n\nIts a Tie')
            quit()   # ends the game

    # function to check if someone won and who won
    def who_won(self):

        '''
        How this works is it checks all rows, columns and diagonals in the board dict for 3 values that are the
        exact same except if they are all ' ' because that means they are empty. it then
        assigns that value to the used_to_find_winner variable,
        if that value is the same as the computer value (x or o) then the computer won
        if not then that means the player has won
        '''

        used_to_find_winner = None

        # Checking if someone won on one of the rows

        if board['top-l'] == board['top-m'] and board['top-m'] == board['top-r'] and board['top-m'] != ' ':  # end part makes it not count if values are ' ' (empty)
            used_to_find_winner = board['top-r']  # could be any of above values as they are the same
        elif board['middle-l'] == board['middle-m'] and board['middle-m'] == board['middle-r'] and board['middle-r'] != ' ':
            used_to_find_winner = board['middle-r']
        elif board['bottom-l'] == board['bottom-m'] and board['bottom-m'] == board['bottom-r'] and board['bottom-r'] != ' ':\
            used_to_find_winner = board['bottom-r']

        # Checking if someone won on one of the columns

        elif board['top-l'] == board['middle-l'] and board['middle-l'] == board['bottom-l'] and board['middle-l'] != ' ':
            used_to_find_winner = board['middle-l']
        elif board['top-m'] == board['middle-m'] and board['middle-m'] == board['bottom-m'] and board['middle-m'] != ' ':
            used_to_find_winner = board['middle-m']
        elif board['top-r'] == board['middle-r'] and board['middle-r'] == board['bottom-r'] and board['middle-r'] != ' ':
            used_to_find_winner = board['middle-r']

        # Checking if someone won on one of the diagonals

        elif board['top-l'] == board['middle-m'] and board['middle-m'] == board['bottom-r'] and board['middle-m'] != ' ':
            used_to_find_winner = board['middle-m']
        elif board['top-r'] == board['middle-m'] and board['middle-m'] == board['bottom-l'] and board['middle-m'] != ' ':
            used_to_find_winner = board['middle-m']

        if used_to_find_winner is not None:  # means some1 has won
            if used_to_find_winner == self.computer:
                print('\nThe Computer Wins')
            else:
                print('\nYou Win!')
            quit()   # stops the code (ends the game)

    # function to add a players x or o to the board
    def add_x_o(self, position, x_or_o):  # makes the value in the board dict a x or o accordingly
        board[position] = x_or_o

    # function to print the board
    def print_board(self):
        print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
        print('-----')
        print(board['middle-l'] + '|' + board['middle-m'] + '|' + board['middle-r'])
        print('-----')
        print(board['bottom-l'] + '|' + board['bottom-m'] + '|' + board['bottom-r'])

    # function for when its the users_turn
    def user_turn(self):
        self.who_won()   # checks if anyone won before continuing
        self.is_draw()   # checks if there is a tie before continuing
        print('\n\n')  # leaves 3 lines between each board image / text
        available_positions = []   # list of all the keys of positions that haven't got a x or o in them available
        for k, v in board.items():  # keys and values in the board dictionary
            if v == ' ': # if the value is ' ' it means its empty because it doesn't have a x or o in it
                available_positions.append(k)

        # creating a string of all the available positions to choose from
        pos_to_choose = ''
        for i in range(len(available_positions) - 1):  # doing this so last position doesn't have a comma at the end
            pos_to_choose += available_positions[i] + ', '
        pos_to_choose += available_positions[len(available_positions) - 1] + ': '

        # validating that they chose a position that's on the board and is empty
        position_valid = False
        while not position_valid:
            choose_position = input("Where do you want to put a {} {} ".format(self.player, pos_to_choose))
            if choose_position in available_positions:
                position_valid = True
                self.add_x_o(choose_position, self.player)
                print('\n\n')
                self.print_board()
                self.computer_turn()

    def computer_turn(self):  # function to decide what to do when its the computer_turn
        self.who_won()  # checks if anyone won before continuing
        self.is_draw()

        all_open_spaces = []  # list of all open spaces for the computer to chose from

        # My strategy for deciding what the computer does

        '''
        Make dictionaries for all rows, columns and diagonals then create lists from those dictionaries
        of occupied spaces and unoccupied spaces and if there are 2 occupied spaces put a X or a O
        (whatever computer is) in the unoccupied space to block or win only if the 2 occupied spaces
        are the same because x o empty  there isn't a need to put a x or o in the empty spot because they
        are different.
        '''

        '''
        I could of just done a whole bunch of ifs to do it but that would have been boring
        '''

        # Making dictionary's for each row

        top_row = {}
        middle_row = {}
        bottom_row = {}

        # adding each key to its dictionary eg. anything that is middle-something goes in the middle_row dictionary ect

        for k, v in board.items():  # keys and values in board
            if v == ' ':  # if space is empty
                all_open_spaces.append(k)  # add the key for that space to the open_spaces list

            if k == 'top-l' or k == 'top-m' or k == 'top-r':  # if key is top-something add it to the top_row dict
                top_row[k] = v
            elif k == 'middle-l' or k == 'middle-m' or k == 'middle-r':  # if key is middle-something add to middle_row
                middle_row[k] = v
            else:  # if key is not middle-something or top-something it is bottom-something so add to bottom_row dict
                bottom_row[k] = v

        # making lists of all unoccupied spaces and occupied spaces in each row to use to decide the best move

        # unoccupied and occupied spaces in top row

        occupied_top_row = []
        unoccupied_top_row = []
        for k, v in top_row.items():
            if v == ' ':  # if its empty
                unoccupied_top_row.append(k)
            else:  # if its not empty
                occupied_top_row.append(k)

        # unoccupied and occupied spaces in middle row

        occupied_mid_row = []
        unoccupied_mid_row = []
        for k, v in middle_row.items():
            if v == ' ':
                unoccupied_mid_row.append(k)
            else:
                occupied_mid_row.append(k)

        # unoccupied and occupied spaces in bottom_row

        occupied_bottom_row = []
        unoccupied_bottom_row = []
        for k, v in bottom_row.items():
            if v == ' ':
                unoccupied_bottom_row.append(k)
            else:
                occupied_bottom_row.append(k)

        # Making dictionary of all columns

        left_column = {}
        middle_column = {}
        right_column = {}

        # adding each key to its correlating dictionary

        for k, v in board.items():
            if k == 'top-l' or k == 'middle-l' or k == 'bottom-l':  # if key is on left side of board add it to left_column dict
                left_column[k] = v
            elif k == 'top-m' or k == 'middle-m' or k == 'bottom-m:':
                middle_column[k] = v
            elif k == 'top-r' or k == 'middle-r' or k == 'bottom-r':
                right_column[k] = v

        # making lists of all occupied and unoccupied spaces in each column

        # occupied and unoccupied spaces in left column

        occupied_left_column = []
        unoccupied_left_column = []
        for k, v in left_column.items():
            if v == ' ':
                unoccupied_left_column.append(k)
            else:
                occupied_left_column.append(k)

        # occupied and unoccupied spaces in middle column

        occupied_middle_column = []
        unoccupied_middle_column = []
        for k, v in middle_column.items():
            if v == ' ':
                unoccupied_middle_column.append(k)
            else:
                occupied_middle_column.append(k)

        # occupied and unoccupied spaces in right column

        occupied_right_column = []
        unoccupied_right_column = []
        for k, v in right_column.items():
            if v == ' ':
                unoccupied_right_column.append(k)
            else:
                occupied_right_column.append(k)

        # making dict of both diagonals

        diagonal_top_left_bottom_right = {}  # diagonal from top left to bottom right
        diagonal_bottom_left_top_right = {}  # diagonal from bottom left to top right

        # adding each key to its dictionary

        for k, v in board.items():
            if k == 'top-l' or k == 'middle-m' or k == 'bottom-r':
                diagonal_top_left_bottom_right[k] = v
            if k == 'bottom-l' or k == 'middle-m' or k == 'top-r':  # didn't use elif because middle-m is in both
                diagonal_bottom_left_top_right[k] = v

        # occupied and unoccupied spaces in diagonal top-l to bottom-r

        occupied_top_left_diagonal = []
        unoccupied_top_left_diagonal = []
        for k, v in diagonal_top_left_bottom_right.items():
            if v == ' ':
                unoccupied_top_left_diagonal.append(k)
            else:
                occupied_top_left_diagonal.append(k)

        # occupied and unoccupied spaces in diagonal bottom-l to top-r

        occupied_bottom_left_diagonal = []
        unoccupied_bottom_left_diagonal = []
        for k, v in diagonal_bottom_left_top_right.items():
            if v == ' ':
                unoccupied_bottom_left_diagonal.append(k)
            else:
                occupied_bottom_left_diagonal.append(k)

        # Computer Choice

        moves = {}

        # How code below works

        '''
            I've made it so If there is two pieces in a row, column or diagonal it checks if those two pieces are the-
            same value and if they are it checks if it will result in a block or win, then it adds the position to
            the moves dictionary and then after it checks if there is any moves that would cause a win and if there is
            it does that move else if there isn't but there is a blocking move it will do that move and if there is no
            winning or blocking move it picks a random move.

        '''

        # Checking rows, columns and diagonals if there is 2 occupied spaces that have the same value in the 2 Xs or 2 Os
        # if so computer places a O or a X in that empty spot depending on if the computer is X or O then passes the turn back to the player

        if len(occupied_top_row) == 2 and board[occupied_top_row[0]] == board[occupied_top_row[1]]:  # second len stops bugs
            position = unoccupied_top_row[0]  # position is the key for the empty spot
            if board[occupied_top_row[0]] == self.computer:
                moves[position] = 'win'  # overrides whatever is there with win
            else:
                if position not in moves:  # because we don't want it twice and we don't want it to override a win
                    moves[position] = 'block'

        if len(occupied_mid_row) == 2 and board[occupied_mid_row[0]] == board[occupied_mid_row[1]]:
            position = unoccupied_mid_row[0]
            if board[occupied_mid_row[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_bottom_row) == 2 and board[occupied_bottom_row[0]] == board[occupied_bottom_row[1]]:
            position = unoccupied_bottom_row[0]
            if board[occupied_mid_row[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_left_column) == 2 and board[occupied_left_column[0]] == board[occupied_left_column[1]]:
            position = unoccupied_left_column[0]
            if board[occupied_left_column[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_middle_column) == 2 and board[occupied_middle_column[0]] == board[occupied_middle_column[1]]:
            position = unoccupied_middle_column[0]
            if board[occupied_middle_column[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_right_column) == 2 and board[occupied_right_column[0]] == board[occupied_right_column[1]]:
            position = unoccupied_right_column[0]
            if board[occupied_right_column[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_top_left_diagonal) == 2 and board[occupied_top_left_diagonal[0]] == board[occupied_top_left_diagonal[1]]:
            position = unoccupied_top_left_diagonal[0]
            if board[occupied_top_left_diagonal[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        if len(occupied_bottom_left_diagonal) == 2 and board[occupied_bottom_left_diagonal[0]] == board[occupied_bottom_left_diagonal[1]]:
            position = unoccupied_bottom_left_diagonal[0]
            if board[occupied_bottom_left_diagonal[0]] == self.computer:
                moves[position] = 'win'
            else:
                if position not in moves:
                    moves[position] = 'block'

        # choosing what move to do out of moves dict

        chosen_move = None

        # checking if there is a win opportunity first
        for k, v in moves.items():
            if v == 'win':
                chosen_move = k   # they chosen_move is the k eg. top_middle it will then put a x or cross in the top_middle

        # if not a win opportunity check if there is a block opportunity
        if chosen_move is None:
            for k in moves:  # value isn't needed as if there is no win and still values in the dict they must be blocks
                chosen_move = k

        # if its still none it means there is no best move so I've made it just pick a random move from all_open_spaces
        if chosen_move is None:
            chosen_move = random.choice(all_open_spaces)

        print('\n')
        print('\n')
        self.add_x_o(position=chosen_move, x_or_o=self.computer)
        self.print_board()
        self.user_turn()


c = Game()
c.greet()  # greets the user and starts game because all functions are linked








