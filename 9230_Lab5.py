import random

# Tic Tac Toe board represented as a 2D array
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Function to print the Tic Tac Toe board
def print_board():
    print("   |   |   ")
    print(" "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" ")
    print("   |   |   ")

# Function to check if the game is over
def game_over():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    # Check for tie
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

# Function to make the computer's move
def computer_move():
    # Check for winning move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if game_over():
                    return
                else:
                    board[row][col] = " "
    
    # Check for blocking move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if game_over():
                    board[row][col] = "O"
                    return
                else:
                    board[row][col] = " "
    
    # Make a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            return

# Main game loop
while True:
    print_board()
    computer_move()
    if game_over():
        print_board()
        print("Game over!")
        break
    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): "))
