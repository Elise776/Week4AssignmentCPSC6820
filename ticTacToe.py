def displayBoard(board, output_func=print):
    output_func("")
    output_func(f" {board[0]} | {board[1]} | {board[2]}")
    output_func("---+---+---")
    output_func(f" {board[3]} | {board[4]} | {board[5]}")
    output_func("---+---+---")
    output_func(f" {board[6]} | {board[7]} | {board[8]}")
    output_func("")


def checkWinner(board, player):
    winningCombo = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for first, second, third in winningCombo:
        if board[first] == player and board[second] == player and board[third] == player:
            return True

    return False


def boardIsFull(board):
    return all(space in ("X", "O") for space in board)


def getPlayerMove(board, player, input_func=input, output_func=print):
    while True:
        move = input_func(f"Player {player}, choose a position from 1 to 9: ")
        move = str(move).strip()

        if not move.isdigit():
            output_func("Please enter a number from 1 to 9.")
            continue

        position = int(move) - 1
        if position < 0 or position > 8:
            output_func("Please enter a number from 1 to 9.")
            continue

        if board[position] in ("X", "O"):
            output_func("That position has already been chosen.")
            continue

        return position


def askToPlayAgain(input_func=input, output_func=print):
    while True:
        response = str(input_func("Do you want to play again? (y/n): ")).strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False

        output_func("Please enter y or n.")


def playGame(input_func=input, output_func=print):
    board = [str(i) for i in range(1, 10)]
    currentPlayer = "X"

    output_func("Player X Turn.")

    while True:
        displayBoard(board, output_func=output_func)

        position = getPlayerMove(board, currentPlayer, input_func=input_func, output_func=output_func)
        board[position] = currentPlayer

        if checkWinner(board, currentPlayer):
            displayBoard(board, output_func=output_func)
            output_func(f"Player {currentPlayer} wins!")
            return currentPlayer

        if boardIsFull(board):
            displayBoard(board, output_func=output_func)
            output_func("The game is a tie!")
            return None

        currentPlayer = "O" if currentPlayer == "X" else "X"


def playMultipleGames(input_func=input, output_func=print):
    games_played = 0

    while True:
        playGame(input_func=input_func, output_func=output_func)
        games_played += 1

        if not askToPlayAgain(input_func=input_func, output_func=output_func):
            break

    return games_played


if __name__ == "__main__":
    playGame()
