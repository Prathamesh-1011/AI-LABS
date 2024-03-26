import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    # Check if the board is full
    if any('-' in row for row in board):
        return None
    else:
        return 'Draw'

def min_max(board, depth, is_maximizing):
    result = evaluate(board)

    if result is not None:
        if result == 'X':
            return -10 + depth, None
        elif result == 'O':
            return 10 - depth, None
        else:
            return 0, None

    if is_maximizing:
        best_score = -sys.maxsize
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score, _ = min_max(board, depth + 1, False)
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    else:
        best_score = sys.maxsize
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score, _ = min_max(board, depth + 1, True)
                    board[i][j] = '-'
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move

def play():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Let's play Tic Tac Toe!")
    print_board(board)
    while True:
        while True:
            user_row = int(input("Enter row (0, 1, 2): "))
            user_col = int(input("Enter column (0, 1, 2): "))
            if board[user_row][user_col] == '-':
                board[user_row][user_col] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        print_board(board)
        result = evaluate(board)
        if result is not None:
            if result == 'X':
                print("Congratulations! You win!")
            elif result == 'O':
                print("Sorry, you lose!")
            else:
                print("It's a draw!")
            break
        _, (row, col) = min_max(board, 0, True)
        board[row][col] = 'O'
        print("Computer's move:")
        print_board(board)
        result = evaluate(board)
        if result is not None:
            if result == 'X':
                print("Congratulations! You win!")
            elif result == 'O':
                print("Sorry, you lose!")
            else:
                print("It's a draw!")
            break

if __name__ == "__main__":
    play()