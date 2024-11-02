'''Info'''
# Name: Venkata Siva Reddy Naga
# UFID: 97561398
# Major: Applied Data Science

"""Description: This Tic Tac Toe game is played on a 3x3 grid by two players who take turns placing their marks, X and O, in the available spaces. 
                The game is designed to initiate a new round, prompt users for their moves, update the game board accordingly, manage incorrect inputs, and identify the winners, as demonstrated in the sample output."""


def Empty_Board(): # This is main separate board for representing X an O
    # Create and return a 3x3 empty board
    return [[" " for _ in range(3)] for _ in range(3)]
    
def Board_pattern(board):
    # Create a formatted representation of the board with row and column labels
    board_form = ["|R\C| 0 | 1 | 2 |"]
    for i in range(3):
        board_form.append([f"| {i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |"])
    return board_form
    
def validate_player_entry(row, column, current_board):
    # Check if the player's move is valid or not
    if row < 0  or row > 2 or column > 2 or column < 0:
        print("Invalid entry: try again. \nRow & column numbers must be either 0, 1, or 2.")
        return 0
    if current_board[row][column] != " ": # If it is not a empty string 
        print("That cell is already taken. \nPlease make another selection.")
        return 0
    return 1

def pattern_print(board): # It is using to print the board in the given format.
    # Print the formatted board
    res = Board_pattern(board)
    for i in range(4):
        print("------------------")
        if i==0:
            print(*res[0], sep="")
        else:
            print(*res[i])
    print("------------------")

def win(board, player):
    """Check if the current player has won."""
    # Here i am checking rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Here i am checking diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main_game():
    while True:
        current_player = "X" # Intitially the player will be X 
        selection_count = 0  # It will be used for checking whether the board is full or not.

        print("New Game: X goes first.")
        print()
        board = Empty_Board()
        pattern_print(board)
        
        while True:
            print()
            print(f"{current_player}'s turn.")
            position = input(f"Where do you want your {current_player} placed? \nPlease enter row number and column number separated by a comma.\n")

            try:
                # Parse player input
                row, column = map(int, position.split(","))
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
                continue
            print(f"You have entered row #{row}")
            print(f"and column #{column}")
            
            # Validate and make the move
            if validate_player_entry(row, column, board):
                board[row][column] = current_player
                selection_count += 1
            else:
                continue
            
            print("Thank you for your selection.")
            pattern_print(board)

            # Check for win or draw
            if win(board, current_player):
                print(f"{current_player} IS THE WINNER!!!")
                pattern_print(board)
                break
            elif selection_count == 9:
                print("DRAW! NOBODY WINS!")
                pattern_print(board)
                break
            
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            
        # Ask if players want to play another game
        another_game = input("\nAnother game? Enter Y or y for yes.\n")
        if another_game.lower() != 'y':
            print("Thank you for playing!")
            break
        
if __name__ == "__main__":
    main_game()