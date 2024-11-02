'''Info'''
# Name: Venkata Siva Reddy Naga
# UFID: 97561398
# Major: Applied Data Science

"""Description: Connect 4 is a game where players select a color and alternately drop colored tokens into a vertically suspended grid with six rows and seven columns. 
                This straightforward game can be played by two players using the same keyboard. 
                It is designed to initiate a new game, prompt users for their moves while displaying available options, update the game board, manage incorrect inputs, and determine the winners, as illustrated in the sample output."""


# Create an empty 6x7 board filled with spaces
def resetBoard():
    return [[' ' for _ in range(7)] for _ in range(6)]

# Used for displaying the current state of the board
def printBoard(board): 
    for i in range(5, -1, -1):  # Start from top row (5) to bottom row (0)
        print(f"| {i+1} |", end="")  # Print row number
        for j in range(7):  # Print each cell in the row
            print(f" {board[i][j]} |", end="")
        print()  # Move to next line
        print('----------------------------------')  # Separator line
    print("|R/C| a | b | c | d | e | f | g |")  # Print column labels
    print('----------------------------------')

# Check if a move is valid (within board and cell is empty)
def validateEntry(board, column, row):
    if column < 0 or column > 6 or row < 0 or row > 5:
        return False  # Out of board boundaries
    return board[row][column] == ' '  # Check if cell is empty

# Find all available positions on the board
def availablePosition(board):
    available = []
    for col in range(7):
        for row in range(6):
            if board[row][col] == ' ':  # Checks if cell is empty
                available.append(f"{chr(97+col)}{row+1}")  # Add position (e.g., 'a1')
                break  # Move to next column
    return available

# Check if the current player has won
def checkWin(board, turn):
    # Checks in the direction of horizontal and vertical wins
    for row in range(6):
        for col in range(7):
            # Check horizontal win (4 in a row)
            if col <= 3 and all(board[row][col+i] == turn for i in range(4)):
                return True
            # Check vertical win (4 in a column)
            if row <= 2 and all(board[row+i][col] == turn for i in range(4)):
                return True
   
    # Checks in the diagonal wins
    for row in range(3):
        for col in range(4):
            # Check positive slope diagonal
            if all(board[row+i][col+i] == turn for i in range(4)):
                return True
            # Check negative slope diagonal
            if all(board[5-row-i][col+i] == turn for i in range(4)):
                return True
    return False  # No wins found yet

# Main game play function
def play():
    board = resetBoard()  # Start with an empty board
    current_player = 'X'  # X goes first
    selection_count = 0  # Keep track of moves made

    while True:
        printBoard(board)  # prints the current board
        print()
        print(f"{current_player}'s turn.")
        available = availablePosition(board)  # shows available moves
        print("Where do you want your", current_player, "placed?")
        print("Available positions are:", available)
        print()
        
        # Get valid input from player
        while True:
            position = input("Please enter column-letter and row-number (e.g., a1): ").lower()
            if position not in available:
                print("Invalid move. Try again.")
            else:
                selection_count += 1
                break

        # Convert input to board coordinates(easy to track and placing variables)
        column = ord(position[0]) - 97  # Convert letter to number (a=0, b=1, etc.)
        row = int(position[1]) - 1  # Convert to 0-based index

        board[row][column] = current_player  # Place the player's choice in position
        print("Thank you for your selection.")

        if checkWin(board, current_player):  # Check if current player won
            print(f"{current_player} IS THE WINNER!!!")
            print("\n")
            printBoard(board)
            break
        elif selection_count == 42:  # There will be only 42 spaces(6x7=42) if count reaches 42, it is full
            print("\nDRAW! NOBODY WINS!")
            printBoard(board)
            break

        # Switch to other player
        current_player = 'O' if current_player == 'X' else 'X'

    # To play again
    print()
    play_again = input("Another game (y/n)? ").lower()
    return play_again == 'y'

# Main function to start and manage games
def main():
    print("New game: X goes first.")
    print()
    while play():  # Keep playing new games until player chooses not to
        print("New game: X goes first.")
        print()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()