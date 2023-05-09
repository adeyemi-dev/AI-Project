import math

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 1
            elif board[i][0] == 'O':
                return -1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 1
            elif board[0][i] == 'O':
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return -1
    return 0

def mini_max_alpha_beta(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if score == 0 and depth == 9:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = mini_max_alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = '-'
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score

    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = mini_max_alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = '-'
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = mini_max_alpha_beta(board, 0, -math.inf, math.inf, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def print_board(board):
    for row in board:
        print(row)

def play_game():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    player = 'X'
    while True:
        print_board(board)
        if player == 'X':
            row, col = map(int, input("Enter row and column to make a move (0-2, 0-2): ").split())
            board[row][col] = 'X'
            player = 'O'

play_game()