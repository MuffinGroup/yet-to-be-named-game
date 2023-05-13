import random

# Function to create an empty Tic-Tac-Toe board
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to make a player's move
def make_move(board, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

# Function to get the bot's move
def get_bot_move(board, bot_player):
    # Check if bot can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = bot_player
                if check_win(board, bot_player):
                    return row, col
                board[row][col] = ' '

    # Check if player can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                if check_win(board, player):
                    return row, col
                board[row][col] = ' '

    # Choose a random move
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

# Main game loop
def play_game():
    global player  # Declare player as a global variable

    board = create_board()
    players = ['X', 'O']
    player = random.choice(players)
    bot_player = 'O' if player == 'X' else 'X'
    game_over = False

    print(f"Player {player} starts the game!")

    while not game_over:
        display_board(board)

        if player == bot_player:
            print("Bot's turn...")
            row, col = get_bot_move(board, bot_player)
        else:
            print("Your turn...")
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

        if make_move(board, row, col):
            if check_win(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                game_over = True
            elif all(board[row][col] != ' ' for row in range(3) for col in range(3)):
                display_board(board)
                print("It's a tie!")
                game_over = True
            else:
                player = bot_player if player == 'X' else 'X'

play_game()