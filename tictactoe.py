# Zachary Niehoff
# SDEV220
# Tic Tac Toe Game
# Due September 13th, 2021

# a class that contains the "gameboard" numbers.  It has to be a class in order to copy the variables and create a
# new gameboard after each game, otherwise the gameboard would carry over between games
class GameBoard:
    def __init__(self):
        self.GB2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# aligns the numbers/xo's into a grid
def gbPrint(gbInstance):
    print(f" {gbInstance[7]} | {gbInstance[8]} | {gbInstance[9]}")
    print('---+---+---')
    print(f" {gbInstance[4]} | {gbInstance[5]} | {gbInstance[6]}")
    print('---+---+---')
    print(f" {gbInstance[1]} | {gbInstance[2]} | {gbInstance[3]}")


# after 5 turns it is possible to have a winner, if a winner is found than this announces it and loops the game
def gbEnd(gbInstance, turn):
    gbPrint(gbInstance)
    print('\nGame Over\n')
    print(f"{turn}'s won")
    playAgain()


# main function for the game
def playAgain():
    gbAgain = input("Play again? Enter 'y' to continue or anything else to exit")
    if gbAgain == 'y':
        game()
    else:
        exit()


def game():
    # creates an object from the Gameboard class
    gbInstance = GameBoard().GB2
    # sets the inital turn
    turn = 'X'
    # counts the number of turns
    count = 0
    # makes sure it loops through at least enough times to come to a draw
    for i in range(10):
        gbPrint(gbInstance)
        print(f"\nIt is {turn}'s turn.")

        # has the user input a number 1-9
        move = int(input(f"Please select a number to place your {turn}: "))

        # makes sure the move is valid and that the space isn't already taken
        if gbInstance[move] != 'X' and gbInstance[move] != 'O':
            gbInstance[move] = turn
            count += 1
        else:
            print('\nInvalid placement or input.  Please select a number that is available on the board.\n')
            continue

        # checks for win conditions
        if count >= 5:
            if gbInstance[7] == gbInstance[8] == gbInstance[9] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[4] == gbInstance[5] == gbInstance[6] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[1] == gbInstance[2] == gbInstance[3] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[1] == gbInstance[4] == gbInstance[7] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[2] == gbInstance[5] == gbInstance[8] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[3] == gbInstance[6] == gbInstance[9] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[7] == gbInstance[5] == gbInstance[3] != ' ':
                gbEnd(gbInstance, turn)
            elif gbInstance[1] == gbInstance[5] == gbInstance[9] != ' ':
                gbEnd(gbInstance, turn)
        # announces the game is a tie after the board is full and no win condition was met
        if count == 9:
            print('\nGame Over\n')
            print("It's a tie!")
            playAgain()
        # alternates turns
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()
