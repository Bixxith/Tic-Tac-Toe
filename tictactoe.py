# Zachary Niehoff
# SDEV220
# Tic Tac Toe Game
# Due September 13th, 2021

# a class that contains the "gameboard" numbers.  It has to be a class in order to copy the variables and create a new gameboard after each game, otherwise the gameboard would carry over between games
class GameBoard:
    def __init__(self):
        self.GB2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def gbPrint(gbInstance):
    print(f" {gbInstance[7]} | {gbInstance[8]} | {gbInstance[9]}")
    print('---+---+---')
    print(f" {gbInstance[4]} | {gbInstance[5]} | {gbInstance[6]}")
    print('---+---+---')
    print(f" {gbInstance[1]} | {gbInstance[2]} | {gbInstance[3]}")


def gbEnd(gbInstance, turn):
    gbPrint(gbInstance)
    print('\nGame Over\n')
    print(f"{turn}'s won")
    gbAgain = input("Play again? Enter 'y' to continue or anything else to exit")
    if gbAgain == 'y':
        game()
    else:
        exit()


def game():
    gbInstance = GameBoard().GB2
    turn = 'X'
    count = 0
    for i in range(10):
        gbPrint(gbInstance)
        print(f"\nIt is {turn}'s turn.")
        move = int(input(f"Please select a number to place your {turn}: "))

        if gbInstance[move] != 'X' and gbInstance[move] != 'O':
            gbInstance[move] = turn
            count += 1
        else:
            print('\nInvalid placement or input.  Please select a number that is available on the board.\n')
            continue
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

        if count == 9:
            print('\nGame Over\n')
            print("It's a tie!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()
