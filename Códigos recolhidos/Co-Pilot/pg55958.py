import numpy as np
import random

# Prints the ndarray in a readable format
def Print_Board(board):
    for i in range(9):
        for j in range(9):
            if j == 0:
                print("|", end='')
            print(board[i, j] if board[i, j] != 0 else ".", end=' ')
            if (j + 1) % 3 == 0:
                print("|", end=' ')
        print()
        if (i + 1) % 3 == 0:
            print("---------------------")

# Finds an empty cell in the board - empty cells are represented by 0
def Find_Empty_Cell(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return i, j
    return None

# This function checks the validity of a number at a given position in the puzzle
def Check_Validity(board, row, col, num):
    # Check row
    if num in board[row, :]:
        return False
    # Check column
    if num in board[:, col]:
        return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i, j] == num:
                return False
    return True

# Solves the Sudoku board using backtracking
def Solve_Sudoku(board):
    empty_cell = Find_Empty_Cell(board)
    if not empty_cell:
        return True  # Puzzle solved
    row, col = empty_cell

    for num in range(1, 10):
        if Check_Validity(board, row, col, num):
            board[row, col] = num
            if Solve_Sudoku(board):
                return True
            board[row, col] = 0  # Backtrack

    return False

# Generates a solved Sudoku board
def Generate_Solved_Board():
    board = np.zeros((9, 9), dtype="int8")
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(9):
        board[i, i] = numbers[i % 9]  # Add initial constraints for validity
    Solve_Sudoku(board)
    return board

# Generates an unsolved Sudoku puzzle by removing numbers
def Generate_Unsolved_Puzzle(board, clues=30):
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells[:81 - clues]:
        board[i, j] = 0

# Allows the user to play Sudoku
def Play_Sudoku(solved_board, unsolved_board):
    while True:
        Print_Board(unsolved_board)
        try:
            row = int(input("Enter the row (1-9, or 0 to quit): ")) - 1
            if row == -1:
                print("Exiting the game. The solved board was:")
                Print_Board(solved_board)
                break
            col = int(input("Enter the column (1-9): ")) - 1
            num = int(input("Enter the number (1-9): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if unsolved_board[row, col] == 0:
            if solved_board[row, col] == num:
                unsolved_board[row, col] = num
                print("Correct!")
                if np.array_equal(solved_board, unsolved_board):
                    print("Congratulations! You solved the Sudoku!")
                    break
            else:
                print("Incorrect number. Try again.")
        else:
            print("Cell already filled. Choose another.")

# Main function
def main():
    print("Welcome to Sudoku!")
    solved_board = Generate_Solved_Board()
    unsolved_board = solved_board.copy()
    Generate_Unsolved_Puzzle(unsolved_board, clues=30)
    print("Here is your puzzle:")
    Play_Sudoku(solved_board, unsolved_board)

if __name__ == "__main__":
    main()
