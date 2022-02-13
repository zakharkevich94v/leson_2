# tic tac toe game
# the computer is playing against the user
X = "X"
O = "O"
EMPTY = " "
TIE = "Draw"
NUM_SQUARES = 25


def display_instruction():
    """Outputs instructions for the player"""
    print("""
    Tic Tac Toe game 
    To make a move, enter a number from 0 to 24.
    The numbers correspond to the fields of the board - as shown below:\n
                0  | 1  | 2  | 3  | 4  |
                ------------------------
                5  | 6  | 7  | 8  | 9  |
                ------------------------
                10 | 11 | 12 | 13 | 14 |
                ------------------------
                15 | 16 | 17 | 18 | 19 |
                ------------------------
                20 | 21 | 22 | 23 | 24 | 
    """)


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n):")
    if go_first == "y":
        print("Then take the first move.  You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0],"|",board[1],"|",board[2],"|",board[3],"|",board[4])
    print("\t", "----------------")
    print("\t", board[5],"|",board[6], "|",board[7], "|",board[8],"|",board[9])
    print("\t", "----------------")
    print("\t", board[10],"|",board[11],"|",board[12],"|",board[13],"|",board[14])
    print("\t", "----------------")
    print("\t", board[15],"|",board[16],"|",board[17],"|",board[18],"|",board[19])
    print("\t", "----------------")
    print("\t", board[20],"|",board[21],"|",board[22],"|",board[23],"|",board[24], "\n")


def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2, 3, 4),
                   (5, 6, 7, 8, 9),
                   (10, 11, 12, 13, 14),
                   (15, 16, 17, 18, 19),
                   (20, 21, 22, 23, 24),
                   (4, 9, 14, 19, 24),
                   (3, 8, 13, 18, 23),
                   (2, 7, 12, 17, 22),
                   (1, 6, 11, 16, 21),
                   (0, 5, 10, 15, 20),
                   (0, 6, 12, 18, 24),
                   (4, 8, 12, 16, 20))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] == board[row[3]] == board[row[4]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Get human move."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 24):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human.  Choose another.\n")
    print("Fine...")
    return move


def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (12, 0, 4, 20, 24, 5, 15, 19, 17, 3, 16, 8, 11, 6, 13)

    print("I shall take square number", end=" ")
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")


def main():
    display_instruction()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program
main()
# end the program
input("\n\nPress the enter key to quit.")
