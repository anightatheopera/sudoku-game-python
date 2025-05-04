import numpy as np
import random

#Prints the ndarray in format so it is readable(a bit at least)
def Print_Board(board):
    for i in range(9):
        for j in range(9):
            if j==0:
                print("|",end='')
            if j!=8:
                print(board[i,j],end=' ')
            else:
                print(board[i,j],end='')
            if (j+1)%3==0:
                print("|",end='')
        if (i+1)%3==0:
            print("\n---------------------",end='')
        print()

#Finds an empty cell in the board - empty cells are represented by 0
def Find_Empty_Cell(board):
    for i in range(9):
        for j in range(9):
            if board[i,j]==0:
                row=i
                col=j
                Fill_Chk=1
                res=np.array([row,col,Fill_Chk],dtype="int8")
                return res
    res=np.array([-1,-1,0])
    return res

#This function checks the validity of a number at a given position in the puzzle 
#Done according to sudoku rules
def Check_Validity(board, row, col, num):
    # Check the row
    if num in board[row, :]:
        return False

    # Check the column
    if num in board[:, col]:
        return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False

    return True

#Generates an unsolved sudoku board 
def Generate_Unsolved_Puzzle(board): 
    upper_limit = 41  # Number of cells to be removed
    cells_removed = 0

    while cells_removed < upper_limit:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row, col] != 0:  # Ensure the cell is not already empty
            board[row, col] = 0
            cells_removed += 1

#Input of the row, column and nummber to check is done here
def Play_Sudoku(Solved_Board,Unsolved_Board):
    while True:    
        row=int(input("Enter the row to insert number:")) - 1
        col=int(input("Enter the column to insert number:")) - 1
        number_check=int(input("Enter the number(or press 10 to exit):"))
        if number_check!=10:
            if Unsolved_Board[row,col]==0:
                print(Solved_Board[row,col])
                if Solved_Board[row,col]==number_check:
                    print("Correct! Updated board:")
                    Unsolved_Board[row,col]=number_check
                    Print_Board(Unsolved_Board)
                else:
                    print("Invalid number! Try again!:")
                    Print_Board(Unsolved_Board)
            else:
                print("That location is already correctly filled!")
            if np.array_equal(Solved_Board,Unsolved_Board):
                print("Congrats on solving the sudoku!")
                break
        else:
            print("\nThe solved board is:")
            Print_Board(Solved_Board)
            return

# Checks if after giving the board to the Sudoku solver, it can still figure out the puzzle
def Solve_Sudoku(board,not_check):
    x=Find_Empty_Cell(board)
    if x[2]==0:
        return True
    else:
        row=x[0]
        col=x[1]
        for i in np.random.permutation(10):
            if i!=0 and i!=not_check:
                if Check_Validity(board,row,col,i):
                    board[row,col]=i
                    if Solve_Sudoku(board,not_check):
                        return True
                    board[row,col]=0 
    return False

#Initializes playing board
def main():
    print("Hello! Welcome to Sudoku!")
    board=np.zeros((9,9),dtype="int8")
    if Solve_Sudoku(board,-1):
        Solved_Board=board.copy()
        print("\n\nThe unsolved puzzle is:\n")
        Generate_Unsolved_Puzzle(board)
        Print_Board(board)
        Unsolved_Board=board.copy()
        Play_Sudoku(Solved_Board,Unsolved_Board)
    else:
        print("The board is not possible!")
    return

if __name__=="__main__":
    main()
