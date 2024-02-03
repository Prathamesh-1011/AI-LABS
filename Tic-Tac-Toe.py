import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 11)

def check_winner(board):
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            return 'Player 1 (X) wins!'
        if all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            return 'Player 2 (O) wins!'
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'Player 1 (X) wins!'
    if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'Player 2 (O) wins!'
    return None

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def computer_move(board, symbol):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = symbol
            break

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            row = int(input(f"Player {current_player} (row): ")) - 1
            col = int(input(f"Player {current_player} (col): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's move:")
            computer_move(board, 'O')

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(winner)
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()