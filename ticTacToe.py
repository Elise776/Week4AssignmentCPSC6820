def displayBoard(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def checkWinner(board, player):
    winningCombo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for first, second, third in winningCombo:
        if (board[first] == player and board[second] == player and board[third] == player):
            return True

    return False


def boardIsFull(board):
    return all(space in ("X", "O") for space in board)


def getPlayerMove(board, player):
    while True:
        move = input(f"Player {player}, choose a position from 1 to 9: ")

        position = int(move) - 1
        return position


def playGame():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentPlayer = "X"

    print("Player X Turn.")

    while True:
        displayBoard(board)

        position = getPlayerMove(board, currentPlayer)
        board[position] = currentPlayer

        if checkWinner(board, currentPlayer):
            displayBoard(board)
            print(f"Player {currentPlayer} wins!")
            break

        if boardIsFull(board):
            displayBoard(board)
            print("The game is a tie!")
            break

        currentPlayer = "O" if currentPlayer == "X" else "X"


if __name__ == "__main__":
    playGame()